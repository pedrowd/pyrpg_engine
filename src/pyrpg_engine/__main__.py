from slots import Slots
from armor import LeatherCap
from characters import PC, Enemy
from game import do_attack, do_equip, do_magic_attack
from attacks import SpikeSlash
from status import Bleeding
from weapons import SmallSword, SmallSharpSword

if __name__ == "__main__":
    slots = Slots()
    enemy_slots = Slots()
    pc = PC(name="PC", damage=1, kind="warrior", slots=slots, hp=100)
    enemy = Enemy(name="Baddie", kind="bandit", slots=enemy_slots)
    # bleeding = Bleeding()
    # bleeding2 = Bleeding()
    # bleeding2.level = 2
    # bleeding.from_level()
    # pc.add_status(bleeding)
    sword = SmallSharpSword()
    do_equip(pc, sword)
    do_attack(pc, enemy)
    do_attack(enemy, pc)
    do_magic_attack(enemy, pc, SpikeSlash())
    do_magic_attack(enemy, pc, SpikeSlash())
    while enemy.hp > 0:
        do_attack(pc, enemy)
        for status in pc.status_list:
            status.apply_effect(pc)
        for status in enemy.status_list:
            status.apply_effect(enemy)
    print(pc)
    helmet = LeatherCap()
    do_equip(pc, helmet)
    print(pc)
    print(enemy)
