"""Status classes."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from characters import Character


@dataclass
class Status:
    name: str = ""
    id: int = 0
    level: int = 0
    max_level: int = 0
    duration: int = 0
    infinite: bool = False
    damage: int = 0
    if duration < 0:
        infinite = True

    def apply_effect(self, character: Character):
        pass

@dataclass
class Bleeding(Status):
    name: str = "Bleeding"
    id: int = 1
    level: int = 1
    max_level: int = 3

    def from_level(self):
        if self.level == 1:
            self.duration = 2
            self.damage = random.randint(5, 10)
        elif self.level == 2:
            self.duration = 3
            self.damage = random.randint(8, 15)
        elif self.level == 3:
            self.duration = 4
            self.damage = random.randint(10, 20)

    def apply_effect(self, character: Character):
        character.hp -= self.damage
        print(f"{self.name} {self.level} has duration: {self.duration}.")
        print(f"{character.name} received {self.damage} damage from {self.name} {self.level}. Remaining HP: {character.hp}.")
        self.duration -= 1
        if self.duration < 1:
            character.status_list.remove(self)
