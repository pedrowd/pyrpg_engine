from slots import Slots
from armor import LeatherCap
from characters import PC, Enemy
from game import do_attack, do_equip
from status import Bleeding
from weapons import SmallSword

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
