from dataclasses import dataclass, field
from typing import Any, Sequence, Mapping, Dict
import sys

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    TypeAlias = Any

LocationDescription: TypeAlias = Mapping[str, Any]
LocationDescriptions: TypeAlias = Sequence[LocationDescription]


@dataclass
class Location:
    name: str
    connections: Dict[str, "Location"] = field(default_factory=dict)

    def __getitem__(self, direction: str) -> "Location":
        return self.connections.get(direction)
