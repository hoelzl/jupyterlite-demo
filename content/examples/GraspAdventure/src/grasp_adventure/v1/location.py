from dataclasses import dataclass, field
from typing import Any, Sequence, Mapping
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
