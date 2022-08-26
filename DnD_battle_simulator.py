import os
import sys
import random
import time
import pygame
import configparser
import gog
import Raycasting

import NPC_class as npc
import dictionaries as misc


class Button:
    def __init__(self, x, y, width, height, objects, button_text='Button', onclick_function=None, one_press=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclick_function
        self.onePress = one_press
        self.reply = generate_map()
        font = pygame.font.SysFont('Arial', 10)

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(button_text, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self, scr):

        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.reply = self.onclickFunction()

                elif not self.alreadyPressed:
                    self.reply = self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        scr.blit(self.buttonSurface, self.buttonRect)


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


def populate_map(hero, npc_list, my_map):
    pass


def my_function():
    pass


def tileset_test():

    pygame.init()

    fps = 60
    fpsClock = pygame.time.Clock()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    surfaceOne = pygame.Surface((100, 100))
    surfaceOne.fill((200, 100, 100,))

    surfaceTwo = pygame.Surface((30, 30))
    surfaceTwo.fill((100, 200, 100,))

    surfaceOne.blit(
        surfaceTwo,
        [10, 10],
        [0, 0, 10, 5]
    )
    tiles = tileset_load()

    # Game loop.
    while True:
        screen.fill((20, 20, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # screen.blit(surfaceOne, [10, 10])
        screen.blit(tiles[2], [10, 10])

        pygame.display.flip()
        fpsClock.tick(fps)


def tileset_load():

    pieces = pygame.image.load(os.path.join("res/img/character_and_tileset", "Dungeon_Character.png")).convert_alpha()

    char1 = pygame.Surface.subsurface(pieces, (64, 0, 16, 16))

    char01a = pygame.Surface.subsurface(pieces, (0 , 0 , 16, 16))
    char02a = pygame.Surface.subsurface(pieces, (16, 0 , 16, 16))
    char03a = pygame.Surface.subsurface(pieces, (32, 0 , 16, 16))
    char04a = pygame.Surface.subsurface(pieces, (48, 0 , 16, 16))
    char05a = pygame.Surface.subsurface(pieces, (64, 0 , 16, 16))
    char06a = pygame.Surface.subsurface(pieces, (80, 0 , 16, 16))
    char07a = pygame.Surface.subsurface(pieces, (96, 0 , 16, 16))

    mob01a = pygame.Surface.subsurface(pieces, (0 , 16, 16, 16))
    mob02a = pygame.Surface.subsurface(pieces, (16, 16, 16, 16))
    mob03a = pygame.Surface.subsurface(pieces, (32, 16, 16, 16))
    mob04a = pygame.Surface.subsurface(pieces, (48, 16, 16, 16))
    mob05a = pygame.Surface.subsurface(pieces, (64, 16, 16, 16))
    mob06a = pygame.Surface.subsurface(pieces, (80, 16, 16, 16))
    mob07a = pygame.Surface.subsurface(pieces, (96, 16, 16, 16))

    char01b = pygame.Surface.subsurface(pieces, (0 , 32, 16, 16))
    char02b = pygame.Surface.subsurface(pieces, (16, 32, 16, 16))
    char03b = pygame.Surface.subsurface(pieces, (32, 32, 16, 16))
    char04b = pygame.Surface.subsurface(pieces, (48, 32, 16, 16))
    char05b = pygame.Surface.subsurface(pieces, (64, 32, 16, 16))
    char06b = pygame.Surface.subsurface(pieces, (80, 32, 16, 16))
    char07b = pygame.Surface.subsurface(pieces, (96, 32, 16, 16))

    mob01b = pygame.Surface.subsurface(pieces, (0 , 48, 16, 16))
    mob02b = pygame.Surface.subsurface(pieces, (16, 48, 16, 16))
    mob03b = pygame.Surface.subsurface(pieces, (32, 48, 16, 16))
    mob04b = pygame.Surface.subsurface(pieces, (48, 48, 16, 16))
    mob05b = pygame.Surface.subsurface(pieces, (64, 48, 16, 16))
    mob06b = pygame.Surface.subsurface(pieces, (80, 48, 16, 16))
    mob07b = pygame.Surface.subsurface(pieces, (96, 48, 16, 16))

    tileset_chars = [char01a, char02a, char03a, char04a, char05a, char06a, char07a]
    tileset_mobs = [mob01a, mob02a, mob03a, mob04a, mob05a, mob06a, mob07a]
    return tileset_chars, tileset_mobs



def generate_map():
    my_map = gog.Map()
    my_map.generateLevel()
    my_map.useCellularAutomata()
    my_map.make_map_dict()
    return my_map


def main2():
    config = configparser.ConfigParser(strict=False)
    config.read("settings.cfg")
    num_columns     = config.getint("map", "map_height_cells")
    num_rows        = config.getint("map", "map_width_cells")
    pixel_width     = config.getint("map", "num_rows")
    pixel_height    = config.getint("map", "num_columns")
    margin          = config.getint("map", "margin")
    my_map = None
    extra = (pixel_width+margin)*num_columns
    objects = []
    run_battle = False
    hero = None
    npc_list = []
    location = [0, 0]
    selection = 0

    scr = init_pygame_window(pixel_width, pixel_height, margin, num_columns, num_rows, extra)

    x1 = extra + 100
    y1 = 660
    x1d = 100
    y1d = 20
    x2 = extra + 100
    y2 = 700
    x2d = 100
    y2d = 20

    custom_button1 = Button(x1, y1, x1d, y1d, objects, 'Reset (onePress)', generate_map)
    custom_button2 = Button(x2, y2, x2d, y2d, objects, 'Start (onePress)', generate_map)

    tileset_chars, tileset_mobs = tileset_load()

    done = False
    clock = pygame.time.Clock()
    black = (0, 0, 0)

    # main Loop
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = pos[0] // (pixel_width + margin)
                column = pos[1] // (pixel_height + margin)
                print("Click ", pos, "Grid coordinates: ", row, column)

                # check if the click is on the button
                if custom_button1.buttonRect.collidepoint(pos):
                    if custom_button1.reply:
                        my_map = custom_button1.reply

                # check is second button pressed and the map populated then runs the battle sim
                if custom_button2.buttonRect.collidepoint(pos) and my_map:
                    run_battle = True
                    hero = npc.Hero(random.choice(list(misc.dListOfNamesD.keys())))  # chose hero name randomly
                    npc_list.append(npc.Mob(random.choice(misc.challenge_1)))
                    populate_map(hero, npc_list, my_map)

                    location = random.choice(list(my_map.freeSpaces()))
                    selection = random.randint(0, 6)


                # checks if we click in the battle map
                if (pixel_width + margin) * num_columns + margin > pos[0] and \
                        (pixel_height + margin) * num_rows > pos[1]:
                    # my_map.mdict[row, column][0] = 5

                    fov_list = Raycasting.fov_calc(row, column, 5, my_map.level, my_map.mdict, num_columns,
                                                   num_rows)
        if run_battle:
            pass
            '''
                main logic:
                1. divide fight to phases
                    a. who goes first
                    b. select action
            '''
        scr.fill(black)
        for obj in objects:
            obj.process(scr)

        if my_map:
            update_grid(pixel_width, pixel_height, margin, num_columns, num_rows, scr, my_map.mdict)

            scr.blit(tileset_chars[selection], [(pixel_width + margin) * location[0]+1, (pixel_height + margin) * location[1]+1])

            # update the sprites ! not done yet
            # update_items()

        clock.tick(50)
        pygame.display.flip()
    pygame.quit()


def init_pygame_window(width, height, margin, grid_size_x, grid_size_y, extra=0):
    pygame.display.set_caption("Grid")
    window_size = [(width + margin) * grid_size_x + margin + extra, (height + margin) * grid_size_y + margin]
    scr = pygame.display.set_mode(window_size)
    pygame.init()
    return scr


def update_grid(width, height, margin, grid_size_x, grid_size_y, scr, my_map):
    black = (0, 0, 0)
    red = (255, 0, 0)
    grey = (105, 105, 105)
    # grey = (0, 0, 0)
    # grey = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    white = (255, 255, 255)

    for row in range(grid_size_x):
        for column in range(grid_size_y):
            color = white

            # if my_map[row][column] in [1]:
            if my_map[column, row][0] in [1]: # wall
                color = black

            # if my_map[row][column] in [2]:
            if my_map[column, row][0] in [2]: # FOV
                color = grey

            if my_map[column, row][0] in [5]: # player
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


def pygame_test_buttons():
    # Imports
    import sys
    import pygame

    # Configuration
    pygame.init()
    fps = 60
    fpsClock = pygame.time.Clock()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))

    font = pygame.font.SysFont('Arial', 10)

    objects = []

    class Button():
        def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.onclickFunction = onclickFunction
            self.onePress = onePress

            self.fillColors = {
                'normal': '#ffffff',
                'hover': '#666666',
                'pressed': '#333333',
            }

            self.buttonSurface = pygame.Surface((self.width, self.height))
            self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

            self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

            self.alreadyPressed = False

            objects.append(self)

        def process(self):

            mousePos = pygame.mouse.get_pos()

            self.buttonSurface.fill(self.fillColors['normal'])
            if self.buttonRect.collidepoint(mousePos):
                self.buttonSurface.fill(self.fillColors['hover'])

                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    self.buttonSurface.fill(self.fillColors['pressed'])

                    if self.onePress:
                        self.onclickFunction()

                    elif not self.alreadyPressed:
                        self.onclickFunction()
                        self.alreadyPressed = True

                else:
                    self.alreadyPressed = False

            self.buttonSurface.blit(self.buttonSurf, [
                self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
                self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
            ])
            screen.blit(self.buttonSurface, self.buttonRect)

    def myFunction():
        print('Button Pressed')

    customButton = Button(30, 30, 100, 100, 'Button One (onePress)', myFunction)
    customButton = Button(30, 180, 100, 100, 'Button Two (multiPress)', myFunction, True)

    # Game loop.
    while True:
        screen.fill((20, 20, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for object in objects:
            object.process()

        pygame.display.flip()
        fpsClock.tick(fps)


if __name__ == "__main__":
    # main()
    main2()
    # tileset_test()
    # test_map_generator()
    # pygame_test_buttons()
