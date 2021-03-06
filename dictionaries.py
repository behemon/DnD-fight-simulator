# Race name: size,speed,[Str,Dex,Con,Int,Wis,Cha]
dRacess = {	
            'Aarakorca'	:('M', 25, [0, 2, 0, 0, 1, 0]),
            'Aasimar'	:('M', 30, [0, 0, 0, 0, 0, 2]),
            'Bugnear'	:('M', 30, [2, 1, 0, 0, 0, 0]),
            'Dragonborn':('M', 30, [2, 0, 0, 0, 0, 1]),
            'Dwarf'		:('M', 25, [0, 0, 2, 0, 0, 0]),
            'Elf'		:('M', 30, [0, 2, 0, 0, 0, 0]),
            'Firbolg'	:('M', 30, [1, 0, 0, 0, 2, 0]),
            'Genasi'	:('M', 30, [0, 0, 1, 0, 0, 0]),
            'Gnome'		:('S', 25, [0, 0, 0, 0, 0, 0]),
            'Goblin'	:('S', 30, [0, 2, 1, 0, 0, 0]),
            'Goliath'	:('M', 30, [2, 0, 1, 0, 0, 0]),
            'Hafling'	:('S', 25, [0, 2, 0, 0, 0, 0]),
            'Half-Elf'	:('M', 30, [0, 0, 0, 0, 0, 2]),
            'Half-Orc'	:('M', 30, [2, 0, 1, 0, 0, 0]),
            'Hobgoblin'	:('M', 30, [0, 0, 2, 1, 0, 0]),
            'Human'		:('M', 30, [1, 1, 1, 1, 1, 1]),
            'Kender'	:('S', 25, [0, 1, 0, 0, 0, 1]),
            'Kenku'		:('M', 30, [0, 2, 0, 0, 1, 0]),
            'Kobold'	:('S', 30, [-2, 2, 0, 0, 0, 0]),
            'Lizardfolk':('M', 30, [0, 0, 2, 0, 1, 0]),
            'Orc'		:('M', 30, [2, 0, 1,-2, 0, 0]),
            'Tabaxi'	:('M', 30, [0, 2, 0, 0, 0, 1]),
            'Tifling'	:('M', 30, [0, 0, 0, 1, 0, 2]),
            'Triton'	:('M', 30, [1, 0, 1, 0, 0, 1]),
            'Yuan-Ti'	:('M', 30, [0, 0, 0, 1, 0, 2]),
            }


# class name , hitdie
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


