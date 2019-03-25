########
#   http://www.wikihow.com/Create-a-Dungeons-and-Dragons-Character
#   https://docs.google.com/spreadsheets/d/1fjnoCiYUCOcrMxffWNwppHfuUDlY1Ae0HQ4t-XCaiPA/edit#gid=0
#   https://drive.google.com/file/d/0B8mF8uNMRN_mLUJRNmkwaDB3R3M/view
#   https://www.dandwiki.com/wiki/5e_Weapons
#   https://stackoverflow.com/questions/20149483/python-canvas-and-grid-tkinter
#   http://media.wizards.com/2016/downloads/DND/DMBasicRulesV05.pdf
#
#   1.map - make random rooms
#   2.hero - smart decision making
#   3.monster - more than one monster, loot drops
#   4.loot - add reach to melee weapons and use it
#   5.fight - ranged fight,
#   6.NPC's - in safe spaces, sell,buy
#   7.shrines - health regen
#   8.action tick - use units speed as base of movement
#
########
import random
import sys
import copy
from time import sleep
import tkinter
from tkinter import N, S, E, W
from A_star_algorithm import pathFind

# import canvas_test as maps
from dictionaries import *
import monster_dictionary as MD


class mainMap():
    def __init__(self, gui):
        self.columns = 30
        self.rows = 30
        self.numberOfRooms = 8
        self.roomMinSize = 3
        self.roomMaxSize = 6
        self.mapMatrix = {}
        self.makeMatrixDict()
        self.roomsList = []

    def makeMatrixDict(self):
        for x in range(self.columns):
            for y in range(self.rows):
                self.roomsList = []
                self.mapMatrix[y, x] = [1, None]

    def makeRoom(self):
        for tries in range(20):
            size = random.randrange(self.roomMinSize, self.roomMaxSize)# + 2
            x_start = random.randrange(0, self.rows - size)
            y_start = random.randrange(0, self.columns - size)
            room = [x_start,y_start,size]
            if self.checkRoomLocation(room):
                self.roomsList.append(room)
                for x in range(x_start, x_start + size ):
                    for y in range(y_start, y_start + size):
                        self.mapMatrix[x,y][0] = None

                # for x in range(x_start, x_start + size + 1):
                #     self.mapMatrix[x, y_start][0] = 1
                #     self.mapMatrix[x, y_start + size][0] = 1
                #
                # for y in range(y_start, y_start + size + 1):
                #     self.mapMatrix[x_start, y][0] = 1
                #     self.mapMatrix[x_start + size, y][0] = 1

                break

    def checkRoomLocation(self,testRoom):

        def intersects(testRoom, room):
            # (R1.topLeft.x < R2.bottomRight.x) &&
            # (R1.bottomRight.x > R2.topLeft.x) &&
            # (R1.topLeft.y < R2.bottomRight.y) &&
            # (R1.bottomRight.y > R2.topLeft.y)
            return not (
                    testRoom[0] <= room[0] + room[2] and
                    testRoom[0] + testRoom[2] >= room[0] and
                    testRoom[1] <= room[1] + room[2] and
                    testRoom[1] + testRoom[2] >= room[1]
            )
        for room in self.roomsList:
            if not intersects(testRoom,room):
                return False
        return True

    def makeRooms(self):
        for room in range(self.numberOfRooms):
            self.makeRoom()

    def makeRoomPath(self,point_a,point_b):
        def forx(x,y,d):
            for xa in range(d):
                self.mapMatrix[x+xa, y][0] = None

        def fory(x,y,d):
            for ya in range(d):
                self.mapMatrix[x, y+ya][0] = None

        if point_a[0] > point_b[0]:
            forx(point_b[0], point_a[1], point_a[0] - point_b[0]+1)
            if point_a[1] > point_b[1]:
                fory(point_b[0], point_b[1], point_a[1] - point_b[1]+1)
            else:
                fory(point_b[0], point_a[1], point_b[1] - point_a[1]+1)
        else:
            forx(point_a[0], point_b[1], point_b[0] - point_a[0]+1)
            if point_b[1] > point_a[1]:
                fory(point_a[0], point_a[1], point_b[1] - point_a[1]+1)
            else:
                fory(point_a[0], point_b[1], point_a[1] - point_b[1]+1)

    def makeRoomPaths(self):
        points = []
        for room in self.roomsList:
            room_senter_x = random.randrange(room[0],room[0]+room[2])
            room_senter_y = random.randrange(room[1],room[1]+room[2])
            # print (room_senter_x,room_senter_y)
            points.append([room_senter_x,room_senter_y])

        # create a pathway from point a to point b
        for n in range(len(points)-1):
            self.makeRoomPath(points[n],points[n+1])
            # print (points[n],points[n+1])

    def printMap(self):

        self.makeRooms()
        self.makeRoomPaths()
        print ('Map:')
        for x in range(self.rows):
            for y in range(self.columns):
                xy = self.mapMatrix[x,y][0]
                if xy is None:
                    print (' . ',end="") # space
                elif xy == 1:
                    print (' O ',end="") # obstacle
                elif xy == 2:
                    print (' S ',end="") # start
                elif xy == 3:
                    print (' R ',end="") # route
                elif xy == 4:
                    print (' F ',end="") # finish
                else:
                    print (' X ',end="")
            print ("")
        # print("exiting on map print for debug")
        # sys.exit()

    def freeSpaces(self):
        freespace = []
        for xy in list(self.mapMatrix.keys()):
            # print (xy)
            if self.mapMatrix[xy][0] != 1:
                freespace.append(xy)
        return freespace


