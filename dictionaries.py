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
					0:-5,1:-5,
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
					22:6,23:6,
					24:7,25:7,
					26:8,27:8,
					28:9,29:9
					}


#name : AR , set or add,score Modifer addon
dItemsArmors = {	
					'Light Armor Padded':(11,'s','DEX'),
					'Light Armor Leather':(11,'s','DEX'),
					'Light Armor Studded leather':(12,'s','DEX'),
					'Medium Armor Hide':(12,'s','DEX'),
					'Medium Armor Chain shirt':(13,'s','DEX'),
					'Medium Armor Scale mail':(14,'s','DEX'),
					'Medium Armor Breastplate':(14,'s','DEX'),
					'Medium Armor Half plate':(15,'s','DEX'),
					'Heavy Armor Ring mail':(14,'s',''),
					'Heavy Armor Chain mail':(16,'s',''),
					'Heavy Armor Splint':(17,'s',''),
					'Heavy Armor Plate':(18,'s','')
				}
'''	'Leather Lamellar':(12,'s','DEX'),
'Plated Leather Armor':(13,'s','DEX'),
'Battle Robe':(11,'s','DEX'),
'Chain Cloth':(16,'s','DEX'),
'Lorica Segmentata':(15,'s'),
'Steam Armor':(18,'s'),
'Wyvern Bone Armor':(17,'s')
}
'''
				
					
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


dListOfNamesD = {
				'Dian':(), 'Nese':(), 'Falledrick':(), 'Mae':(), 'Valhein':(), 'Dol':(), 'Earl':(), 'Cedria':(),
				'Azulei':(), 'Yun':(), 'Cybel':(), 'Ina':(), 'Foolly':(), 'Skili':(), 'Juddol':(), 'Janver':(),
				'Viska':(), 'Hirschendy':(), 'Silka':(), 'Hellsturn':(), 'Essa':(), 'Mykonos':(),
				'Fenton':(), 'Tyrena':(), 'Inqoul':(), 'Mankov':(), 'Derilia':(), 'Hexema':(), 'Wyton':(),
				'Kaedum':(), 'Gouram':(), 'Libertia':(), 'Berasailles':(), 'Juxta':(), 'Taehr':(),
				'Comtol':(), 'Gherak':(), 'Hest':(), 'Qony':(), 'Masamka':(), 'Twyll':(), 'Tenos':(), 'Axim':(),
				'Westrynda':(), 'Saphros':(), 'Olkham':(), 'Handok':(), 'Kemetra':(), 'Yos':(),
				'Wentingle':(), 'Ames':(), 'Molosh':(), 'Inkov':(), 'Phasasia':(), 'Ziedinghal':(),
				'Bregul':(), 'Eishvack':(), 'Lora':(), 'Krenting':(), 'Symbole':(), 'Elignoir':(),
				'Keligkrul':(), 'Qwey':(), 'Vindinglag':(), 'Kusakira':(), 'Weme':(), 'Fayd':(),
				'Rushvita':(), 'Vulkor':(), 'Amers':(), 'Ortos':(), 'Vanius':(), 'Chandellia':(),
				'Lilikol':(), 'Catca':(), 'Cormus':(), 'Yuela':(), 'Ariban':(), 'Tryton':(), 'Fesscha':(),
				'Opalul':(), 'Zakzos':(), 'Hortimer':(), 'Anklos':(), 'Dushasiez':(), 'Polop':(),
				'Mektal':(), 'Orinphus':(), 'Denatra':(), 'Elkazzi':(), 'Dyne':(), 'Domos':(),
				'Letryal':(), 'Manniv':(), 'Sylestia':(), 'Esnol':(), 'Fasafuros':(), 'Ghanfer':(),
				'Kahnite':(), 'Sweyda':(), 'Uylis':(), 'Retenia':(), 'Bassos':(), 'Arkensval':(),
				'Impelos':(), 'Grandius':(), 'Fulcrux':(), 'Lassahein':(), 'Edsveda':(), 'Earakun':(),
				'Fous':(), 'Maas':(), 'Basenphal':(), 'Jubidya':(), 'Divya':(), 'Kosunten':(),
				'Ordayius':(), 'Dozzer':(), 'Gangher':(), 'Escha':(), 'Manchul':(), 'Kempos':(), 'Kulo':(),
				'Urtench':(), 'Kesta':(), 'Helahona':(), 'Ryte':(), 'Falcia':(), 'Umannos':(),
				'Urkensvall':(), 'Fedra':(), 'Bulkensar':(), 'Comia':(), 'Tyul':(), 'Lasendarl':()
				}

#level:needed XP , Proficiency Bonus
dXPlevelUP = {
				1:(0		, +2),
				2:(300 		, +2),
				3:(900 		, +2),
				4:(2700 	, +2),
				5:(6500 	, +3),
				6:(14000 	, +3),
				7:(23000 	, +3),
				8:(34000 	, +3),
				9:(48000 	, +4),
				10:(64000 	, +4),
				11:(85000 	, +4),
				12:(100000 	, +4),
				13:(120000 	, +5),
				14:(140000 	, +5),
				15:(165000 	, +5),
				16:(195000 	, +5),
				17:(225000 	, +6),
				18:(265000 	, +6),
				19:(305000 	, +6),
				20:(355000 	, +6)
			}

