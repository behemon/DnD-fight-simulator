########
#   http://www.wikihow.com/Create-a-Dungeons-and-Dragons-Character
#   https://docs.google.com/spreadsheets/d/1fjnoCiYUCOcrMxffWNwppHfuUDlY1Ae0HQ4t-XCaiPA/edit#gid=0
#   https://drive.google.com/file/d/0B8mF8uNMRN_mLUJRNmkwaDB3R3M/view
#   https://www.dandwiki.com/wiki/5e_Weapons
#   https://stackoverflow.com/questions/20149483/python-canvas-and-grid-tkinter
#   http://media.wizards.com/2016/downloads/DND/DMBasicRulesV05.pdf
########
import random
import sys
import copy
from time import sleep
import Tkinter
from Tkinter import N,S,E,W
from A_star_algorithm import pathFind

# import canvas_test as maps
from dictionaries import *
import monster_dictionary as MD

class mainMap():
    def __init__(self,gui):
        self.columns = 10
        self.rows = 10
        self.mapMatrix = {}
        self.makeMatrixDict()

    def makeMatrixDict(self):
        for x in range(self.columns):
            for y in range(self.rows):
                self.mapMatrix[y,x]=[None, None]


class Loot():
    def __init__(self):
        self.name = None
        self.location = None
        # self.all_items_dicts = merge_dicts(dItemsArmors, dItemsShields, dItemsWeaponsMele, dItemsWeaponsRanged)
        self.all_items_dicts = dItemsArmors
        self.figuresSizeX = None
        self.figuresSizeY = None
        self.x0 = None
        self.x1 = None
        self.y0 = None
        self.y1 = None


    def populate_space_on_grid(self, gui, sell = None ):
        if sell != None:
            self.location = sell
        else:
            self.location = random.choice(gui.myMap.mapMatrix.keys())

        self.figuresSizeX = gui.canvasWidth/gui.myMap.columns
        self.figuresSizeY = gui.canvasHeight/gui.myMap.rows
        #calculate size for the unit
        self.x0 = self.location[0]*self.figuresSizeX
        self.x1 = (1+self.location[0])*self.figuresSizeX
        self.y0 = self.location[1]*self.figuresSizeY
        self.y1 = (1+self.location[1])*self.figuresSizeY


