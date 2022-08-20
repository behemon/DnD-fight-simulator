import random
import time
import pygame

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


def init_pygame_window(width, height, margin, grid_size_x, grid_size_y):
    pygame.display.set_caption("Grid")
    window_size = [(width + margin) * grid_size_x + margin, (height + margin) * grid_size_y + margin]
    scr = pygame.display.set_mode(window_size)
    pygame.init()
    return scr


def update_grid(width, height, margin, grid_size_x, grid_size_y, scr, my_map):
    black = (0, 0, 0)
    red = (255, 0, 0)
    grey = (105, 105, 105)
    white = (255, 255, 255)

    for row in range(grid_size_x):
        for column in range(grid_size_y):
            color = white

            # if my_map[row][column] in [1]:
            if my_map[row, column][0] in [1]: # wall
                color = black

            # if my_map[row][column] in [2]:
            if my_map[row, column][0] in [2]: # FOV
                color = grey

            if my_map[row, column][0] in [5]: # player
                color = red

            pygame.draw.rect(scr,
                             color,
                             [(margin + width) * column + margin,
                              (margin + height) * row + margin,
                              width,
                              height])
            
            
def test_map_generator():

    import configparser
    import gog
    import Raycasting

    config = configparser.ConfigParser(strict=False)
    config.read("settings.cfg")
    num_columns     = config.getint("map", "map_height_cells")
    num_rows        = config.getint("map", "map_width_cells")
    pixel_width     = config.getint("map", "num_rows")
    pixel_height    = config.getint("map", "num_columns")
    margin          = config.getint("map", "margin")

    scr = init_pygame_window(pixel_width, pixel_height, margin, num_columns, num_rows)

    my_map = gog.Map()
    my_map.generateLevel()
    my_map.useCellularAutomata()
    my_map.make_map_dict()
    update_grid(pixel_width, pixel_height, margin, num_columns, num_rows, scr, my_map.mdict)

    rand_spot = random.choice(my_map.freeSpaces())
    my_map.mdict[rand_spot[0], rand_spot[1]][0] = 5

    fov_list = Raycasting.fov_calc(rand_spot[0], rand_spot[1], 5, my_map.level, my_map.mdict, num_columns, num_rows)
    print(fov_list)

    done = False
    clock = pygame.time.Clock()
    black = (0, 0, 0)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (pixel_width + margin)
                row = pos[1] // (pixel_height + margin)
                print("Click ", pos, "Grid coordinates: ", row, column)

                my_map.mdict[row, column][0] = 5
                fov_list = Raycasting.fov_calc(row, column, 5, my_map.level, my_map.mdict, num_columns,
                                               num_rows)

        scr.fill(black)
        update_grid(pixel_width, pixel_height, margin, num_columns, num_rows, scr, my_map.mdict)
        clock.tick(50)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    # main()
    test_map_generator()
