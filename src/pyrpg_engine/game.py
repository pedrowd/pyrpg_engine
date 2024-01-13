from __future__ import annotations

from typing import TYPE_CHECKING

from characters import Character

if TYPE_CHECKING:
    from items import Item


def do_attack(attacker: Character, defender: Character) -> str:
    damage = attacker.attack(defender)
    result = (
        f"{attacker.name} hits {defender.name} for {damage} damage."
        f" Remaining HP: {defender.hp}."
    )
    print(result)
    return result


def do_equip(character: Character, item: Item) -> str:
    item_name = character.equip(item)
    info = ""
    if hasattr(item, "damage"):
        info = f" (+{item.damage} damage)"
    elif hasattr(item, "defense"):
        info = f" (+{item.defense} defense)"
    result = f"{character.name} has equipped {item_name}{info}."
    print(result)
    return result