class GuiSetup(Tkinter.Tk):
    def __init__(self,parent,heroName):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.heroName = heroName
        self.initialize()

    def initialize(self):
        self.grid()

        # canvas size configuration
        self.canvasWidth = 300
        self.canvasHeight = 300
        self.canvas=Tkinter.Canvas(self, width=self.canvasWidth, height=self.canvasHeight, background='white')
        self.canvas.grid(row=0,column=11,rowspan=11)

        # making the map chess grid
        self.myMap = mainMap(self)
        # grid X*Y configuration
        self.myMap.rows = 20
        self.myMap.columns = 20
        self.myMap.makeMatrixDict()
        # create the grid
        setCanvasGrid(self,self.myMap.rows,self.myMap.columns)
        self.horizonLength = self.canvasWidth / self.myMap.columns
        self.verticalLength = self.canvasHeight / self.myMap.rows

        # pathfinder freedom configuration
        self.pathfindingMap = self.pathfindingMapGenerator()
        self.fredom_directions = 8 # number of possible directions to move on the map
        if self.fredom_directions == 4:
            self.dx = [1, 0, -1, 0]
            self.dy = [0, 1, 0, -1]
        elif self.fredom_directions == 8:
            self.dx = [1, 1, 0, -1, -1, -1,  0,  1]
            self.dy = [0, 1, 1,  1,  0, -1, -1, -1]


        mainFrame = Tkinter.Frame(self, borderwidth=5, relief="sunken", width=500, height=200)
        mainFrame.grid(column=0, row=0, columnspan=10, rowspan=11, sticky=(N, S, E, W))


        self.button1 = Tkinter.Button(self,text=u"run simulator",command=self.runSimulator)
        self.text_title = Tkinter.Label(self,text="Battle:")
        self.text_title.grid(	column=5,row=0)
        self.button1.grid(		column=5,row=10,sticky=N+S+E+W)


        # ##################################################
        # window setup
        self.text_hero_name			= Tkinter.Label(self, text="Name:")
        self.text_hero_race			= Tkinter.Label(self, text="Race:")
        self.text_hero_class		= Tkinter.Label(self, text="Class:")
        self.text_hero_Str			= Tkinter.Label(self, text="Str:")
        self.text_hero_Dex			= Tkinter.Label(self, text="Dex:")
        self.text_hero_Con			= Tkinter.Label(self, text="Con:")
        self.text_hero_Int			= Tkinter.Label(self, text="Int:")
        self.text_hero_Wis			= Tkinter.Label(self, text="Wis:")
        self.text_hero_Cha			= Tkinter.Label(self, text="Cha:")

        self.text_hero_name_V		= Tkinter.Label(self)
        self.text_hero_race_V		= Tkinter.Label(self)
        self.text_hero_class_V		= Tkinter.Label(self)
        self.text_hero_Str_V		= Tkinter.Label(self)
        self.text_hero_Dex_V		= Tkinter.Label(self)
        self.text_hero_Con_V		= Tkinter.Label(self)
        self.text_hero_Int_V		= Tkinter.Label(self)
        self.text_hero_Wis_V		= Tkinter.Label(self)
        self.text_hero_Cha_V		= Tkinter.Label(self)

        self.text_hero_HitPoints	= Tkinter.Label(self, text="Hit Points")
        self.text_hero_HitPoints_V	= Tkinter.Label(self)
        self.text_hero_AC			= Tkinter.Label(self, text="AC")
        self.text_hero_AC_V			= Tkinter.Label(self)
        self.text_hero_kills		= Tkinter.Label(self, text="Kills")
        self.text_hero_kills_V		= Tkinter.Label(self)
        self.text_hero_XP			= Tkinter.Label(self,  text="XP")
        self.text_hero_XP_V			= Tkinter.Label(self)

        self.text_monster_name		= Tkinter.Label(self, text="Name:")
        self.text_monster_race		= Tkinter.Label(self, text="Race:")
        self.text_monster_class		= Tkinter.Label(self, text="Class:")
        self.text_monster_Str		= Tkinter.Label(self, text="Str:")
        self.text_monster_Dex		= Tkinter.Label(self, text="Dex:")
        self.text_monster_Con		= Tkinter.Label(self, text="Con:")
        self.text_monster_Int		= Tkinter.Label(self, text="Int:")
        self.text_monster_Wis		= Tkinter.Label(self, text="Wis:")
        self.text_monster_Cha		= Tkinter.Label(self, text="Cha:")

        self.text_monster_name_V	= Tkinter.Label(self)
        self.text_monster_race_V	= Tkinter.Label(self)
        self.text_monster_class_V	= Tkinter.Label(self)
        self.text_monster_Str_V		= Tkinter.Label(self)
        self.text_monster_Dex_V		= Tkinter.Label(self)
        self.text_monster_Con_V		= Tkinter.Label(self)
        self.text_monster_Int_V		= Tkinter.Label(self)
        self.text_monster_Wis_V		= Tkinter.Label(self)
        self.text_monster_Cha_V		= Tkinter.Label(self)

        self.text_monster_HitPoints	= Tkinter.Label(self, text="Hit Points")
        self.text_monster_HitPoints_V	= Tkinter.Label(self)
        self.text_monster_AC		= Tkinter.Label(self, text="AC")
        self.text_monster_AC_V		= Tkinter.Label(self)


        # GRID
        self.text_hero_name.grid(			column=1, row=1, sticky=W+E)
        self.text_hero_race.grid(			column=1, row=2, sticky=W+E)
        self.text_hero_class.grid(			column=1, row=3, sticky=W+E)
        self.text_hero_Str.grid(			column=1, row=4, sticky=W+E)
        self.text_hero_Dex.grid(			column=1, row=5, sticky=W+E)
        self.text_hero_Con.grid(			column=1, row=6, sticky=W+E)
        self.text_hero_Int.grid(			column=1, row=7, sticky=W+E)
        self.text_hero_Wis.grid(			column=1, row=8, sticky=W+E)
        self.text_hero_Cha.grid(			column=1, row=9, sticky=W+E)

        self.text_hero_name_V.grid(			column=2, row=1, sticky=W+E)
        self.text_hero_race_V.grid(			column=2, row=2, sticky=W+E)
        self.text_hero_class_V.grid(		column=2, row=3, sticky=W+E)
        self.text_hero_Str_V.grid(			column=2, row=4, sticky=W+E)
        self.text_hero_Dex_V.grid(			column=2, row=5, sticky=W+E)
        self.text_hero_Con_V.grid(			column=2, row=6, sticky=W+E)
        self.text_hero_Int_V.grid(			column=2, row=7, sticky=W+E)
        self.text_hero_Wis_V.grid(			column=2, row=8, sticky=W+E)
        self.text_hero_Cha_V.grid(			column=2, row=9, sticky=W+E)

        self.text_hero_HitPoints.grid(		column=3, row=2)
        self.text_hero_HitPoints_V.grid(	column=3, row=3)
        self.text_hero_AC.grid(				column=3, row=4)
        self.text_hero_AC_V.grid(			column=3, row=5)
        self.text_hero_kills.grid(			column=3, row=6)
        self.text_hero_kills_V.grid(		column=3, row=7)
        self.text_hero_XP.grid(				column=3, row=8)
        self.text_hero_XP_V.grid(			column=3, row=9)

        self.text_monster_name.grid(		column=7, row=1, sticky=W+E)
        self.text_monster_race.grid(		column=7, row=2, sticky=W+E)
        self.text_monster_class.grid(		column=7, row=3, sticky=W+E)
        self.text_monster_Str.grid(			column=7, row=4, sticky=W+E)
        self.text_monster_Dex.grid(			column=7, row=5, sticky=W+E)
        self.text_monster_Con.grid(			column=7, row=6, sticky=W+E)
        self.text_monster_Int.grid(			column=7, row=7, sticky=W+E)
        self.text_monster_Wis.grid(			column=7, row=8, sticky=W+E)
        self.text_monster_Cha.grid(			column=7, row=9, sticky=W+E)
        self.text_monster_name_V.grid(		column=8, row=1, sticky=W+E)
        self.text_monster_race_V.grid(		column=8, row=2, sticky=W+E)
        self.text_monster_class_V.grid(		column=8, row=3, sticky=W+E)
        self.text_monster_Str_V.grid(		column=8, row=4, sticky=W+E)
        self.text_monster_Dex_V.grid(		column=8, row=5, sticky=W+E)
        self.text_monster_Con_V.grid(		column=8, row=6, sticky=W+E)
        self.text_monster_Int_V.grid(		column=8, row=7, sticky=W+E)
        self.text_monster_Wis_V.grid(		column=8, row=8, sticky=W+E)
        self.text_monster_Cha_V.grid(		column=8, row=9, sticky=W+E)
        self.text_monster_HitPoints.grid(	column=6, row=2)
        self.text_monster_HitPoints_V.grid(	column=6, row=3)
        self.text_monster_AC.grid(			column=6, row=4)
        self.text_monster_AC_V.grid(		column=6, row=5)

    def runSimulator(self):
        '''
        1. two randomly generated locatios for mob and hero
        2. seeking each other
        3. when in next sells start attack rounds
        4. try to disengage when low on health
        5. death and new round , mob random location ,hero from his spot
        '''
        # create Hero
        self.hero = Hero(self.heroName)
        self.hero.populate_space_on_grid(self)
        # create the unit on grid
        self.heroAvatar=self.canvas.create_oval(self.hero.x0, self.hero.y0, self.hero.x1, self.hero.y1, fill="blue")
        self.update()

        # create loot
        self.loot = Loot()
        self.loot.name = random.choice(self.loot.all_items_dicts.keys())
        self.loot.location = random.choice(self.myMap.mapMatrix.keys())
        self.myMap.mapMatrix[self.loot.location][1] = self.loot.name

        self.loot.populate_space_on_grid(self, self.loot.location)
        self.lootAvatar = self.canvas.create_oval(self.loot.x0, self.loot.y0, self.loot.x1, self.loot.y1, fill="yellow")

        # start battle
        while self.hero.alive:
            self.gui_dBattle2()

        # clear the board
        self.canvas.delete(self.heroAvatar)
        self.update()

    def gui_dBattle2(self):
        monster = Mob()
        monster.populate_space_on_grid(self)

        # create the monster unit on grid
        self.monsterAvatar=self.canvas.create_oval(monster.x0, monster.y0, monster.x1, monster.y1, fill="red")
        self.updateGameInfo(self.hero,monster)
        self.update()
        sleep(1)

        turn = self.check_initiative(self.hero,monster)

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
        walk_path_loot = 0
        pick_up_loot = 0

        walk_path = self.pathFindStep(myself, enemy)

        for key, value in self.myMap.mapMatrix.items():
            if value[1] != None:
                # print(key, value)
                lootExist = True
                walk_path_loot = self.pathFindStep(myself, self.loot)

        if len(walk_path) > 1 :
            hunt = 1

        if len(walk_path) <= 1 :
            attack = 2

        if myself.HitPoints/float(myself.MaxHP) <= 0.3 and myself.canHeal and myself.HitDiceCount > 0:
            heal = 3

        if myself.canLoot and lootExist and len(walk_path_loot) > 1:
            getLoot = 4

        if lootExist and len(walk_path_loot) <= 1 and myself.canLoot:
            pick_up_loot = 5

        # if not None in self.myMap.mapMatrix.values():
        #     print self.myMap.mapMatrix.values()

        actionSelection = [hunt, attack, heal,getLoot,pick_up_loot]
        # print actionSelection
        return max(actionSelection)

    def doAction(self, action, myself, avatar, enemy):
        # hunt
        if action == 1:
            RouteStep = int(self.pathFindStep(myself, enemy)[0])
            self.canvas.move(avatar, self.dx[RouteStep]*self.horizonLength, self.dy[RouteStep]*self.verticalLength )
            self.myMap.mapMatrix[myself.location][0] = None
            myself.location = ( myself.location[0] + self.dx[RouteStep] ,  myself.location[1] + self.dy[RouteStep] )
            self.myMap.mapMatrix[ myself.location ][0]= myself
            self.update()

        if action == 2:
            self.gui_dAttack2(myself,enemy)

        if action == 3:
            myself.heal()

        if action == 4:
            RouteStep = int(self.pathFindStep(myself, self.loot)[0])
            self.canvas.move(avatar, self.dx[RouteStep]*self.horizonLength, self.dy[RouteStep]*self.verticalLength )
            self.myMap.mapMatrix[myself.location][0] = None
            myself.location = ( myself.location[0] + self.dx[RouteStep] ,  myself.location[1] + self.dy[RouteStep] )
            self.myMap.mapMatrix[ myself.location ][0]= myself
            self.update()

        if action == 5:
            myself.armor = self.loot.name
            myself.calcAC()
            self.update()
            self.myMap.mapMatrix[self.loot.location] = [None,None]
            self.canvas.delete(self.lootAvatar)
            self.loot.location = None
            self.loot.name = None

    def check_initiative(self,hero,monster):
        hero_initiative = dScoreModifier[hero.dDex]
        monster_initiative = dScoreModifier[monster.dDex]
        if hero_initiative >= monster_initiative:
            return True
        return False

    def gui_dAttack2(self, attacker, attacked):
        diceRoll = randGen(1,20)
        if diceRoll == 1:
            return
        elif diceRoll == 20:
            attacked.HitPoints -= self.demageCalc(attacker)+self.demageCalc(attacker)
        else:
            if diceRoll + dScoreModifier[attacker.dStr] > attacked.AC:
                attacked.HitPoints -= self.demageCalc(attacker)

    def demageCalc(self, attacker):
        #mele attack
        x = randGen(dItemsWeaponsMele.get(attacker.weapon)[0],dItemsWeaponsMele.get(attacker.weapon)[1]) + dScoreModifier[attacker.dStr]
        if x<0:
            x= 0
        return x
        #ranged attack
        return randGen(dItemsWeaponsRanged.get(attacker.weapon)[0],dItemsWeaponsRanged.get(attacker.weapon)[1]) + dScoreModifier[attacker.dDex]

    def updateGameInfo(self, hero, monster):
        self.text_hero_name_V.config(		    text=hero.name)
        self.text_hero_race_V.config(		    text=hero.dRaceName)
        self.text_hero_class_V.config(		    text=hero.dClass)
        self.text_hero_Str_V.config(		    text=hero.dStr)
        self.text_hero_Dex_V.config(		    text=hero.dDex)
        self.text_hero_Con_V.config(		    text=hero.dCons)
        self.text_hero_Int_V.config(		    text=hero.dInt)
        self.text_hero_Wis_V.config(		    text=hero.dWis)
        self.text_hero_Cha_V.config(		    text=hero.dCha)
        self.text_hero_HitPoints_V.config(	    text=hero.HitPoints)
        self.text_hero_AC_V.config(			    text=hero.AC)
        self.text_hero_kills_V.config(		    text=hero.kills)
        self.text_hero_XP_V.config(			    text=hero.XP)

        self.text_monster_name_V.config(	    text=monster.name)
        self.text_monster_race_V.config(	    text=monster.dRaceName)
        self.text_monster_class_V.config(	    text=monster.dClass)
        self.text_monster_Str_V.config(		    text=monster.dStr)
        self.text_monster_Dex_V.config(		    text=monster.dDex)
        self.text_monster_Con_V.config(		    text=monster.dCons)
        self.text_monster_Int_V.config(		    text=monster.dInt)
        self.text_monster_Wis_V.config(		    text=monster.dWis)
        self.text_monster_Cha_V.config(		    text=monster.dCha)
        self.text_monster_HitPoints_V.config(	text=monster.HitPoints)
        self.text_monster_AC_V.config(		    text=monster.AC)

    def pathfindingMapGenerator(self):
        the_map = []
        row = [0] * self.myMap.columns
        for i in range(self.myMap.rows):
            the_map.append(list(row))
        return the_map

    def pathFindStep(self, startObject, endObject):
        return pathFind(self.pathfindingMap, self.fredom_directions, self.dx, self.dy, startObject.location[0], startObject.location[1], endObject.location[0], endObject.location[1], self.myMap.columns, self.myMap.rows)


    ################ not in use ####################
    def move_N(self,unit):
        self.canvas.move(unit,0,-1*self.verticalLength)
    def move_NE(self,unit):
        self.canvas.move(unit,self.horizonLength,-1*self.verticalLength)
    def move_E(self,unit):
        self.canvas.move(unit,self.horizonLength,0)
    def move_SE(self,unit):
        self.canvas.move(unit,self.horizonLength,self.verticalLength)
    def move_S(self,unit):
        self.canvas.move(unit,0,self.verticalLength)
    def move_SW(self,unit):
        self.canvas.move(unit,-1*self.horizonLength,self.verticalLength)
    def move_W(self,unit):
        self.canvas.move(unit,-1*self.horizonLength,0)
    def move_NW(self,unit):
        self.canvas.move(unit,-1*self.horizonLength,-1*self.verticalLength)


    def canvas_lgoic(self):
        #print self.myMap.mapMatrix

        #dimentions of the player or mob in the grid
        figuresSizeX = self.canvasWidth/self.myMap.columns
        figuresSizeY = self.canvasHeight/self.myMap.rows

        #generation of the start and the finish sells path of the unit
        location = random.choice(self.myMap.mapMatrix.keys())
        endLocation = random.choice(self.myMap.mapMatrix.keys())

        #calculate size for the unit
        x0 = location[0]*figuresSizeX
        x1 = (1+location[0])*figuresSizeX
        y0 = location[1]*figuresSizeY
        y1 = (1+location[1])*figuresSizeY

        #create the unit
        figure1=self.canvas.create_oval(x0, y0, x1, y1, fill="blue")
        self.update()

        #for pathfinding start x0,y0 and end of path x1 y1
        xA = location[0]
        xB = endLocation[0]
        yA = location[1]
        yB = endLocation[1]

        # use A*star algorithm to find the path from start to end
        route = pathFind(self.pathfindingMap, self.fredom_directions, self.dx, self.dy, xA, yA, xB, yB, self.myMap.columns, self.myMap.rows)
        print route

        #move the unit all the way from start location to finish location
        for i in route:
            sleep(0.1)
            self.canvas.move(figure1, self.dx[int(i)]*self.horizonLength, self.dy[int(i)]*self.verticalLength )
            self.update()

        #terminate the unit from memory and the board
        self.canvas.delete(figure1)


