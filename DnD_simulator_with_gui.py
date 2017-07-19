########
#http://www.wikihow.com/Create-a-Dungeons-and-Dragons-Character
#https://docs.google.com/spreadsheets/d/1fjnoCiYUCOcrMxffWNwppHfuUDlY1Ae0HQ4t-XCaiPA/edit#gid=0
#https://drive.google.com/file/d/0B8mF8uNMRN_mLUJRNmkwaDB3R3M/view
#https://www.dandwiki.com/wiki/5e_Weapons
#https://stackoverflow.com/questions/20149483/python-canvas-and-grid-tkinter
# http://media.wizards.com/2016/downloads/DND/DMBasicRulesV05.pdf
########
import random
import sys
import copy
from time import sleep
import Tkinter
from Tkinter import N,S,E,W

import canvas_test as maps
from dictionaries import *



class GuiSetup(Tkinter.Tk):
	def __init__(self,parent,heroName):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.heroName = heroName
		# self.geometry("400x250+600+600")
		# self.resizable(width=False,height=False)
		self.initialize()
		
	def initialize(self):
		self.grid()
		
		
		self.canvasWidth = 300
		self.canvasHeight = 300
		self.canvas=Tkinter.Canvas(self, width=self.canvasWidth, height=self.canvasHeight, background='white')
		self.canvas.grid(row=0,column=11,rowspan=11)
		
		self.myMap = maps.mainMap(self)
		maps.setCanvasGrid(self,self.myMap.rows,self.myMap.columns)
		
		mainFrame = Tkinter.Frame(self, borderwidth=5, relief="sunken", width=500, height=200)
		mainFrame.grid(column=0, row=0, columnspan=10, rowspan=11, sticky=(N, S, E, W))

		
		self.button1 = Tkinter.Button(self,text=u"run simulator",command=self.runSimulator)
		self.text_title = Tkinter.Label(self,text="Battle:")
		self.text_title.grid(	column=5,row=0)
		self.button1.grid(		column=5,row=10,sticky=N+S+E+W)


		###################################################
		# window setup
		self.text_hero_name			= Tkinter.Label(self,text="Name:")
		self.text_hero_race			= Tkinter.Label(self,text="Race:")
		self.text_hero_class		= Tkinter.Label(self,text="Class:")
		self.text_hero_Str			= Tkinter.Label(self,text="Str:")
		self.text_hero_Dex			= Tkinter.Label(self,text="Dex:")
		self.text_hero_Con			= Tkinter.Label(self,text="Con:")
		self.text_hero_Int			= Tkinter.Label(self,text="Int:")
		self.text_hero_Wis			= Tkinter.Label(self,text="Wis:")
		self.text_hero_Cha			= Tkinter.Label(self,text="Cha:")
		self.text_hero_name_V		= Tkinter.Label(self)
		self.text_hero_race_V		= Tkinter.Label(self)
		self.text_hero_class_V		= Tkinter.Label(self)
		self.text_hero_Str_V		= Tkinter.Label(self)
		self.text_hero_Dex_V		= Tkinter.Label(self)
		self.text_hero_Con_V		= Tkinter.Label(self)
		self.text_hero_Int_V		= Tkinter.Label(self)
		self.text_hero_Wis_V		= Tkinter.Label(self)
		self.text_hero_Cha_V		= Tkinter.Label(self)
		self.text_hero_HitPoints	= Tkinter.Label(self,text="Hit Points")
		self.text_hero_HitPoints_V	= Tkinter.Label(self)
		self.text_hero_AC			= Tkinter.Label(self,text="AC")
		self.text_hero_AC_V			= Tkinter.Label(self)
		self.text_hero_kills		= Tkinter.Label(self,text="Kills")
		self.text_hero_kills_V		= Tkinter.Label(self)

		self.text_monster_name		= Tkinter.Label(self,text="Name:")
		self.text_monster_race		= Tkinter.Label(self,text="Race:")
		self.text_monster_class		= Tkinter.Label(self,text="Class:")
		self.text_monster_Str		= Tkinter.Label(self,text="Str:")
		self.text_monster_Dex		= Tkinter.Label(self,text="Dex:")
		self.text_monster_Con		= Tkinter.Label(self,text="Con:")
		self.text_monster_Int		= Tkinter.Label(self,text="Int:")
		self.text_monster_Wis		= Tkinter.Label(self,text="Wis:")
		self.text_monster_Cha		= Tkinter.Label(self,text="Cha:")
		self.text_monster_name_V	= Tkinter.Label(self)
		self.text_monster_race_V	= Tkinter.Label(self)
		self.text_monster_class_V	= Tkinter.Label(self)
		self.text_monster_Str_V		= Tkinter.Label(self)
		self.text_monster_Dex_V		= Tkinter.Label(self)
		self.text_monster_Con_V		= Tkinter.Label(self)
		self.text_monster_Int_V		= Tkinter.Label(self)
		self.text_monster_Wis_V		= Tkinter.Label(self)
		self.text_monster_Cha_V		= Tkinter.Label(self)
		self.text_monster_HitPoints	= Tkinter.Label(self,text="Hit Points")
		self.text_monster_HitPoints_V	= Tkinter.Label(self)
		self.text_monster_AC		= Tkinter.Label(self,text="AC")
		self.text_monster_AC_V		= Tkinter.Label(self)


		#GRID
		self.text_hero_name.grid(			column=1,row=1, sticky=W+E)	
		self.text_hero_race.grid(			column=1,row=2, sticky=W+E)	
		self.text_hero_class.grid(			column=1,row=3, sticky=W+E)
		self.text_hero_Str.grid(			column=1,row=4, sticky=W+E)	
		self.text_hero_Dex.grid(			column=1,row=5, sticky=W+E)	
		self.text_hero_Con.grid(			column=1,row=6, sticky=W+E)	
		self.text_hero_Int.grid(			column=1,row=7, sticky=W+E)	
		self.text_hero_Wis.grid(			column=1,row=8, sticky=W+E)	
		self.text_hero_Cha.grid(			column=1,row=9, sticky=W+E)
		                                                    
		self.text_hero_name_V.grid(			column=2,row=1, sticky=W+E)	
		self.text_hero_race_V.grid(			column=2,row=2, sticky=W+E)	
		self.text_hero_class_V.grid(		column=2,row=3, sticky=W+E)
		self.text_hero_Str_V.grid(			column=2,row=4, sticky=W+E)	
		self.text_hero_Dex_V.grid(			column=2,row=5, sticky=W+E)	
		self.text_hero_Con_V.grid(			column=2,row=6, sticky=W+E)	
		self.text_hero_Int_V.grid(			column=2,row=7, sticky=W+E)	
		self.text_hero_Wis_V.grid(			column=2,row=8, sticky=W+E)	
		self.text_hero_Cha_V.grid(			column=2,row=9, sticky=W+E)	
		
		self.text_hero_HitPoints.grid(		column=3,row=2)
		self.text_hero_HitPoints_V.grid(	column=3,row=3)
		self.text_hero_AC.grid(				column=3,row=4)
		self.text_hero_AC_V.grid(			column=3,row=5)
		self.text_hero_kills.grid(			column=3,row=6)
		self.text_hero_kills_V.grid(		column=3,row=7)
		
		self.text_monster_name.grid(		column=7,row=1, sticky=W+E)	
		self.text_monster_race.grid(		column=7,row=2, sticky=W+E)	
		self.text_monster_class.grid(		column=7,row=3, sticky=W+E)	
		self.text_monster_Str.grid(			column=7,row=4, sticky=W+E)	
		self.text_monster_Dex.grid(			column=7,row=5, sticky=W+E)	
		self.text_monster_Con.grid(			column=7,row=6, sticky=W+E)	
		self.text_monster_Int.grid(			column=7,row=7, sticky=W+E)	
		self.text_monster_Wis.grid(			column=7,row=8, sticky=W+E)	
		self.text_monster_Cha.grid(			column=7,row=9, sticky=W+E)	
		self.text_monster_name_V.grid(		column=8,row=1, sticky=W+E)	
		self.text_monster_race_V.grid(		column=8,row=2, sticky=W+E)	
		self.text_monster_class_V.grid(		column=8,row=3, sticky=W+E)	
		self.text_monster_Str_V.grid(		column=8,row=4, sticky=W+E)	
		self.text_monster_Dex_V.grid(		column=8,row=5, sticky=W+E)	
		self.text_monster_Con_V.grid(		column=8,row=6, sticky=W+E)	
		self.text_monster_Int_V.grid(		column=8,row=7, sticky=W+E)	
		self.text_monster_Wis_V.grid(		column=8,row=8, sticky=W+E)	
		self.text_monster_Cha_V.grid(		column=8,row=9, sticky=W+E)	
		self.text_monster_HitPoints.grid(	column=6,row=2)
		self.text_monster_HitPoints_V.grid(	column=6,row=3)
		self.text_monster_AC.grid(			column=6,row=4)
		self.text_monster_AC_V.grid(		column=6,row=5)
		
		
	def runSimulator(self):
		self.gui_dBattle()
	
	def gui_dBattle(self):
		hero = Hero(self.heroName)
		
		
		# print self.myMap.mapMatrix
		figuresSizeX = self.canvasWidth/self.myMap.columns
		figuresSizeY = self.canvasHeight/self.myMap.rows
		# print figuresSizeX
		# print figuresSizeY
		figure1=self.canvas.create_oval(0, 0, figuresSizeX, figuresSizeY, fill="blue")
		self.update()
		sleep(5)
		self.canvas.move(figure1,figuresSizeX,figuresSizeY)
		
		return
		
		while hero.alive:
			monster = Hero(mobNameGen())
			self.updateGameInfo(hero,monster)
			self.update()
			sleep(1)
			# break ###########################
			self.gui_dFight(hero,monster)
			if hero.alive:
				hero.XP += monster.XpReword
				hero.kills += 1
				hero.dCheckStatus()		
		
	def	gui_dFight(self,hero,monster):	
	
		while hero.alive and monster.alive:
			sleep(1)
			hero_initiative = dScoreModifier[hero.dDex]
			monster_initiative = dScoreModifier[monster.dDex]
			if hero_initiative >= monster_initiative:
				self.gui_dAttack(hero,monster)
			else:
				self.gui_dAttack(monster,hero)

			
			self.text_hero_HitPoints_V.config(text=hero.HitPoints) 
			self.text_monster_HitPoints_V.config(text=monster.HitPoints)
			hero.dCheckStatus()
			monster.dCheckStatus()
			self.update()
		
		
	def gui_dAttack(self,first,second):
		#first attacks
		if randGen(1,20) > second.AC:
			self.gui_dAttackTurns(first,second)
			second.dCheckStatus()	
		#second attacks
		if randGen(1,20) > first.AC and second.alive:	
			self.gui_dAttackTurns(second,first)	

			
	def gui_dAttackTurns(self,attacker,attacked):
		diceRoll = randGen(1,20)
		if diceRoll == 1:
			return
		elif diceRoll == 20:
			attacked.HitPoints -= self.demageCalc(attacker)+self.demageCalc(attacker)
		else:
			attacked.HitPoints -= self.demageCalc(attacker)
			
			
	def demageCalc(self,attacker):
		#mele attack
		return randGen(dItemsWeaponsMele.get(attacker.weapon)[0],dItemsWeaponsMele.get(attacker.weapon)[1]) + dScoreModifier[attacker.dStr]
		#ranged attack
		return randGen(dItemsWeaponsRanged.get(attacker.weapon)[0],dItemsWeaponsRanged.get(attacker.weapon)[1]) + dScoreModifier[attacker.dDex]

		
	def updateGameInfo(self,hero,monster):
		self.text_hero_name_V.config(		text=hero.name)	
		self.text_hero_race_V.config(		text=hero.dRaceName)	
		self.text_hero_class_V.config(		text=hero.dClass)		
		self.text_hero_Str_V.config(		text=hero.dStr)		
		self.text_hero_Dex_V.config(		text=hero.dDex)		
		self.text_hero_Con_V.config(		text=hero.dCons)		
		self.text_hero_Int_V.config(		text=hero.dInt)		
		self.text_hero_Wis_V.config(		text=hero.dWis)		
		self.text_hero_Cha_V.config(		text=hero.dCha)		
		self.text_hero_HitPoints_V.config(	text=hero.HitPoints)		
		self.text_hero_AC_V.config(			text=hero.AC)		
		self.text_hero_kills_V.config(		text=hero.kills)
		
		self.text_monster_name_V.config(	text=monster.name)	
		self.text_monster_race_V.config(	text=monster.dRaceName)	
		self.text_monster_class_V.config(	text=monster.dClass)		
		self.text_monster_Str_V.config(		text=monster.dStr)		
		self.text_monster_Dex_V.config(		text=monster.dDex)		
		self.text_monster_Con_V.config(		text=monster.dCons)		
		self.text_monster_Int_V.config(		text=monster.dInt)		
		self.text_monster_Wis_V.config(		text=monster.dWis)		
		self.text_monster_Cha_V.config(		text=monster.dCha)		
		self.text_monster_HitPoints_V.config(	text=monster.HitPoints)		
		self.text_monster_AC_V.config(		text=monster.AC)		
	