class Objects:
    def __init__(self):
        self.name = None
        self.location = None

    def populate_space_on_grid(self, gui, sell=None):
        if sell != None:
            self.location = sell
        else:
            self.location = random.choice(gui.myMap.mapMatrix.keys())

        self.figuresSizeX = gui.canvasWidth / gui.myMap.columns
        self.figuresSizeY = gui.canvasHeight / gui.myMap.rows
        # calculate size for the unit
        self.x0 = self.location[0] * self.figuresSizeX
        self.x1 = (1 + self.location[0]) * self.figuresSizeX
        self.y0 = self.location[1] * self.figuresSizeY
        self.y1 = (1 + self.location[1]) * self.figuresSizeY


class Loot(Objects):
    def __init__(self):
        Objects.__init__(self)
        # self.name = None
        # self.location = None
        self.all_items_dicts = merge_dicts(dItemsArmors, dItemsShields, dItemsWeaponsMele, dItemsWeaponsRanged, dItemsHealingPotions)
        # self.all_items_dicts = dItemsArmors
        self.figuresSizeX = None
        self.figuresSizeY = None
        self.x0 = None
        self.x1 = None
        self.y0 = None
        self.y1 = None


class GuiSetup(tkinter.Tk):
    def __init__(self, parent, heroName):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.heroName = heroName
        self.initialize()

    def initialize(self):
        self.grid()

        # canvas size configuration
        self.canvasWidth = 300
        self.canvasHeight = 300
        self.canvas = tkinter.Canvas(self, width=self.canvasWidth, height=self.canvasHeight, background='white')
        self.canvas.grid(row=0, column=11, rowspan=11)

        # making the map chess grid
        self.myMap = mainMap(self)
        self.myMap.makeMatrixDict()
        # create the grid
        setCanvasGrid(self, self.myMap.rows, self.myMap.columns)
        self.horizonLength = self.canvasWidth / self.myMap.columns
        self.verticalLength = self.canvasHeight / self.myMap.rows

        # pathfinder freedom configuration
        self.pathfindingMap = self.pathfindingMapGenerator()
        self.fredom_directions = 8  # number of possible directions to move on the map
        if self.fredom_directions == 4:
            self.dx = [1, 0, -1, 0]
            self.dy = [0, 1, 0, -1]
        elif self.fredom_directions == 8:
            self.dx = [1, 1, 0, -1, -1, -1, 0, 1]
            self.dy = [0, 1, 1, 1, 0, -1, -1, -1]

        mainFrame = tkinter.Frame(self, borderwidth=5, relief="sunken", width=500, height=200)
        mainFrame.grid(column=0, row=0, columnspan=10, rowspan=11, sticky=(N, S, E, W))

        self.button1 = tkinter.Button(self, text=u"run simulator", command=self.runSimulator)
        self.text_title = tkinter.Label(self, text="Battle:")
        self.text_title.grid(column=5, row=0)
        self.button1.grid(column=5, row=10, sticky=N + S + E + W)

        # ##################################################
        # window setup
        self.text_hero_name = tkinter.Label(self, text="Name:")
        self.text_hero_race = tkinter.Label(self, text="Race:")
        self.text_hero_class = tkinter.Label(self, text="Class:")
        self.text_hero_Str = tkinter.Label(self, text="Str:")
        self.text_hero_Dex = tkinter.Label(self, text="Dex:")
        self.text_hero_Con = tkinter.Label(self, text="Con:")
        self.text_hero_Int = tkinter.Label(self, text="Int:")
        self.text_hero_Wis = tkinter.Label(self, text="Wis:")
        self.text_hero_Cha = tkinter.Label(self, text="Cha:")

        self.text_hero_name_V = tkinter.Label(self)
        self.text_hero_race_V = tkinter.Label(self)
        self.text_hero_class_V = tkinter.Label(self)
        self.text_hero_Str_V = tkinter.Label(self)
        self.text_hero_Dex_V = tkinter.Label(self)
        self.text_hero_Con_V = tkinter.Label(self)
        self.text_hero_Int_V = tkinter.Label(self)
        self.text_hero_Wis_V = tkinter.Label(self)
        self.text_hero_Cha_V = tkinter.Label(self)

        self.text_hero_HitPoints = tkinter.Label(self, text="Hit Points")
        self.text_hero_HitPoints_V = tkinter.Label(self)
        self.text_hero_AC = tkinter.Label(self, text="AC")
        self.text_hero_AC_V = tkinter.Label(self)
        self.text_hero_kills = tkinter.Label(self, text="Kills")
        self.text_hero_kills_V = tkinter.Label(self)
        self.text_hero_XP = tkinter.Label(self, text="XP")
        self.text_hero_XP_V = tkinter.Label(self)

        self.text_monster_name = tkinter.Label(self, text="Name:")
        self.text_monster_race = tkinter.Label(self, text="Race:")
        self.text_monster_class = tkinter.Label(self, text="Class:")
        self.text_monster_Str = tkinter.Label(self, text="Str:")
        self.text_monster_Dex = tkinter.Label(self, text="Dex:")
        self.text_monster_Con = tkinter.Label(self, text="Con:")
        self.text_monster_Int = tkinter.Label(self, text="Int:")
        self.text_monster_Wis = tkinter.Label(self, text="Wis:")
        self.text_monster_Cha = tkinter.Label(self, text="Cha:")

        self.text_monster_name_V = tkinter.Label(self)
        self.text_monster_race_V = tkinter.Label(self)
        self.text_monster_class_V = tkinter.Label(self)
        self.text_monster_Str_V = tkinter.Label(self)
        self.text_monster_Dex_V = tkinter.Label(self)
        self.text_monster_Con_V = tkinter.Label(self)
        self.text_monster_Int_V = tkinter.Label(self)
        self.text_monster_Wis_V = tkinter.Label(self)
        self.text_monster_Cha_V = tkinter.Label(self)

        self.text_monster_HitPoints = tkinter.Label(self, text="Hit Points")
        self.text_monster_HitPoints_V = tkinter.Label(self)
        self.text_monster_AC = tkinter.Label(self, text="AC")
        self.text_monster_AC_V = tkinter.Label(self)

        # GRID
        self.text_hero_name.grid(column=1, row=1, sticky=W + E)
        self.text_hero_race.grid(column=1, row=2, sticky=W + E)
        self.text_hero_class.grid(column=1, row=3, sticky=W + E)
        self.text_hero_Str.grid(column=1, row=4, sticky=W + E)
        self.text_hero_Dex.grid(column=1, row=5, sticky=W + E)
        self.text_hero_Con.grid(column=1, row=6, sticky=W + E)
        self.text_hero_Int.grid(column=1, row=7, sticky=W + E)
        self.text_hero_Wis.grid(column=1, row=8, sticky=W + E)
        self.text_hero_Cha.grid(column=1, row=9, sticky=W + E)

        self.text_hero_name_V.grid(column=2, row=1, sticky=W + E)
        self.text_hero_race_V.grid(column=2, row=2, sticky=W + E)
        self.text_hero_class_V.grid(column=2, row=3, sticky=W + E)
        self.text_hero_Str_V.grid(column=2, row=4, sticky=W + E)
        self.text_hero_Dex_V.grid(column=2, row=5, sticky=W + E)
        self.text_hero_Con_V.grid(column=2, row=6, sticky=W + E)
        self.text_hero_Int_V.grid(column=2, row=7, sticky=W + E)
        self.text_hero_Wis_V.grid(column=2, row=8, sticky=W + E)
        self.text_hero_Cha_V.grid(column=2, row=9, sticky=W + E)

        self.text_hero_HitPoints.grid(column=3, row=2)
        self.text_hero_HitPoints_V.grid(column=3, row=3)
        self.text_hero_AC.grid(column=3, row=4)
        self.text_hero_AC_V.grid(column=3, row=5)
        self.text_hero_kills.grid(column=3, row=6)
        self.text_hero_kills_V.grid(column=3, row=7)
        self.text_hero_XP.grid(column=3, row=8)
        self.text_hero_XP_V.grid(column=3, row=9)

        self.text_monster_name.grid(column=7, row=1, sticky=W + E)
        self.text_monster_race.grid(column=7, row=2, sticky=W + E)
        self.text_monster_class.grid(column=7, row=3, sticky=W + E)
        self.text_monster_Str.grid(column=7, row=4, sticky=W + E)
        self.text_monster_Dex.grid(column=7, row=5, sticky=W + E)
        self.text_monster_Con.grid(column=7, row=6, sticky=W + E)
        self.text_monster_Int.grid(column=7, row=7, sticky=W + E)
        self.text_monster_Wis.grid(column=7, row=8, sticky=W + E)
        self.text_monster_Cha.grid(column=7, row=9, sticky=W + E)
        self.text_monster_name_V.grid(column=8, row=1, sticky=W + E)
        self.text_monster_race_V.grid(column=8, row=2, sticky=W + E)
        self.text_monster_class_V.grid(column=8, row=3, sticky=W + E)
        self.text_monster_Str_V.grid(column=8, row=4, sticky=W + E)
        self.text_monster_Dex_V.grid(column=8, row=5, sticky=W + E)
        self.text_monster_Con_V.grid(column=8, row=6, sticky=W + E)
        self.text_monster_Int_V.grid(column=8, row=7, sticky=W + E)
        self.text_monster_Wis_V.grid(column=8, row=8, sticky=W + E)
        self.text_monster_Cha_V.grid(column=8, row=9, sticky=W + E)
        self.text_monster_HitPoints.grid(column=6, row=2)
        self.text_monster_HitPoints_V.grid(column=6, row=3)
        self.text_monster_AC.grid(column=6, row=4)
        self.text_monster_AC_V.grid(column=6, row=5)

    def runSimulator(self):
        '''
        1. two randomly generated locatios for mob and hero
        2. seeking each other
        3. when in next sells start attack rounds
        4. try to disengage when low on health
        5. death and new round , mob random location ,hero from his spot
        '''
        # for x in range(5):
        #     self.myMap.makeMatrixDict()
        #     self.myMap.printMap()
        # sys.exit()

        # generate map
        self.walls = []
        self.myMap.makeMatrixDict()
        self.myMap.makeRooms()
        self.myMap.makeRoomPaths()
        self.updateWalls()
        self.update()

        # create Hero
        self.hero = Hero(self.heroName)
        self.hero.populate_space_on_grid(self)
        # create the unit on grid
        self.heroAvatar = self.canvas.create_oval(self.hero.x0, self.hero.y0, self.hero.x1, self.hero.y1, fill="blue")
        self.update()

        # self.walls = []
        # self.walls = self.generateWalls()


        self.lootList = []
        for x in range(5):
            self.lootList.append(self.createLoot())

        # start battle
        while self.hero.alive:
            self.gui_dBattle2()

        # clear the board
        self.canvas.delete(self.heroAvatar)
        # looks ugly need to change and make it support more loot.
        # if self.loot.name is not None:
        #     self.removeLoot(self.loot)
        if self.lootList:
            for loot in self.lootList:
                # loot = None
                self.removeLoot(loot)

        self.removeWalls()
        # if self.walls:
        #     for wall in self.walls:
        #         # loot = None
        #         self.removeWall(wall)
        self.update()

    def gui_dBattle2(self):
        monster = Mob()
        monster.populate_space_on_grid(self)

        # create the monster unit on grid
        self.monsterAvatar = self.canvas.create_oval(monster.x0, monster.y0, monster.x1, monster.y1, fill="red")
        self.updateGameInfo(self.hero, monster)
        self.update()
        sleep(1)

        turn = self.check_initiative(self.hero, monster)

        while True:
            if turn:
                sleep(0.2)
                heroAction = self.selectAction(self.hero, monster)
                # print "hero action: ", heroAction
                self.doAction(heroAction, self.hero, self.heroAvatar, monster)
                turn = False

            else:
                sleep(0.2)
                monsterAction = self.selectAction(monster, self.hero)
                # print "monster action: ", monsterAction
                self.doAction(monsterAction, monster, self.monsterAvatar, self.hero)
                turn = True

            self.updateGameInfo(self.hero, monster)
            self.hero.dCheckStatus()
            monster.dCheckStatus()
            self.update()

            if not monster.alive or not self.hero.alive:
                self.canvas.delete(self.monsterAvatar)
                self.update()
                if self.hero.alive:
                    self.hero.XP += monster.XpReword
                    self.hero.kills += 1
                    self.hero.dCheckStatus()
                break

    def selectAction(self, myself, enemy):
        hunt = 0
        attack = 0
        heal = 0
        getLoot = 0
        lootExist = False
        lootPathList = []
        walk_path_loot = 0
        pick_up_loot = 0

        walk_path = self.pathFindStep(myself, enemy)

        if self.lootList:
            lootExist = True
            for loot in self.lootList:
                print (loot.name,)
                path = self.pathFindStep(myself, loot)
                lootPathList.append([path, len(path)])
            walk_path_loot = min(lootPathList, key=lambda t: t[1])[0]

        # if myself.canLoot:
        #     print (myself.name, "AC advantage:", myself.AC - enemy.AC)
        #     print (myself.name, "HP percentage:", (100.0 / myself.MaxHP) * myself.HitPoints)

        if len(walk_path) > 1:
            hunt = 1

        if len(walk_path) <= 1:
            attack = 2

        if myself.HitPoints / float(myself.MaxHP) <= 0.35 and myself.canHeal and myself.HitDiceCount > 0:
            heal = 3

        if myself.canLoot and lootExist and len(walk_path_loot) > 1:
            getLoot = 4

        if lootExist and len(walk_path_loot) <= 1 and myself.canLoot:
            pick_up_loot = 5

        # if not None in self.myMap.mapMatrix.values():
        #     print self.myMap.mapMatrix.values()

        actionSelection = [hunt, attack, heal, getLoot, pick_up_loot]
        return max(actionSelection)

    def doAction(self, action, myself, avatar, enemy):
        # hunt
        if action == 1:  # walk to enemy
            RouteStep = int(self.pathFindStep(myself, enemy)[0])
            self.canvas.move(avatar, self.dx[RouteStep] * self.horizonLength, self.dy[RouteStep] * self.verticalLength)
            self.myMap.mapMatrix[myself.location][0] = None
            myself.location = (myself.location[0] + self.dx[RouteStep], myself.location[1] + self.dy[RouteStep])
            self.myMap.mapMatrix[myself.location][0] = myself
            self.update()

        if action == 2:  # attack closest enemy
            self.gui_dAttack2(myself, enemy)

        if action == 3:  # heal self
            myself.heal()

        if action == 4:  # walk to loot
            lootPathList = []
            for loot in self.lootList:
                path = self.pathFindStep(myself, loot)
                lootPathList.append([path, len(path)])
            # walk_path_loot = min(lootPathList, key = lambda t: t[1])[0]
            RouteStep = int(min(lootPathList, key=lambda t: t[1])[0][0])
            # RouteStep = int(self.pathFindStep(myself, self.loot)[0])
            self.canvas.move(avatar, self.dx[RouteStep] * self.horizonLength, self.dy[RouteStep] * self.verticalLength)
            self.myMap.mapMatrix[myself.location][0] = None
            myself.location = (myself.location[0] + self.dx[RouteStep], myself.location[1] + self.dy[RouteStep])
            self.myMap.mapMatrix[myself.location][0] = myself
            self.update()

        if action == 5:  # pickup loot
            for loot in self.lootList:
                path = self.pathFindStep(myself, loot)
                if len(path) <= 1:
                    myself.inventory.append(loot.name)
                    myself.updateEquipment()
                    # myself.armor = loot.name
                    # myself.calcAC()
                    self.removeLoot(loot)
                    self.lootList.remove(loot)
                    self.update()

    def check_initiative(self, hero, monster):
        hero_initiative = dScoreModifier[hero.dDex]
        monster_initiative = dScoreModifier[monster.dDex]
        if hero_initiative >= monster_initiative:
            return True
        return False

    def gui_dAttack2(self, attacker, attacked):
        diceRoll = randGen(1, 20)
        if diceRoll == 1:
            return
        elif diceRoll == 20:
            attacked.HitPoints -= self.demageCalc(attacker) + self.demageCalc(attacker)
        else:
            if diceRoll + dScoreModifier[attacker.dStr] > attacked.AC:
                attacked.HitPoints -= self.demageCalc(attacker)

    def demageCalc(self, attacker):
        # melee attack

        x = fullDiceRoll(attacker.weapon) + dScoreModifier[attacker.dStr]
        if x < 0:
            return 0
        return x

        # ranged attack not implemented
        return randGen(dItemsWeaponsRanged.get(attacker.weapon)[0], dItemsWeaponsRanged.get(attacker.weapon)[1]) + \
               dScoreModifier[attacker.dDex]

    def updateGameInfo(self, hero, monster):
        self.text_hero_name_V.config(text=hero.name +" (lvl "+str(hero.lvl)+")")
        self.text_hero_race_V.config(text=hero.dRaceName)
        self.text_hero_class_V.config(text=hero.dClass)
        self.text_hero_Str_V.config(text=hero.dStr)
        self.text_hero_Dex_V.config(text=hero.dDex)
        self.text_hero_Con_V.config(text=hero.dCons)
        self.text_hero_Int_V.config(text=hero.dInt)
        self.text_hero_Wis_V.config(text=hero.dWis)
        self.text_hero_Cha_V.config(text=hero.dCha)
        self.text_hero_HitPoints_V.config(text=str(hero.HitPoints)+" ("+str(hero.MaxHP)+")")
        self.text_hero_AC_V.config(text=hero.AC)
        self.text_hero_kills_V.config(text=hero.kills)
        self.text_hero_XP_V.config(text=str(hero.XP)+" ("+str(dXPlevelUP[hero.lvl + 1][0])+")")

        self.text_monster_name_V.config(text=monster.name)
        self.text_monster_race_V.config(text=monster.dRaceName)
        self.text_monster_class_V.config(text=monster.dClass)
        self.text_monster_Str_V.config(text=monster.dStr)
        self.text_monster_Dex_V.config(text=monster.dDex)
        self.text_monster_Con_V.config(text=monster.dCons)
        self.text_monster_Int_V.config(text=monster.dInt)
        self.text_monster_Wis_V.config(text=monster.dWis)
        self.text_monster_Cha_V.config(text=monster.dCha)
        self.text_monster_HitPoints_V.config(text=str(monster.HitPoints)+" ("+str(monster.MaxHP)+")")
        self.text_monster_AC_V.config(text=monster.AC)

    def pathfindingMapGenerator(self):
        the_map = []
        row = [0] * self.myMap.columns
        for i in range(self.myMap.rows):
            the_map.append(list(row))
        return the_map

    def updateMap(self):
        # for x in range(self.myMap.rows):
        #     for y in range(self.myMap.columns):
        #         xy = self.myMap.mapMatrix[x,y][0]
        #         # print (xy)
        #         if xy is 1:
        #             self.pathfindingMap[x][y] = 1
        for xy in self.walls:
            # print (xy.location[1],xy.location[0])
            self.pathfindingMap[xy.location[1]][xy.location[0]] = 1

    def pathFindStep(self, startObject, endObject):
        self.updateMap()
        return pathFind(self.pathfindingMap, self.fredom_directions, self.dx, self.dy, startObject.location[0],
                        startObject.location[1], endObject.location[0], endObject.location[1], self.myMap.columns,
                        self.myMap.rows)

    def createLoot(self):
        # create loot
        loot = Loot()
        loot.name = random.choice(list(loot.all_items_dicts.keys()))
        loot.location = random.choice(list(self.myMap.freeSpaces()))
        self.myMap.mapMatrix[loot.location][1] = loot.name
        loot.populate_space_on_grid(self, loot.location)
        loot.lootAvatar = self.canvas.create_oval(loot.x0, loot.y0, loot.x1, loot.y1, fill="yellow")
        return loot

    def removeLoot(self, loot):
        self.myMap.mapMatrix[loot.location] = [None, None]
        self.canvas.delete(loot.lootAvatar)
        loot = None
        # loot.location = None
        # loot.name = None

    def updateWalls(self):
        for x in range(self.myMap.rows):
            for y in range(self.myMap.columns):
                if self.myMap.mapMatrix[x,y][0]==1:
                    self.walls.append(self.generateWall(x,y))

    def generateWall(self,x,y):
        wall = Objects()
        wall.name = "wall"
        wall.location = [x,y]
        wall.populate_space_on_grid(self,wall.location)
        wall.wallAvatar = self.canvas.create_rectangle(wall.x0, wall.y0, wall.x1, wall.y1, fill="black")
        return wall

    def removeWalls(self):
        for wall in self.walls:
            self.myMap.mapMatrix[wall.location] = [None, None]
            self.canvas.delete(wall.lootAvatar)
            loot = None

    ################ not in use ####################
    def move_N(self, unit):
        self.canvas.move(unit, 0, -1 * self.verticalLength)

    def move_NE(self, unit):
        self.canvas.move(unit, self.horizonLength, -1 * self.verticalLength)

    def move_E(self, unit):
        self.canvas.move(unit, self.horizonLength, 0)

    def move_SE(self, unit):
        self.canvas.move(unit, self.horizonLength, self.verticalLength)

    def move_S(self, unit):
        self.canvas.move(unit, 0, self.verticalLength)

    def move_SW(self, unit):
        self.canvas.move(unit, -1 * self.horizonLength, self.verticalLength)

    def move_W(self, unit):
        self.canvas.move(unit, -1 * self.horizonLength, 0)

    def move_NW(self, unit):
        self.canvas.move(unit, -1 * self.horizonLength, -1 * self.verticalLength)

    def canvas_lgoic(self):
        # print self.myMap.mapMatrix

        # dimentions of the player or mob in the grid
        figuresSizeX = self.canvasWidth / self.myMap.columns
        figuresSizeY = self.canvasHeight / self.myMap.rows

        # generation of the start and the finish sells path of the unit
        location = random.choice(self.myMap.mapMatrix.keys())
        endLocation = random.choice(self.myMap.mapMatrix.keys())

        # calculate size for the unit
        x0 = location[0] * figuresSizeX
        x1 = (1 + location[0]) * figuresSizeX
        y0 = location[1] * figuresSizeY
        y1 = (1 + location[1]) * figuresSizeY

        # create the unit
        figure1 = self.canvas.create_oval(x0, y0, x1, y1, fill="blue")
        self.update()

        # for pathfinding start x0,y0 and end of path x1 y1
        xA = location[0]
        xB = endLocation[0]
        yA = location[1]
        yB = endLocation[1]

        # use A*star algorithm to find the path from start to end
        route = pathFind(self.pathfindingMap, self.fredom_directions, self.dx, self.dy, xA, yA, xB, yB,
                         self.myMap.columns, self.myMap.rows)
        print (route)

        # move the unit all the way from start location to finish location
        for i in route:
            sleep(0.1)
            self.canvas.move(figure1, self.dx[int(i)] * self.horizonLength, self.dy[int(i)] * self.verticalLength)
            self.update()

        # terminate the unit from memory and the board
        self.canvas.delete(figure1)


