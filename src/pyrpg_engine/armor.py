"""Armor classes."""

from __future__ import annotations

from dataclasses import dataclass

from items import Item


@dataclass
class Armor(Item):
    defense: int = 0


@dataclass
class BodyArmor(Armor):
    kind: str = "bodyarmor"


@dataclass
class LeatherArmor(BodyArmor):
    defense: int = 1
    name: str = "Leather Armor"
    value: int = 1
    level: int = 1
    size: int = 2


@dataclass
class Shield(Armor):
    kind: str = "shield"


@dataclass
class WoodenShield(Shield):
    defense: int = 1
    name: str = "Wooden Shield"
    value: int = 1
    level: int = 1
    size: int = 1


@dataclass
class Helmet(Armor):
    kind: str = "helmet"


@dataclass
class LeatherCap(Helmet):
    defense: int = 1
    name: str = "Leather Cap"
    value: int = 1
    level: int = 1
    size: int = 1