class Unit:
    def __init__(self,name):
        # charecter configuration
        self.name 	= name
        self.alive 	= True
        self.action = None
        self.XP		= 0
        self.lvl	= 1
        ############################
        self.dRaceName	= random.choice(dRacess.keys())
        self.dRace		= dRacess[self.dRaceName]
        self.dStr		= abilityGen(4) + self.dRace[2][0]
        self.dDex		= abilityGen(4) + self.dRace[2][1]
        self.dCons		= abilityGen(4) + self.dRace[2][2]
        self.dInt		= abilityGen(4) + self.dRace[2][3]
        self.dWis		= abilityGen(4) + self.dRace[2][4]
        self.dCha		= abilityGen(4) + self.dRace[2][5]
        self.dClass 	= random.choice(dClasses.keys())
        self.HitDice 	= dClasses.get(self.dClass)
        self.HitDiceCount = 1
        self.HitPoints 	= self.HitDice + dScoreModifier[self.dCons]
        self.MaxHP		= copy.deepcopy(self.HitPoints)
        self.armor		= None
        self.shield		= 0
        self.AC			= 10
        self.weapon		= random.choice(dItemsWeaponsMele.keys())
        self.XpReword	= 300
        self.inventory	= {}

    def populate_space_on_grid(self, gui, sell = None ):
        if sell != None:
            self.location = sell
        else:
            self.location = random.choice(gui.myMap.mapMatrix.keys())

        self.figuresSizeX = gui.canvasWidth/gui.myMap.columns
        self.figuresSizeY = gui.canvasHeight/gui.myMap.rows
        #calculate size for the unit
        self.x0 = self.location[0]*self.figuresSizeX
        self.x1 = (1+self.location[0])*self.figuresSizeX
        self.y0 = self.location[1]*self.figuresSizeY
        self.y1 = (1+self.location[1])*self.figuresSizeY

    def dmgCalc(self):
        dmg = int(self.Str/4)
        if dmg < 1:
            dmg = 1
        return dmg

    def calcAC(self):
        AC = 10
        if self.armor != None:
            AC = dItemsArmors.get(self.armor)[0]
        newAC = AC + int(self.shield) + dScoreModifier[self.dDex]
        self.AC = newAC

    def dCheckStatus(self):
        if self.HitPoints > 0:
            self.alive = True
        else:
            self.alive = False
        if self.XP >= dXPlevelUP[self.lvl+1][0]:
            self.levelUP()

    def levelUP(self):
            self.lvl += 1
            self.HitDiceCount += 1
            addHP = randGen(1,self.HitDice)+dScoreModifier[self.dCons]
            if addHP < 1:
                addHP = 1
            self.MaxHP += addHP
            self.HitPoints = copy.deepcopy(self.MaxHP)

    def heal(self):
        self.HitPoints += randGen(1,self.HitDice)
        if self.HitPoints > self.MaxHP:
            self.HitPoints = copy.deepcopy(self.MaxHP)
        self.HitDiceCount -= 1