class Unit:
	def __init__(self,name,HP):
		self.name 	= name
		self.alive 	= True
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
		self.AC			= self.calcAC()
		self.weapon		= random.choice(dItemsWeaponsMele.keys())
		self.XpReword	= 300
		self.inventory	= {}
		
	def dmgCalc(self):
		dmg = int(self.Str/4)
		if dmg < 1:
			dmg = 1
		return dmg
		
			
	def calcAC(self):
		AC = 10
		if self.armor != None:
			AC = dItemsArmors.get(self.armor)[0]
		return AC + self.shield + dScoreModifier[self.dDex]
	
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


class Hero(Unit):
	def __init__(self,name):
		Unit.__init__(self,name,randGen(20,45))
		self.kills = 0

		
class Mob(Unit):
	def __init__(self):
		Unit.__init__(self,mobNameGen(),randGen(20,45))
		self.XpReword = randGen(1,5)

			
def randGen(startNum,endNum):
	return random.randint(startNum,endNum)

	
def mobNameGen():
	return random.choice(dListOfNamesD.keys())


def abilityGen(numOfRolls):
	rollsList = []
	for x in range(numOfRolls):
		rollsList.append(randGen(1,6))
	
	return sum(sorted(rollsList)[1:])	

	
def gui_test():
	app = GuiSetup(None,"mafrum")
	app.title("test")
	app.mainloop()
	
	
if(__name__ == "__main__"):
	# main(sys.argv[1])
	gui_test()

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	