########
#http://www.wikihow.com/Create-a-Dungeons-and-Dragons-Character
#https://docs.google.com/spreadsheets/d/1fjnoCiYUCOcrMxffWNwppHfuUDlY1Ae0HQ4t-XCaiPA/edit#gid=0
#https://drive.google.com/file/d/0B8mF8uNMRN_mLUJRNmkwaDB3R3M/view
#https://www.dandwiki.com/wiki/5e_Weapons
#https://stackoverflow.com/questions/20149483/python-canvas-and-grid-tkinter
########
import random
import sys
from time import sleep
import Tkinter
from Tkinter import N,S,E,W


#Race name: size,speed,[Str,Dex,Con,Int,Wis,Cha]
dRacess = {	
			'Aarakorca'	:('M',25,[0,2,0,0,1,0]),
			'Aasimar'	:('M',30,[0,0,0,0,0,2]),
			'Bugnear'	:('M',30,[2,1,0,0,0,0]),
			'Dragonborn':('M',30,[2,0,0,0,0,1]),
			'Dwarf'		:('M',25,[0,0,2,0,0,0]),
			'Elf'		:('M',30,[0,2,0,0,0,0]),
			'Firbolg'	:('M',30,[1,0,0,0,2,0]),
			'Genasi'	:('M',30,[0,0,1,0,0,0]),
			'Gnome'		:('S',25,[0,0,0,0,0,0]),
			'Goblin'	:('S',30,[0,2,1,0,0,0]),
			'Goliath'	:('M',30,[2,0,1,0,0,0]),
			'Hafling'	:('S',25,[0,2,0,0,0,0]),
			'Half-Elf'	:('M',30,[0,0,0,0,0,2]),
			'Half-Orc'	:('M',30,[2,0,1,0,0,0]),
			'Hobgoblin'	:('M',30,[0,0,2,1,0,0]),
			'Human'		:('M',30,[1,1,1,1,1,1]),
			'Kender'	:('S',25,[0,1,0,0,0,1]),
			'Kenku'		:('M',30,[0,2,0,0,1,0]),
			'Kobold'	:('S',30,[-2,2,0,0,0,0]),
			'Lizardfolk':('M',30,[0,0,2,0,1,0]),
			'Orc'		:('M',30,[2,0,1,-2,0,0]),
			'Tabaxi'	:('M',30,[0,2,0,0,0,1]),
			'Tifling'	:('M',30,[0,0,0,1,0,2]),
			'Triton'	:('M',30,[1,0,1,0,0,1]),
			'Yuan-Ti'	:('M',30,[0,0,0,1,0,2]),
			}


#class name , hitdie
dClasses = {	
			'barbarian':12,
			'bard':		8,
			'cleric':	8,
			'druid':	8,
			'fighter':	10,
			'monk':		8,
			'paladin':	10,
			'ranger':	10,
			'rouge':	8,
			'sorcerer':	6,
			'warlock':	8,
			'wizard':	6
			}


dScoreModifier = {	
					1:-5,
					2:-4,3:-4,
					4:-3,5:-3,
					6:-2,7:-2,
					8:-1,9:-1,
					10:0,11:0,
					12:1,13:1,
					14:2,15:2,
					16:3,17:3,
					18:4,19:4,
					20:5,21:5,
					22:6,23:6
					}

#name : AR , set or add,score Modifer addon
dItemsArmors = {	'Leather Lamellar':(12,'s','DEX'),
					'Plated Leather Armor':(13,'s','DEX'),
					'Battle Robe':(11,'s','DEX'),
					'Chain Cloth':(16,'s','DEX'),
					'Lorica Segmentata':(15,'s'),
					'Steam Armor':(18,'s'),
					'Wyvern Bone Armor':(17,'s')
					}

dItemsSields = {	
					'Bukler':(1,'a'),
					'Wicker shield':(1,'a'),
					'Wyvern Bone Shield':(2,'a'),
					'Tower Shield':(3,'a')
				}

dItemsWeaponsMele = {
						'Sword':(1,4)
						}