# name : AR , set or add,score Modifer addon
dItemsArmors = {
                    'No Armor'                      :(10,'s','DEX'),
                    'Light Armor Padded'            :(11,'s','DEX'),
                    'Light Armor Leather'           :(11,'s','DEX'),
                    'Light Armor Studded leather'   :(12,'s','DEX'),
                    'Medium Armor Hide'             :(12,'s','DEX'),
                    'Medium Armor Chain shirt'      :(13,'s','DEX'),
                    'Medium Armor Scale mail'       :(14,'s','DEX'),
                    'Medium Armor Breastplate'      :(14,'s','DEX'),
                    'Medium Armor Half plate'       :(15,'s','DEX'),
                    'Heavy Armor Ring mail'         :(14,'s',''),
                    'Heavy Armor Chain mail'        :(16,'s',''),
                    'Heavy Armor Splint'            :(17,'s',''),
                    'Heavy Armor Plate'             :(18,'s','')
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


dItemsShields = {
                    'No Sheild':(0,'a'),
                    'Bukler':(1,'a'),
                    'Wicker shield':(1,'a'),
                    'Wyvern Bone Shield':(2,'a'),
                    'Tower Shield':(3,'a')
                }


dItemsWeaponsMele = {
                        'Fist'          :('1d1'),
                        'Sword'         :('1d4'),
                        'Club'          :('1d4'),
                        'Dagger'        :('1d4'),
                        'Greatclub'     :('1d8'),
                        'Handaxe'       :('1d6'),
                        'Javelin'       :('1d6'),
                        'Light hammer'  :('1d4'),
                        'Mace'          :('1d6'),
                        'Quarterstaff'  :('1d6'),
                        'Sickle'        :('1d4'),
                        'Spear'         :('1d6'),
                        'Battleaxe'     :('1d8'),
                        'Flail'         :('1d8'),
                        'Glaive'        :('1d10'),
                        'Greataxe'      :('1d12'),
                        'Greatsword'    :('2d6'),
                        'Halberd'       :('1d10'),
                        'Lance'         :('1d12'),
                        'Longsword'     :('1d8'),
                        'Maul'          :('2d6'),
                        'Morningstar'   :('1d8'),
                        'Pike'          :('1d10'),
                        'Rapier'        :('1d8'),
                        'Scimitar'      :('1d6'),
                        'Shortsword'    :('1d6'),
                        'Trident'       :('1d6'),
                        'War pick'      :('1d8'),
                        'Warhammer'     :('1d8'),
                        'Whip'          :('1d4')
                        }

dItemsWeaponsRanged = {
                        'bow':('1d4')
                        }


dItemsHealingPotions = {
                        'Minor Healing'     :('2d4 + 2'),
                        'Greater healing'   :('4d4 + 4'),
                        'Superior healing'  :('8d4 + 8'),
                        'Supreme healing'   :('10d4 + 20')
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

# level:needed XP , Proficiency Bonus
dXPlevelUP = {
                1:  (0		, +2),
                2:  (300 	, +2),
                3:  (900 	, +2),
                4:  (2700 	, +2),
                5:  (6500 	, +3),
                6:  (14000 	, +3),
                7:  (23000 	, +3),
                8:  (34000 	, +3),
                9:  (48000 	, +4),
                10: (64000 	, +4),
                11: (85000 	, +4),
                12: (100000 , +4),
                13: (120000 , +5),
                14: (140000 , +5),
                15: (165000 , +5),
                16: (195000 , +5),
                17: (225000 , +6),
                18: (265000 , +6),
                19: (305000 , +6),
                20: (355000 , +6)
            }
# action number: (action name,hero useble , monster useble)
actions = {
            1: ("melee",    True,   True),
            2: ("ranged",   True,   True),
            3: ("hunt",     True,   True),
            4: ("flee",     True,   True),
            5: ("heal",     True,   False),
            6: ("get loot", True,   False),
            7: ("equip",    True,   False),
            8: ("unequip",  True,   False)
            }

############
# http://media.wizards.com/2016/downloads/DND/DMBasicRulesV05.pdf
############
# Challenge 0 (0-10 XP)
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

# Challenge 1/8 (25 XP)
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

# Challenge 1/4 (50 XP)
challenge_2 = [
                'Acolyte',
                'Axe Beak',
                'Blink Dog',
                'Boar',
                'Constrictor Snake',
                'Draft Horse',
                'Elk',
                'Flying Sword',
                'Giant Badger',
                'Giant Bat',
                'Giant Centipede',
                'Giant Frog',
                'Giant Lizard',
                'Giant Owl',
                'Giant Poisonous Snake',
                'Giant Wolf Spider',
                'Goblin',
                'Panther',
                'Pteranodon',
                'Riding Horse',
                'Skeleton',
                'Swarm of Bats',
                'Swarm of Rats',
                'Swarm of Ravens',
                'Wolf',
                'Zombie'
                ]

# Challenge 1/2 (100 XP)
challenge_3 = [
                'Ape',
                'Black Bear',
                'Cockatrice',
                'Crocodile',
                'Giant Goat',
                'Giant Sea Horse',
                'Giant Wasp',
                'Gnoll',
                'Hobgoblin',
                'Lizardfolk',
                'Orc',
                'Reef Shark',
                'Satyr',
                'Swarm of Insects',
                'Thug',
                'Warhorse',
                'Worg'
                ]

# Challenge 1 (200 XP)
challenge_4 = [
                'Animated Armor',
                'Brown Bear',
                'Bugbear',
                'Death Dog',
                'Dire Wolf',
                'Ghoul',
                'Giant Eagle',
                'Giant Hyena',
                'Giant Octopus',
                'Giant Spider',
                'Giant Toad',
                'Giant Vulture',
                'Harpy',
                'Hippogriff',
                'Lion',
                'Swarm of Quippers',
                'Tiger'
                ]

# Challenge 2 (450 XP)
challenge_5 = [
                'Allosaurus',
                'Awakened Tree',
                'Berserker',
                'Centaur',
                'Gargoyle',
                'Giant Boar',
                'Giant Constrictor Snake',
                'Giant Elk',
                'Grick',
                'Griffon',
                'Hunter Shark',
                'Nothic',
                'Ochre Jelly',
                'Ogre',
                'Pegasus',
                'Plesiosaurus',
                'Polar Bear',
                'Priest',
                'Rhinoceros',
                'Saber-toothed Tiger',
                'Swarm of Poisonous Snakes'
                ]

# Challenge 3 (700 XP)
challenge_6 = [
                'Ankylosaurus',
                'Basilisk',
                'Doppelganger',
                'Giant Scorpion',
                'Hell Hound',
                'Killer Whale',
                'Knight',
                'Manticore',
                'Minotaur',
                'Mummy',
                'Owlbear',
                'Phase Spider',
                'Spectator',
                'Werewolf',
                'Wight',
                'Winter Wolf',
                'Yeti'
                ]

# Challenge 4 (1',100 XP)
challenge_7 = [
                'Banshee',
                'Elephant',
                'Flameskull',
                'Ghost'
                ]

# Challenge 5 (1',800 XP)
challenge_8 = [
                'Air Elemental',
                'Earth Elemental',
                'Fire Elemental',
                'Flesh Golem',
                'Giant Crocodile',
                'Giant Shark',
                'Hill Giant',
                'Triceratops',
                'Troll',
                'Water Elemental'
                ]

# Challenge 6 (2',300 XP)
challenge_9 = [
                'Chimera',
                'Cyclops',
                'Mage',
                'Mammoth',
                'Medusa',
                'Wyvern'
                ]

# Challenge 7 (2',900 XP)
challenge_10 = ['Giant Ape']

# Challenge 8 (3',900 XP)
challenge_11 = [
                'Frost Giant',
                'Hydra',
                'Tyrannosaurus Rex',
                'Young Green Dragon'
                ]

# Challenge 9 (5',000 XP)
challenge_12 = ['Fire Giant']

# Challenge 10 (5,900 XP)
challenge_13 = ['Stone Golem']

# Challenge 17 (18,000 XP)
challenge_14 = ['Adult Red Dragon']

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

spelllist = {
1:["Absorb Elements", "Alarm", "Burning Hands", "Catapult", "Cause Fear", "Charm Person", "Chromatic Orb", "Color Spray", "Comprehend Languages",
"Detect Magic", "Disguise Self", "Earth Tremor", "Expeditious Retreat", "False Life", "Feather Fall", "Find Familiar", "Floating Disk", "Fog Cloud", "Grease",
"Hideous Laughter", "Ice Knife", "Identify", "Illusory Script", "Jump", "Longstrider", "Mage Armor", "Magic Missile", "Protection from Evil and Good", "Ray of Sickness",
"Shield", "Silent Image", "Sleep", "Snare", "Tasha’s Hideous Laughter", "Tenser’s Floating Disk", "Thunderwave", "Unseen Servant", "Witch Bolt"],

2: ["Acid Arrow", "Aganazzar’s Scorcher", "Alter Self", "Arcane Lock", "Arcanist's Magic Aura", "Blindness/Deafness", "Blur", "Cloud of Daggers",
"Continual Flame", "Crown of Madness", "Darkness", "Darkvision", "Detect Thoughts", "Dragon's Breath", "Dust Devil", "Earthbind",
"Enlarge/Reduce", "Flaming Sphere", "Flock of Familiars", "Gentle Repose", "Gust of Wind", "Hold Person", "Invisibility", "Knock", "Levitate",
"Locate Object", "Magic Mouth", "Magic Weapon", "Maximilian’s Earthen Grasp", "Melf’s Acid Arrow", "Mind Spike", "Mirror Image", "Misty Step",
"Nystul’s Magic Aura", "Phantasmal Force", "Pyrotechnics", "Ray of Enfeeblement", "Rope Trick", "Scorching Ray", "See Invisibility", "Shadow Blade",
"Shatter", "Skywrite", "Snilloc’s Snowball Swarm", "Spider Climb", "Suggestion", "Warding Wind", "Web"],

3: ["Animate Dead", "Bestow Curse", "Blink", "Catnap", "Clairvoyance", "Counterspell", "Dispel Magic", "Enemies Abound", "Erupting Earth",
"Fear", "Feign Death", "Fireball", "Flame Arrows", "Fly", "Galder’s Tower", "Gaseous Form", "Glyph of Warding", "Haste", "Hypnotic Pattern",
"Leomund’s Tiny Hut", "Life Transference", "Lightning Bolt", "Magic Circle", "Major Image", "Melf's Minute Meteors", "Nondetection", "Phantom Steed",
"Protection from Energy", "Remove Curse", "Sending", "Sleet Storm", "Slow", "Stinking Cloud", "Summon Lesser Demons", "Thunder Step",
"Tidal Wave", "Tiny Hut", "Tiny Servant", "Tongues", "Vampiric Touch", "Wall of Sand", "Wall of Water", "Water Breathing"],

4:["Arcane Eye", "Banishment", "Black Tentacles", "Blight", "Charm Monster", "Confusion", "Conjure Minor Elementals", "Control Water", "Dimension Door",
"Elemental Bane", "Evard’s Black Tentacles", "Fabricate", "Faithful Hound", "Fire Shield", "Galder’s Speedy Courier", "Greater Invisibility", "Hallucinatory Terrain",
"Ice Storm", "Leomund’s Secret Chest",  "Locate Creature", "Mordenkainen’s Faithful Hound", "Mordenkainen’s Private Sanctum", "Otiluke’s Resilient Sphere", "Phantasmal Killer",
"Polymorph", "Private Sanctum", "Resilient Sphere", "Secret Chest", "Sickening Radiance", "Stone Shape", "Stoneskin", "Storm Sphere", "Summon Greater Demon", "Vitriolic Sphere",
"Wall of Fire", "Watery Sphere"],

5:["Animate Objects",  "Arcane Hand", "Bigby's Hand", "Cloudkill", "Cone of Cold", "Conjure Elemental", "Contact Other Plane", "Control Winds", "Creation", "Danse Macabre", "Dawn",
"Dominate Person", "Dream",  "Enervation", "Far Step", "Geas",  "Hold Monster", "Immolation", "Infernal Calling", "Legend Lore", "Mislead", "Modify Memory", "Negative Energy Flood",
"Passwall", "Planar Binding", "Rary's Telepathic Bond", "Scrying", "Seeming", "Skill Empowerment", "Steel Wind Strike", "Synaptic Static", "Telekinesis", "Telepathic Bond", "Teleportation Circle",
"Transmute Rock", "Wall of Force", "Wall of Light", "Wall of Stone"],

6:["Arcane Gate", "Chain Lightning", "Circle of Death", "Contingency", "Create Homunculus", "Create Undead", "Disintegrate","Drawmij's Instant Summons", "Eyebite", "Flesh to Stone",
"Freezing Sphere", "Globe of Invulnerability", "Guards and Wards", "Instant Summons", "Investiture of Flame", "Investiture of Ice", "Investiture of Stone", "Investiture of Wind",
"Magic Jar", "Mass Suggestion", "Mental Prison", "Move Earth", "Otiluke's Freezing Sphere",  "Otto's Irresistible Dance", "Programmed Illusion", "Scatter", "Soul Cage", "Sunbeam",
"Tenser’s Transformation", "True Seeing", "Wall of Ice"],

7:[ "Crown of Stars", "Delayed Blast Fireball", "Etherealness", "Finger of Death", "Forcecage", "Magnificent Mansion", "Mirage Arcane", "Mordenkainen’s Sword", "Mordenkainen's Magnificent Mansion",
"Plane Shift", "Power Word Pain", "Prismatic Spray", "Project Image", "Reverse Gravity", "Sequester", "Simulacrum", "Symbol", "Teleport", "Whirlwind"],

8:["Abi-Dalzim’s Horrid Wilting", "Antimagic Field",  "Antipathy/Sympathy", "Clone", "Control Weather", "Demiplane", "Dominate Monster", "Feeblemind", "Illusory Dragon", "Incendiary Cloud",
"Maddening Darkness", "Maze", "Mighty Fortress", "Mind Blank", "Power Word Stun", "Sunburst", "Telepathy"],

9:["Astral Projection", "Foresight", "Gate", "Imprisonment", "Invulnerability", "Mass Polymorph", "Meteor Swarm", "Power Word Kill", "Prismatic Wall", "Psychic Scream", "Shapechange",
"Time Stop", "True Polymorph", "Weird", "Wish"]
}