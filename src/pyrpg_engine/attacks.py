"""Attack system classes."""
from __future__ import annotations

import random
from dataclasses import dataclass

from status import Status, Bleeding


@dataclass
class Attack:
    name: str = ""
    damage: int = 0
    status: Status | None = None
    status_chance: int = 0
    status_always:  bool = False
    status_level: int = 0
    if status_chance < 0:
        status_always = True

@dataclass
class MagicAttack(Attack):
    name: str = ""
    mp_cost: int = 0
    status: Status | None = None
    status_chance: int = 0
    status_always: bool = False
    status_level: int = 0
    damage: int = 0

    def __post_init__(self):
        if self.status_chance < 0:
            self.status_always = True


@dataclass
class SpikeSlash(MagicAttack):
    name: str = "Spike Slash"
    mp_cost: int = 15
    status: type[Status] = Bleeding
    status_level: int = 1
    status_chance: int = -1
    damage: int = random.randint(10, 15)


s = SpikeSlash()
print(s.status_always)