class Hero(Unit):
    def __init__(self,name):
        Unit.__init__(self,name)
        self.kills = 0
        self.canHeal = True
        self.canLoot = True
        self.calcAC()


class Mob(Unit):
    def __init__(self):
        Unit.__init__(self,"")

        self.name = random.choice(challenge_1)
        # self.name = random.choice(random.choice(challenge_all))
        mobParams =  MD.monsterDict[self.name]
        self.dRaceName	= "monster"
        self.dRace		= "monster"
        self.dClass		= "monster"
        self.dStr		= mobParams[5][0]
        self.dDex		= mobParams[5][1]
        self.dCons		= mobParams[5][2]
        self.dInt		= mobParams[5][3]
        self.dWis		= mobParams[5][4]
        self.dCha		= mobParams[5][5]
        # self.dClass 	= random.choice(dClasses.keys())
        # self.HitDice 	= mobParams[]
        # self.HitDiceCount = 1
        # self.HitPoints 	= self.HitDice + dScoreModifier[self.dCons]
        self.HitPoints 	= self.calcHP(mobParams[3])
        self.MaxHP		= copy.deepcopy(self.HitPoints)
        self.armor		= None
        self.shield		= 0
        self.AC			= int(mobParams[2])
        self.weapon		= random.choice(dItemsWeaponsMele.keys())
        self.XpReword	= int(mobParams[9])
        self.canHeal    = False
        self.canLoot    = False


    def calcHP(self,x):
        x = x.split()
        result = diceRoll(x[0])
        if len(x)> 1:
            stringa = "%s%s%s"%(result, x[1],x[2])
            result = eval(stringa)
        if result <= 0:
            result = 1
        return result


