"""Item classes."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Item:
    name: str = ""
    kind: str = ""
    value: int = 0
    level: int = 0
    size: int = 0
    if kind == "heal":
        heal: int = 0