############
#http://media.wizards.com/2016/downloads/DND/DMBasicRulesV05.pdf
############
#Challenge 0 (0-10 XP)
challenge_0 = [
				'Awakened Shrub',
				'Baboon',
				'Badger',
				'Bat',
				'Cat',
				'Commoner',
				'Crab',
				'Deer',
				'Eagle',
				'Frog',
				'Giant Fire Beetle',
				'Goat',
				'Hawk',
				'Hyena',
				'Jackal',
				'Lizard',
				'Octopus',
				'Owl',
				'Quipper',
				'Rat',
				'Raven',
				'Scorpion',
				'Sea Horse',
				'Spider',
				'Vulture',
				'Weasel'
				]

#Challenge 1/8 (25 XP)
challenge_1 = [
				'Bandit',
				'Blood Hawk',
				'Camel',
				'Cultist',
				'Flying Snake',
				'Giant Crab',
				'Giant Rat',
				'Giant Weasel',
				'Guard',
				'Kobold',
				'Mastiff',
				'Merfolk',
				'Mule',
				'Poisonous Snake',
				'Pony',
				'Stirge',
				'Twig Blight'
				]

#Challenge 1/4 (50 XP)
challenge_2 = [
				'Acolyte',
				'Axe beak',
				'Blink dog',
				'Boar',
				'Constrictor snake',
				'Draft horse',
				'Elk',
				'Flying sword',
				'Giant badger',
				'Giant bat',
				'Giant centipede',
				'Giant frog',
				'Giant lizard',
				'Giant owl',
				'Giant poisonous snake',
				'Giant wolf spider',
				'Goblin',
				'Panther',
				'Pteranodon',
				'Riding horse',
				'Skeleton',
				'Swarm of bats',
				'Swarm of rats',
				'Swarm of ravens',
				'Wolf',
				'Zombie'
				]

#Challenge 1/2 (100 XP)
challenge_3 = [
				'Ape',
				'Black bear',
				'Cockatrice',
				'Crocodile',
				'Giant goat',
				'Giant sea horse',
				'Giant wasp',
				'Gnoll',
				'Hobgoblin',
				'Lizardfolk',
				'Orc',
				'Reef shark',
				'Satyr',
				'Swarm of insects',
				'Thug',
				'Warhorse',
				'Worg'
				]

#Challenge 1 (200 XP)
challenge_4 = [
				'Animated armor',
				'Brown bear',
				'Bugbear',
				'Death dog',
				'Dire wolf',
				'Ghoul',
				'Giant eagle',
				'Giant hyena',
				'Giant octopus',
				'Giant spider',
				'Giant toad',
				'Giant vulture',
				'Harpy',
				'Hippogriff',
				'Lion',
				'Swarm of quippers',
				'Tiger'
				]

#Challenge 2 (450 XP)
challenge_5 = [
				'Allosaurus',
				'Awakened tree',
				'Berserker',
				'Centaur',
				'Gargoyle',
				'Giant boar',
				'Giant constrictor snake',
				'Giant elk',
				'Grick',
				'Griffon',
				'Hunter shark',
				'Nothic',
				'Ochre jelly',
				'Ogre',
				'Pegasus',
				'Plesiosaurus',
				'Polar bear',
				'Priest',
				'Rhinoceros',
				'Saber-toothed tiger',
				'Swarm of poisonous snakes'
				]

#Challenge 3 (700 XP)
challenge_6 = [
				'Ankylosaurus',
				'Basilisk',
				'Doppelganger',
				'Giant scorpion',
				'Hell hound',
				'Killer whale',
				'Knight',
				'Manticore',
				'Minotaur',
				'Mummy',
				'Owlbear',
				'Phase spider',
				'Spectator',
				'Werewolf',
				'Wight',
				'Winter wolf',
				'Yeti'
				]

#Challenge 4 (1',100 XP)
challenge_7 = [
				'Banshee',
				'Elephant',
				'Flameskull',
				'Ghost'
				]

#Challenge 5 (1',800 XP)
challenge_8 = [
				'Air elemental',
				'Earth elemental',
				'Fire elemental',
				'Flesh golem',
				'Giant crocodile',
				'Giant shark',
				'Hill giant',
				'Triceratops',
				'Troll',
				'Water elemental'
				]

#Challenge 6 (2',300 XP)
challenge_9 = [
				'Chimera',
				'Cyclops',
				'Mage',
				'Mammoth',
				'Medusa',
				'Wyvern'
				]

#Challenge 7 (2',900 XP)
challenge_10 = ['Giant ape']

#Challenge 8 (3',900 XP)
challenge_11 = [
				'Frost giant',
				'Hydra',
				'Tyrannosaurus rex',
				'Young green dragon'
				]

#Challenge 9 (5',000 XP)
challenge_12 = ['Fire giant']

#Challenge 10 (5,900 XP)
challenge_13 = ['Stone golem']

#Challenge 17 (18,000 XP)
challenge_14 = ['Adult red dragon']

challenge_all = [
				challenge_0,
				challenge_1,
				challenge_2,
				challenge_3,
				challenge_4,
				challenge_5,
				challenge_6,
				challenge_7,
				challenge_8,
				challenge_9,
				challenge_10,
				challenge_11,
				challenge_12,
				challenge_13,
				challenge_14
				]




