from __future__ import annotations

from typing import TYPE_CHECKING

from armor import LeatherCap
from characters import PC, Character, Enemy
from status import Bleeding
from slots import Slots
from weapons import SmallSword

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


if __name__ == "__main__":
    slots = Slots()
    enemy_slots = Slots()
    pc = PC(name="PC", damage=1, kind="warrior", slots=slots)
    enemy = Enemy(name="Baddie", kind="bandit", slots=enemy_slots)
    bleeding = Bleeding()
    bleeding2 = Bleeding()
    bleeding2.level = 2
    bleeding.from_level()
    pc.add_status(bleeding)
    do_attack(pc, enemy)
    do_attack(enemy, pc)
    while enemy.hp:
        do_attack(pc, enemy)
        for status in pc.status_list:
            status.apply_effect(pc)
    print(pc)
    sword = SmallSword()
    do_equip(pc, sword)
    helmet = LeatherCap()
    do_equip(pc, helmet)
    print(pc)
    print(enemy)
