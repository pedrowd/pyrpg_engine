"""Weapon classes."""

from __future__ import annotations

from dataclasses import dataclass, field

from items import Item
from status import Status, Bleeding


@dataclass
class Weapon(Item):
    damage: int = 0
    range: int = 0
    name: str = "Weapon"
    status: type[Status] | None = None
    status_chance: float = 0.0
    status_level: int = 0


@dataclass
class Sword(Weapon):
    kind: str = "sword"
    range: int = 1


@dataclass
class SmallSword(Sword):
    damage: int = 1
    name: str = "Small Sword"
    value = 1
    level = 1
    size = 1


@dataclass
class SmallSharpSword(Sword):
    damage: int = 1
    name: str = "Small Sharp Sword"
    value: int = 2
    level: int = 2
    size: int = 1
    status: type[Status] | None = Bleeding
    status_chance: float = 0.2
    status_level: int = 1