class Unit:
    def __init__(self, name):
        # charecter configuration
        self.name = name
        self.alive = True
        self.action = None
        self.XP = 0
        self.lvl = 1
        ############################
        self.dRaceName = random.choice(list(dRacess.keys()))
        self.dRace = dRacess[self.dRaceName]
        self.dStr = abilityGen(4) + self.dRace[2][0]
        self.dDex = abilityGen(4) + self.dRace[2][1]
        self.dCons = abilityGen(4) + self.dRace[2][2]
        self.dInt = abilityGen(4) + self.dRace[2][3]
        self.dWis = abilityGen(4) + self.dRace[2][4]
        self.dCha = abilityGen(4) + self.dRace[2][5]
        self.dClass = random.choice(list(dClasses.keys()))
        self.HitDice = dClasses.get(self.dClass)
        self.HitDiceCount = 1
        self.HitPoints = self.HitDice + dScoreModifier[self.dCons]
        self.MaxHP = copy.deepcopy(self.HitPoints)
        self.armor = None
        self.shieldName = 'No Sheild'
        self.AC = 10
        self.weaponName = None
        self.weapon = None
        self.XpReword = 300
        self.inventory = []

    def populate_space_on_grid(self, gui, sell=None):
        if sell != None:
            self.location = sell
        else:
            # self.location = random.choice(list(gui.myMap.mapMatrix.keys()))
            print (random.choice(list(gui.myMap.mapMatrix.keys())))
            print (random.choice(list(gui.myMap.freeSpaces())))
            self.location = random.choice(list(gui.myMap.freeSpaces()))

        self.figuresSizeX = gui.canvasWidth / gui.myMap.columns
        self.figuresSizeY = gui.canvasHeight / gui.myMap.rows
        # calculate size for the unit
        self.x0 = self.location[0] * self.figuresSizeX
        self.x1 = (1 + self.location[0]) * self.figuresSizeX
        self.y0 = self.location[1] * self.figuresSizeY
        self.y1 = (1 + self.location[1]) * self.figuresSizeY

    def dmgCalc(self):
        dmg = int(self.Str / 4)
        if dmg < 1:
            dmg = 1
        return dmg

    def calcAC(self):
        AC = 10
        if self.armor != None:
            AC = dItemsArmors.get(self.armor)[0]
        newAC = AC + int(dItemsShields.get(self.shieldName)[0]) + dScoreModifier[self.dDex]
        self.AC = newAC

    def dCheckStatus(self):
        if self.HitPoints > 0:
            self.alive = True
        else:
            self.alive = False
        if self.XP >= dXPlevelUP[self.lvl + 1][0]:
            self.levelUP()

    def levelUP(self):
        self.lvl += 1
        self.HitDiceCount += 1
        addHP = randGen(1, self.HitDice) + dScoreModifier[self.dCons]
        if addHP < 1:
            addHP = 1
        self.MaxHP += addHP
        self.HitPoints = copy.deepcopy(self.MaxHP)

    def heal(self):
        self.HitPoints += randGen(1, self.HitDice)
        if self.HitPoints > self.MaxHP:
            self.HitPoints = copy.deepcopy(self.MaxHP)
        self.HitDiceCount -= 1

    def updateEquipment(self):
        bestMeleeWeapon = self.weaponName
        bestRangedWeapon = 0
        bestAromr = 'No Armor'
        bestShield = 'No Sheild'
        # print self.armor,",",self.weaponName,",",self.shieldName
        for item in self.inventory:
            if item in dItemsArmors:
                if dItemsArmors[item][0] > dItemsArmors[bestAromr][0]:
                    bestAromr = item

            if item in dItemsShields:
                if dItemsShields[item][0] > dItemsShields[bestShield][0]:
                    bestShield = item

            if item in dItemsWeaponsMele:
                newWeapon = eval(dItemsWeaponsMele[item].replace('d', '*'))
                oldWeapon = eval(dItemsWeaponsMele[bestMeleeWeapon].replace('d', '*'))
                if newWeapon > oldWeapon:
                    bestMeleeWeapon = item

        self.armor = bestAromr
        self.shieldName = bestShield
        self.weaponName = bestMeleeWeapon
        # print self.armor,",",self.weaponName,",",self.shieldName
        self.calcAC()


