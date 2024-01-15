from __future__ import annotations

import random
from typing import TYPE_CHECKING

from characters import Character
from attacks import MagicAttack
from weapons import Weapon
from status import Status

if TYPE_CHECKING:
    from items import Item


def do_attack(attacker: Character, defender: Character) -> str:
    damage = attacker.attack(defender)
    weapon = attacker.slots.hand
    if weapon and weapon.status_chance:
        if weapon.status_chance < random.random():
            add_status(defender, weapon)
    result = (
        f"{attacker.name} hits {defender.name} for {damage} damage."
        f" Remaining HP: {defender.hp}."
    )
    print(result)
    return result


def do_magic_attack(attacker: Character, defender: Character, attack: MagicAttack) -> str:
    defender.hp -= attack.damage
    attacker.mp -= attack.mp_cost
    if attack.status_chance:
        if attack.status_chance < random.random():
            add_status(defender, attack)
    result = (
        f"{attacker.name} hits {defender.name} with {attack.name} for {attack.damage} damage."
        f" Remaining HP: {defender.hp}."
    )
    print(result)
    return result


def add_status(character: Character, source: Weapon | MagicAttack):
    st = source.status()
    st.level = source.status_level
    if hasattr(st, "from_level"):
        st.from_level()
    character.add_status(st)
    print(f"Added {st.name} {st.level} to {character.name}.")


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
