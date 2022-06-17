import random
import time

import NPC_class as npc
import dictionaries as misc


def rand_gen(start_num: int, end_num: int):
    return random.randint(start_num, end_num)


def dice_roll(dice):
    x = dice.split("d")
    result = 0
    for times in range(int(x[0])):
        result += rand_gen(1, int(x[1]))
    return result


def full_dice_roll(x):
    x = x.split()
    result = dice_roll(x[0])
    if len(x) > 1:
        stringa = "%s%s%s" % (result, x[1], x[2])
        result = eval(stringa)
    if result <= 0:
        result = 1
    # print "dmg type:",x,result
    return result


def check_initiative(hero, monster):
    hero_initiative = misc.dScoreModifier[hero.dDex]
    monster_initiative = misc.dScoreModifier[monster.dDex]
    if hero_initiative >= monster_initiative:
        return True
    return False


def d_attack(attacker, attacked):
    my_dice_roll = rand_gen(1, 20)
    if my_dice_roll == 1:
        return
    elif my_dice_roll == 20:
        attacked.HitPoints -= damage_calc(attacker) + damage_calc(attacker)
    else:
        if my_dice_roll + misc.dScoreModifier[attacker.dStr] > attacked.AC:
            attacked.HitPoints -= damage_calc(attacker)


def damage_calc(attacker):
    # melee attack

    x = full_dice_roll(attacker.weapon) + misc.dScoreModifier[attacker.dStr]
    if x < 0:
        return 0
    return x

    # ranged attack not implemented
    # return randGen(dItemsWeaponsRanged.get(attacker.weapon)[0], dItemsWeaponsRanged.get(attacker.weapon)[1]) + \
    #        dScoreModifier[attacker.dDex]


def run_fight(hero, mob):
    hero.dCheckStatus()
    mob.dCheckStatus()

    turn = check_initiative(hero, mob)

    while mob.alive and hero.alive:
        if turn:
            time.sleep(0.2)
            d_attack(hero, mob)
            turn = False

        else:
            time.sleep(0.2)
            d_attack(mob, hero)
            turn = True

        hero.dCheckStatus()
        mob.dCheckStatus()
        time.sleep(0.2)
        my_string = f"hero HP:{hero.HitPoints} monster HP:{mob.HitPoints}"
        print(my_string)
        # print(hero.HitPoints, mob.HitPoints)


def main():
    hero = npc.Hero(random.choice(list(misc.dListOfNamesD.keys())))  # chose hero name randomly
    mob = npc.Mob(random.choice(misc.challenge_1))
    print(hero.name, mob.name, flush=True)
    run_fight(hero, mob)


if __name__ == "__main__":
    main()