dItemsWeaponsRanged = {
						'bow':(1,4)
						}


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
		
		self.button1 = Tkinter.Button(self,text=u"run simulator",command=self.runSimulator)
		self.text_title = Tkinter.Label(self,text="Battle:")
		self.text_title.grid(				column=5,row=0)
		self.button1.grid(					column=5,row=10)
		
		mainFrame = Tkinter.Frame(self, borderwidth=5, relief="sunken", width=400, height=200)
		mainFrame.grid(column=0, row=1, columnspan=10, rowspan=9, sticky=(N, S, E, W))
		
		# self.text_KILLS = Tkinter.Label(self,text="KILLS:")
		# self.text_KILLS.grid(				column=0,row=6)	
		
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
		self.text_hero_name.grid(			column=0,row=1, sticky='W')	
		self.text_hero_race.grid(			column=0,row=2, sticky='W')	
		self.text_hero_class.grid(			column=0,row=3, sticky='W')
		self.text_hero_Str.grid(			column=0,row=4, sticky='W')	
		self.text_hero_Dex.grid(			column=0,row=5, sticky='W')	
		self.text_hero_Con.grid(			column=0,row=6, sticky='W')	
		self.text_hero_Int.grid(			column=0,row=7, sticky='W')	
		self.text_hero_Wis.grid(			column=0,row=8, sticky='W')	
		self.text_hero_Cha.grid(			column=0,row=9, sticky='W')
		self.text_hero_name_V.grid(			column=1,row=1, sticky='W')	
		self.text_hero_race_V.grid(			column=1,row=2, sticky='W')	
		self.text_hero_class_V.grid(		column=1,row=3, sticky='W')
		self.text_hero_Str_V.grid(			column=1,row=4, sticky='W')	
		self.text_hero_Dex_V.grid(			column=1,row=5, sticky='W')	
		self.text_hero_Con_V.grid(			column=1,row=6, sticky='W')	
		self.text_hero_Int_V.grid(			column=1,row=7, sticky='W')	
		self.text_hero_Wis_V.grid(			column=1,row=8, sticky='W')	
		self.text_hero_Cha_V.grid(			column=1,row=9, sticky='W')	
		self.text_hero_HitPoints.grid(		column=2,row=2)
		self.text_hero_HitPoints_V.grid(	column=2,row=3)
		self.text_hero_AC.grid(				column=2,row=4)
		self.text_hero_AC_V.grid(			column=2,row=5)
			
		self.text_monster_name.grid(		column=7,row=1, sticky='W')	
		self.text_monster_race.grid(		column=7,row=2, sticky='W')	
		self.text_monster_class.grid(		column=7,row=3, sticky='W')	
		self.text_monster_Str.grid(			column=7,row=4, sticky='W')	
		self.text_monster_Dex.grid(			column=7,row=5, sticky='W')	
		self.text_monster_Con.grid(			column=7,row=6, sticky='W')	
		self.text_monster_Int.grid(			column=7,row=7, sticky='W')	
		self.text_monster_Wis.grid(			column=7,row=8, sticky='W')	
		self.text_monster_Cha.grid(			column=7,row=9, sticky='W')	
		self.text_monster_name_V.grid(		column=8,row=1, sticky='W')	
		self.text_monster_race_V.grid(		column=8,row=2, sticky='W')	
		self.text_monster_class_V.grid(		column=8,row=3, sticky='W')	
		self.text_monster_Str_V.grid(		column=8,row=4, sticky='W')	
		self.text_monster_Dex_V.grid(		column=8,row=5, sticky='W')	
		self.text_monster_Con_V.grid(		column=8,row=6, sticky='W')	
		self.text_monster_Int_V.grid(		column=8,row=7, sticky='W')	
		self.text_monster_Wis_V.grid(		column=8,row=8, sticky='W')	
		self.text_monster_Cha_V.grid(		column=8,row=9, sticky='W')	
		self.text_monster_HitPoints.grid(	column=6,row=2)
		self.text_monster_HitPoints_V.grid(	column=6,row=3)
		self.text_monster_AC.grid(			column=6,row=4)
		self.text_monster_AC_V.grid(		column=6,row=5)
		

		
	def runSimulator(self):
		# self.gui_battle()
		self.gui_dBattle()
	
	def gui_dBattle(self):
		hero = Hero(self.heroName)
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
			second.HitPoints -= randGen(dItemsWeaponsMele.get(first.weapon)[0],dItemsWeaponsMele.get(first.weapon)[1]) + dScoreModifier[first.dDex]
		#second attacks
		if randGen(1,20) > first.AC:
			first.HitPoints -= randGen(dItemsWeaponsMele.get(second.weapon)[0],dItemsWeaponsMele.get(second.weapon)[1]) + dScoreModifier[second.dDex]
			

		
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
	
		# self.text_hero_KILLS.config(text=hero.kills)

		
	def gui_battle(self):
		hero = Hero(sys.argv[1])

		while hero.alive:
			monster = Mob()
			self.text_hero_name.config(text=hero.name)
			self.text_hero_XP.config(text=hero.XP)
			self.text_monster_name.config(text=monster.name)	
			self.text_hero_KILLS.config(text=hero.kills)			
			self.gui_fight(hero,monster)
			if hero.alive:
				hero.XP += monster.XpReword
				hero.kills += 1
				hero.checkStatus()
		
	def gui_fight(self,hero,monster):
		while True:
			sleep(0.1)
			hero.HP 	-= monster.Dmg*randGen(0,3)
			monster.HP 	-= hero.Dmg*randGen(0,3)
			hero.checkStatus()
			monster.checkStatus()
			self.text_hero_HP.config(text=hero.HP) 
			self.text_monster_HP.config(text=monster.HP) 
			
			self.update()
			if not (hero.alive and monster.alive):
				break
		