class Hero(Unit):
    def __init__(self, name):
        Unit.__init__(self, name)
        self.kills = 0
        self.canHeal = True
        self.canLoot = True
        self.weaponName = random.choice(list(dItemsWeaponsMele.keys()))
        self.weapon = dItemsWeaponsMele[self.weaponName]
        self.calcAC()


class Mob(Unit):
    def __init__(self):
        Unit.__init__(self, "")

        self.name = random.choice(challenge_0)
        # self.name = random.choice(random.choice(challenge_all))
        mobParams = MD.monsterDict[self.name]
        self.dRaceName = "monster"
        self.dRace = "monster"
        self.dClass = "monster"
        self.dStr = mobParams[5][0]
        self.dDex = mobParams[5][1]
        self.dCons = mobParams[5][2]
        self.dInt = mobParams[5][3]
        self.dWis = mobParams[5][4]
        self.dCha = mobParams[5][5]
        # self.dClass 	= random.choice(dClasses.keys())
        # self.HitDice 	= mobParams[]
        # self.HitDiceCount = 1
        # self.HitPoints 	= self.HitDice + dScoreModifier[self.dCons]
        self.HitPoints = self.calcHP(mobParams[3])
        self.MaxHP = copy.deepcopy(self.HitPoints)
        self.armor = None
        self.shield = 0
        self.AC = int(mobParams[2])
        # self.weapon		= random.choice(dItemsWeaponsMele.keys())
        self.weapon = mobParams[7]
        self.XpReword = int(mobParams[9])
        self.canHeal = False
        self.canLoot = False

    def calcHP(self, x):
        x = x.split()
        result = diceRoll(x[0])
        if len(x) > 1:
            stringa = "%s%s%s" % (result, x[1], x[2])
            result = eval(stringa)
        if result <= 0:
            result = 1
        return result