def diceRoll(dice):
    x = dice.split("d")
    result = 0
    for times in range(int(x[0])):
        result += randGen(1,int(x[1]))
    return result


def randGen(startNum,endNum):
    return random.randint(startNum,endNum)


def mobNameGen():
    print random.choice(random.choice(challenge_all))

    return random.choice(dListOfNamesD.keys())


def abilityGen(numOfRolls):
    rollsList = []
    for x in range(numOfRolls):
        rollsList.append(randGen(1,6))

    return sum(sorted(rollsList)[1:])


def setCanvasGrid(canv , rows , columns):
    for line in range(rows):
        x = line*(canv.canvasWidth/rows)
        canv.canvas.create_line(x,0,x,canv.canvasHeight,fill="black")
    for line in range(columns):
        y = line*(canv.canvasWidth/columns)
        canv.canvas.create_line(0,y,canv.canvasWidth,y,fill="black")


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
    app = GuiSetup(None,"mafrum")
    app.title("test")
    app.mainloop()


def parse_monster_list():
    import re
    # fileList = open("monster list.txt","r").readlines()
    fileList = open("Nonplayer Characters example.txt","r").readlines()
    # dummyFile = open("temp.txt","w")
    textList = []
    sets = []
    x=[]
    for line in fileList:
        if line == '\n':
            sets.append(x)
            x=[]
            continue
        x.append(line.strip())

    for set in sets:
        if set == []:
            continue
        name,size,alighment,AC,HP,speed,params,hardDmg,calcDmg,challenge,XP = "","","","","","","","","","",""

        # print "\n"

        # print set

        # print set[0] 	# name
        name = set[0] 	# name

        # print set[1] 	# size , alighment
        size = set[1].split(",")[0].split(" ")[0]	# size , alighment
        alighment = set[1].split(",")[1].strip()	# size , alighment

        # print set[2]	# armor class
        AC = set[2].split(" ")[2]	# armor class

        # print set[3].split("(")[1].split(")")[0]	# hit points
        HP = set[3].split("(")[1].split(")")[0]	# hit points

        # print set[4]	# speed
        speed =  set[4].split(" ")[1]	# speed

        # print set[5]	# "STR DEX CON INT WIS CHA"

        # print map(int,set[6].split()[0::2])	# STR DEX CON INT WIS CHA
        params =  map(int,set[6].split()[0::2])	# STR DEX CON INT WIS CHA

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
        print ("'%s':( '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' ),")%(
            name,size,alighment,AC,HP,speed,params,hardDmg,calcDmg,challenge,XP)


def monster_generator_test():
    mob = Mob()


if(__name__ == "__main__"):
    gui_test()

    # main(sys.argv[1])
    # parse_monster_list()

    # monster_generator_test()































