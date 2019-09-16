import random
import copy
from PyQt5 import QtCore
from dictionaries import *
import monster_dictionary as MD

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
        self.figuresSizeX = 0
        self.figuresSizeY = 0
        self.x0 = 0
        self.x1 = 0
        self.y0 = 0
        self.y1 = 0
        self.dij = []
        self.qtitem = None

    def populate_space_on_grid(self, gui, sell=None):
        if sell != None:
            print('mof')
            self.location = sell
        else:
            # self.location = random.choice(list(gui.myMap.mapMatrix.keys()))
            self.location = random.choice(list(gui.myMap.freeSpaces()))
        self.figuresSizeX = gui.canvasWidth / gui.myMap.columns
        self.figuresSizeY = gui.canvasHeight / gui.myMap.rows
        # calculate size for the unit
        self.x0 = self.location[0] * self.figuresSizeX
        self.x1 = (1 + self.location[0]) * self.figuresSizeX
        self.y0 = self.location[1] * self.figuresSizeY
        self.y1 = (1 + self.location[1]) * self.figuresSizeY

    def populate_space_on_grid_pyqt5(self, gui, side, sell=None):

        if sell != None:
            self.location = sell
        else:
            # self.location = random.choice(list(gui.myMap.mapMatrix.keys()))

            self.location = random.choice(list(gui.freeSpaces()))

        self.figuresSizeX = side / gui.columns
        self.figuresSizeY = side / gui.rows
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
        addHP = random.randint(1, self.HitDice) + dScoreModifier[self.dCons]
        if addHP < 1:
            addHP = 1
        self.MaxHP += addHP
        self.HitPoints = copy.deepcopy(self.MaxHP)

    def heal(self):
        self.HitPoints += random.randint(1, self.HitDice)
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
        self.type = "hero"
        self.kills = 0
        self.canHeal = True
        self.canLoot = True
        self.weaponName = random.choice(list(dItemsWeaponsMele.keys()))
        self.weapon = dItemsWeaponsMele[self.weaponName]
        self.calcAC()
        self.color = QtCore.Qt.blue


class Mob(Unit):
    def __init__(self):
        Unit.__init__(self, "")

        self.type = "monster"
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
        self.color = QtCore.Qt.red

    def calcHP(self, x):
        x = x.split()
        result = diceRoll(x[0])
        if len(x) > 1:
            stringa = "%s%s%s" % (result, x[1], x[2])
            result = eval(stringa)
        if result <= 0:
            result = 1
        return result

def diceRoll(dice):
    x = dice.split("d")
    result = 0
    for times in range(int(x[0])):
        result += random.randint(1, int(x[1]))
    return result

def abilityGen(numOfRolls):
    rollsList = []
    for x in range(numOfRolls):
        rollsList.append(random.randint(1, 6))

    return sum(sorted(rollsList)[1:])