def fullDiceRoll(x):
    x = x.split()
    result = diceRoll(x[0])
    if len(x) > 1:
        stringa = "%s%s%s" % (result, x[1], x[2])
        result = eval(stringa)
    if result <= 0:
        result = 1
    # print "dmg type:",x,result
    return result


def diceRoll(dice):
    x = dice.split("d")
    result = 0
    for times in range(int(x[0])):
        result += randGen(1, int(x[1]))
    return result


def randGen(startNum, endNum):
    return random.randint(startNum, endNum)


def mobNameGen():
    print (random.choice(random.choice(challenge_all)))

    return random.choice(dListOfNamesD.keys())


def abilityGen(numOfRolls):
    rollsList = []
    for x in range(numOfRolls):
        rollsList.append(randGen(1, 6))

    return sum(sorted(rollsList)[1:])


def setCanvasGrid(canv, rows, columns):
    for line in range(rows):
        x = line * (canv.canvasWidth / rows)
        canv.canvas.create_line(x, 0, x, canv.canvasHeight, fill="black")
    for line in range(columns):
        y = line * (canv.canvasWidth / columns)
        canv.canvas.create_line(0, y, canv.canvasWidth, y, fill="black")


def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def gui_test():
    app = GuiSetup(None, "mafrum")
    app.title("test")
    app.mainloop()


