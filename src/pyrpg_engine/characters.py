"""Character classes."""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, cast

from armor import Armor, BodyArmor, Helmet, Shield
from journeys.status import Status
from slots import Slots
from weapons import Weapon

if TYPE_CHECKING:
    from items import Item


@dataclass
class Character:
    name: str = ""
    level: int = 1
    mp: int = 30
    max_mp: int = 30
    hp: int = 40
    max_hp: int = 40
    defense: int = 0
    damage: int = 0
    kind: str = ""
    slots: Slots | None = None
    status_list: list[Status] = field(default_factory=list)

    def attack(self, other: Character) -> int:
        attack_roll = random.randint(0, 4)
        defense_roll = random.randint(0, 2)
        damage = self.damage * attack_roll - other.defense * defense_roll
        damage = max(damage, 0)
        other.hp -= damage
        other.hp = max(other.hp, 0)
        return damage

    def heal(self, amount: int) -> int:
        old_hp = self.hp
        self.hp += amount
        self.hp = max(self.hp, self.max_hp)
        return self.hp - old_hp

    def level_up(self) -> None:
        self.level += 1
        self.max_hp += 5
        self.hp = self.max_hp

    def equip(self, item: Item) -> str:
        self.slots = cast(Slots, self.slots)
        if isinstance(item, Weapon):
            self.slots.hand = item
            self.damage += item.damage
        elif isinstance(item, Armor):
            if isinstance(item, Shield):
                self.slots.arm = item
            elif isinstance(item, BodyArmor):
                self.slots.body = item
            elif isinstance(item, Helmet):
                self.slots.head = item
            self.defense += item.defense
        return item.name

    def unequip(self, slot: str) -> str:
        old_item: Item = getattr(self.slots, slot)
        if hasattr(old_item, "defense"):
            old_item = cast(Armor, old_item)
            self.defense -= old_item.defense
        elif hasattr(old_item, "damage"):
            old_item = cast(Weapon, old_item)
            self.damage -= old_item.damage
        setattr(self.slots, slot, None)
        return old_item.name

    def add_status(self, status: Status) -> None:
        self.status_list.append(status)

    def remove_status(self, status: Status) -> None:
        self.status_list.remove(status)

    def __repr__(self) -> str:
        self.slots = cast(Slots, self.slots)
        hand = f"On hand: {self.slots.hand.name if self.slots.hand else '' : <15}"
        hand_damage = f"Damage: +{self.slots.hand.damage if self.slots.hand else 0}"
        arm = f"On arm: {self.slots.arm.name if self.slots.arm else '' : <16}"
        arm_defense = f"Defense: +{self.slots.arm.defense if self.slots.arm else 0}"
        body = f"On body: {self.slots.body.name if self.slots.body else '' : <15}"
        body_defense = f"Defense: +{self.slots.body.defense if self.slots.body else 0}"
        head = f"On head: {self.slots.head.name if self.slots.head else '' : <15}"
        head_defense = f"Defense: +{self.slots.head.defense if self.slots.head else 0}"
        sheet = f"""        {self.kind.title()}
        Name: {self.name}
        Level: {self.level}
        HP: {self.hp} / {self.max_hp}
        MP: {self.mp} / {self.max_mp}
        Defense: {self.defense}     Damage: {self.damage}
        Wearing:
            {hand} - {hand_damage}
            {arm} - {arm_defense}
            {body} - {body_defense}
            {head} - {head_defense}
        Statuses:
            {" ".join(f"{status.name} level {status.level}" for status in self.status_list)}
        """
        return sheet


class PC(Character):
    pass


class NPC(Character):
    pass


class Enemy(Character):
    pass
