import os
import json
from psrd.universal import parse_universal, print_struct
from psrd.sections import ability_pass, entity_pass, cap_words
from psrd.rules import write_rules
from psrd.stat_block import stat_block_pass
from psrd.files import char_replace

def heading_pass(struct):
	spell = None
	sections = []
	spells = []
	if struct['type'] == 'section' and struct.has_key('sections'):
		for child in struct['sections']:
			if child['type'] == 'spell':
				if spell:
					if len(sections) > 0:
						s = spell.setdefault('sections', [])
						s.extend(sections)
				spell = child
				spells.append(spell)
				sections = []
			else:
				sections.append(child)
		if len(sections) > 0:
			s = spell.setdefault('sections', [])
			s.extend(sections)
		if len(spells) == 1:
			return spells[0]
	return struct

def parent_pass_in_file(struct):
	parent = struct['sections'][0]
	for spell in struct['sections']:
		if spell != parent:
			spell['parent'] = cap_words(parent['name'])
		if spell['name'].find(",") > -1:
			parts = spell['name'].split(",")
			spell['parent'] = cap_words(parts[0].strip())

def parent_pass_out_of_file(spell):
	if spell['name'].find(",") > -1:
		parts = spell['name'].split(",")
		spell['parent'] = cap_words(parts[0].strip())

def cap_pass(spell):
	spell['name'] = cap_words(spell['name'])
	if not spell.has_key('level'):
		print "WTF: level %s %s" % (spell['name'], spell.keys())
	for level in spell.get('level', []):
		level['class'] = cap_words(level['class'])

def misc_fix_pass(spell):
	if spell['name'] == 'Shadowbard':
		spell['school'] = 'illusion'
		spell['subschool'] = 'shadow'
		spell['descriptor'] = ['shadow']
	elif spell['name'] == "Curse, Major":
		spell['parent'] = "Bestow Curse"
	elif spell['name'] in ("Acid Pit", "Hungry Pit", "Spiked Pit"):
		spell['parent'] = "Create Pit"
	elif spell['name'] in ("Evolution Surge", "Evolution Surge, Greater"):
		spell['parent'] = "Evolution Surge, Lesser"
	elif spell['name'] == "Evolution Surge, Lesser":
		del spell['parent']
	elif spell['name'] == "Flare Burst":
		spell['paremt'] = "Flare"
	elif spell['name'] == "Geas, Lesser":
		del spell['parent']
	elif spell['name'] in ("Rejuvenate Eidolon", "Rejuvenate Eidolon, Greater"):
		spell['parent'] = "Rejuvenate Eidolon, Lesser"
	elif spell['name'] == "Rejuvenate Eidolon, Lesser":
		del spell['parent']
	elif spell['name'] == "Shared Wrath":
		spell['paremt'] = "Wrath"
	elif spell['name'] == "Tireless Pursuers":
		spell['parent'] = "Tireless Pursuit"
	elif spell['name'] in ("Crushing Hand", "Forceful Hand", "Grasping Hand"):
		spell['parent'] = "Interposing Hand"
	elif spell['name'] == "Deeper Darkness":
		spell['parent'] = "Darkness"
	elif spell['name'] == "Identify":
		spell['parent'] = "Detect Magic"
	elif spell['name'] == "Make Whole":
		spell['parent'] = "Mending"
	elif spell['name'] in ("Age Resistance", "Age Resistance, Greater"):
		spell['parent'] = "Age Resistance, Lesser"
	elif spell['name'] == "Age Resistance, Lesser":
		del spell['parent']
	elif spell['name'] == "Cackling Skull":
		spell['parent'] = "Magic Mouth"
	elif spell['name'] == "Call Construct":
		spell['parent'] = "Instant Summons"
	elif spell['name'] in ("Create Demiplane", "Create Demiplane, Greater"):
		spell['parent'] = "Create Demiplane, Lesser"
	elif spell['name'] == "Create Demiplane, Lesser":
		del spell['parent']
	elif spell['name'] == "Dance of a Thousand Cuts":
		spell['parent'] = "Dance Of A Hundred Cuts"
	elif spell['name'] == "Disguise Other":
		spell['parent'] = "Disguise Self"
	elif spell['name'] in ("Ice Crystal Teleport", "Interplanetary Teleport"):
		spell['parent'] = "Teleport"
	elif spell['name'] == "Miserable Pity":
		spell['parent'] = "Sanctuary"
	elif spell['name'] == "Possess Object":
		spell['parent'] = "Magic Jar"
	elif spell['name'] == "Rain of Frogs":
		spell['parent'] = "Summon Swarm"
	elif spell['name'] == "Raise Animal Companion":
		spell['parent'] = "Raise Dead"
	elif spell['name'] == "Ray of Sickening":
		spell['parent'] = "Ray Of Exhaustion"
	elif spell['name'] == "Restore Eidolon":
		spell['parent'] = "Restoration"
	elif spell['name'] == "Restore Eidolon, Lesser":
		spell['parent'] = "Restoration, Lesser"
	elif spell['name'] == "Summon Elder Worm":
		spell['parent'] = "Summon Nature's Ally VIII"
	elif spell['name'] == "Summon Froghemoth":
		spell['parent'] = "Summon Nature's Ally IX"
	elif spell['name'] == "Summon Minor Ally":
		spell['parent'] = "Summon Nature's Ally I"
	elif spell['name'] == "Summon Minor Monster":
		spell['parent'] = "Summon Monster I"
	elif spell['name'] in ("Symbol of Healing", "Symbol of Mirroring", "Symbol of Revelation", "Symbol of Scrying", "Symbol of Strife", "Symbol of Vulnerability"):
		spell['parent'] = "Symbol Of Death"
	elif spell['name'] == "Unholy Ice":
		spell['parent'] = "Holy Ice"

def parse_spell(filename, output, book):
	struct = parse_universal(filename, output, book, max_title=4)
	struct = stat_block_pass(struct, book)
	struct = heading_pass(struct)
	#struct = entity_pass(struct)
	struct = ability_pass(struct)
	if struct['type'] == 'section':
		if struct.has_key('name'):
			write_rules(output, struct, book, struct['name'])
		else:
			parent_pass_in_file(struct)
			for spell in struct['sections']:
				misc_fix_pass(spell)
				cap_pass(spell)
				write_spell(output, book, spell)
	else:
		parent_pass_out_of_file(struct)
		misc_fix_pass(struct)
		cap_pass(struct)
		write_spell(output, book, struct)

def write_spell(output, book, spell):
	print "%s: %s" %(spell['source'], spell['name'])
	filename = create_spell_filename(output, book, spell)
	fp = open(filename, 'w')
	json.dump(spell, fp, indent=4)
	fp.close()

def create_spell_filename(output, book, spell):
	title = char_replace(book) + "/spells/" + char_replace(spell['name'])
	return os.path.abspath(output + "/" + title + ".json")
