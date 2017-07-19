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