class Unit:
	def __init__(self,name,HP):
		self.name 	= name
		self.Str 	= randGen(1,20) 
		self.Sta 	= randGen(1,20)
		self.MaxHP 	= HP*self.Sta
		self.HP 	= HP*self.Sta
		self.Dmg	= self.dmgCalc()
		self.alive 	= True
		self.XP		= 0
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
		self.HitPoints 	= self.HitDice + dScoreModifier[self.dCons]
		self.armor		= None
		self.shield		= 0
		self.AC			= self.calcAC()
		self.weapon		= random.choice(dItemsWeaponsMele.keys())
		self.XpReword	= 1
		
	def dmgCalc(self):
		dmg = int(self.Str/4)
		if dmg < 1:
			dmg = 1
		return dmg
	
	
	def checkStatus(self):
		if self.HP > 0:
			self.alive = True
		else:
			self.alive = False
		
		if self.XP >= 10:
			self.HP = self.MaxHP
			self.XP -= 10

			
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
		
		if self.XP >= 10:
			self.HitPoints = self.MaxHP
			self.XP -= 10		
	
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
	nameList = ["Grolla","mugdolen","ahab","shlunzon"]
	return nameList[randGen(0,len(nameList)-1)]


def abilityGen(numOfRolls):
	rollsList = []
	for x in range(numOfRolls):
		rollsList.append(randGen(1,6))
	
	return sum(sorted(rollsList)[1:])	

def fight(hero,mob):
	while True:
		sleep(0.1)
		hero.HP -= mob.Dmg*randGen(0,3)
		mob.HP 	-= hero.Dmg*randGen(0,3)
		hero.checkStatus()
		mob.checkStatus()
		sys.stdout.write( "%s:%s %s:%s   \r"%(hero.name,hero.HP,mob.name,mob.HP))
		sys.stdout.flush()
		if not (hero.alive and mob.alive):
			break


def battle(hero):	
	while hero.alive:
		mob = Mob()
		print ""
		fight(hero,mob)
		if hero.alive:
			hero.XP += mob.XpReword
			hero.kills += 1
	print "\nKills:",hero.kills

		
def main(name):
	mob = Mob()
	hero = Hero(name)
	battle(hero)

	
def game(name):
	# mob = Mob()
	hero = Hero(name)
	# app.text_hero_name.config(text=hero.name)
	battle(hero)


	
def gui_test():
	app = GuiSetup(None,"mafrum")
	app.title("test")
	app.mainloop()
	
	
if(__name__ == "__main__"):
	# main(sys.argv[1])
	gui_test()

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	