def parse_monster_list():
    import re
    # fileList = open("monster list.txt","r").readlines()
    fileList = open("Nonplayer Characters example.txt", "r").readlines()
    # dummyFile = open("temp.txt","w")
    textList = []
    sets = []
    x = []
    for line in fileList:
        if line == '\n':
            sets.append(x)
            x = []
            continue
        x.append(line.strip())

    for set in sets:
        if set == []:
            continue
        name, size, alighment, AC, HP, speed, params, hardDmg, calcDmg, challenge, XP = "", "", "", "", "", "", "", "", "", "", ""

        # print "\n"

        # print set

        # print set[0] 	# name
        name = set[0]  # name

        # print set[1] 	# size , alighment
        size = set[1].split(",")[0].split(" ")[0]  # size , alighment
        alighment = set[1].split(",")[1].strip()  # size , alighment

        # print set[2]	# armor class
        AC = set[2].split(" ")[2]  # armor class

        # print set[3].split("(")[1].split(")")[0]	# hit points
        HP = set[3].split("(")[1].split(")")[0]  # hit points

        # print set[4]	# speed
        speed = set[4].split(" ")[1]  # speed

        # print set[5]	# "STR DEX CON INT WIS CHA"

        # print map(int,set[6].split()[0::2])	# STR DEX CON INT WIS CHA
        params = map(int, set[6].split()[0::2])  # STR DEX CON INT WIS CHA

        for line in set:
            if "Challenge" in line:
                # print line
                challenge = line.split(" ")[1]
                XP = line.split("(")[1].split(" XP")[0]
            if "Hit:" in line:
                p1 = re.compile(r"[\:]\s\d+")
                p2 = re.compile(r"\d+[d]\d+\s.\s\d+|\d+[d]\d+")
                # p3 = re.compile(r"\d+[d]\d+^\s")
                try:
                    # print p1.search(str(line)).group().split(": ")[1]
                    hardDmg = p1.search(str(line)).group().split(": ")[1]
                except:
                    pass
                try:
                    # print p2.search(str(line)).group()
                    calcDmg = p2.search(str(line)).group()
                except:
                    pass

        # print ("'"+%s+"'"+":"+ %s + %s + %s + %s + %s + %s + %s)%name,size_alighment,AC,HP,speed,params,hardDmg,calcDmg
        print ("'%s':( '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' ),") % (
            name, size, alighment, AC, HP, speed, params, hardDmg, calcDmg, challenge, XP)


def monster_generator_test():
    mob = Mob()


if (__name__ == "__main__"):
    gui_test()

    # main(sys.argv[1])
    # parse_monster_list()

    # monster_generator_test()
