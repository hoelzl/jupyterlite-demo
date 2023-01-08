from dataclasses import dataclass, field
from typing import Any, Dict
import sys

from .location import Location, LocationDescriptions

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    TypeAlias = Any

if sys.version_info >= (3, 11):
    from typing import Self
else:
    Self = Any

LocationDict: TypeAlias = Dict[str, Location]


@dataclass
class World:
    location_dict: LocationDict
    initial_location_name: str

    def __getitem__(self, location_name: str):
        """Return the connected location in direction `location_name`.

        >>> world = World.from_location_descriptions([{"name": "A"}, {"name": "B"}])
        >>> world["A"]
        Location(name='A', connections={})
        >>> world["B"]
        Location(name='B', connections={})
        >>> world["C"]
        Traceback (most recent call last):
        ...
        KeyError: 'C'
        """
        return self.location_dict[location_name]

    @classmethod
    def from_location_descriptions(
        cls, location_descriptions: LocationDescriptions
    ) -> Self:
        """Create a World from a description of its locations.

        >>> World.from_location_descriptions(
        ...         [{"name": "A", "connections": {"east": "B"}},
        ...          {"name": "B", "connections": {"west": "A"}}])
        World(location_dict={'A': Location(name='A', connections={'east': ...}),
                            'B': Location(name='B', connections={'west': ...})},
              initial_location_name='A')
        """
        return cls(
            location_dict=(_create_location_dict(location_descriptions)),
            initial_location_name=location_descriptions[0]["name"],
        )


def _create_location_dict(location_descriptions: LocationDescriptions) -> LocationDict:
    """Create a location dictionary from descriptions.

    >>> _create_location_dict(
    ...         [{"name": "A", "connections": {"east": "B"}},
    ...          {"name": "B", "connections": {"west": "A"}}])
    {'A': Location(name='A',
          connections={'east': Location(name='B', connections={'west': ...})}),
     'B': Location(name='B',
          connections={'west': Location(name='A', connections={'east': ...})})}
    """
    locations = _create_location_dict_without_connections(location_descriptions)
    _build_connections_for_all_locations(locations, location_descriptions)
    return locations


def _create_location_dict_without_connections(
    location_descriptions: LocationDescriptions,
) -> LocationDict:
    location_dict = {
        location_description["name"]: Location(location_description["name"])
        for location_description in location_descriptions
    }
    return location_dict


def _build_connections_for_all_locations(
    location_dict: LocationDict, location_descriptions: LocationDescriptions
):
    for location_description in location_descriptions:
        connections = {
            direction: location_dict[name]
            for direction, name in location_description.get("connections", {}).items()
        }
        location_dict[location_description["name"]].connections = connections
