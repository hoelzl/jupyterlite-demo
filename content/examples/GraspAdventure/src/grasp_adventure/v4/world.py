from dataclasses import dataclass
from typing import Any, Dict
import sys

from .location import Location

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    TypeAlias = Any

LocationDict: TypeAlias = Dict[str, Location]


@dataclass
class World:
    location_dict: LocationDict
    initial_location_name: str

    def __getitem__(self, location_name: str):
        """Return the connected location in direction `location_name`.

        >>> from grasp_adventure.v4.game_factory import GameFactory
        >>> world = GameFactory().create_world([{"name": "A"}, {"name": "B"}])
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

    @property
    def description(self):
        return "Nothing noteworthy is happening in the world."
