from dataclasses import dataclass

from .base_classes import Action
from .location import Location


@dataclass
class Pawn:
    location: Location

    @property
    def actions(self):
        return self.location.move_actions
