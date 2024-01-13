"""Slots."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armor import BodyArmor, Helmet, Shield
    from weapons import Weapon


@dataclass
class Slots:
    hand: Weapon | None = None
    arm: Shield | None = None
    body: BodyArmor | None = None
    head: Helmet | None = None
