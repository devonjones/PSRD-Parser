import os
import json
from BeautifulSoup import BeautifulSoup
from psrd.universal import parse_universal, print_struct
from psrd.sections import ability_pass, entity_pass, cap_words
from psrd.rules import write_rules
from psrd.stat_block import stat_block_pass
from psrd.files import char_replace, makedirs
from psrd.races import write_race

def monster_structural_pass(struct):
	sections = []
	changed = False
	for child in struct.get('sections', []):
		sections.append(child)
		if child['type'] == 'creature':
			changed = True
			child['name'] = struct['name']
			soup = BeautifulSoup(struct['text'])
			child['description'] = ''.join(soup.findAll(text=True))
		elif child.get('name', '').strip().endswith('Characters'):
			changed = True
			child['type'] = 'race'
			child['subtype'] = 'monster_race'
	if changed:
		return {'type': 'section', 'sections': sections, 'source': struct['source']}
	else:
		return struct

def structural_pass(struct):
	if struct.has_key('name'):
		# Single monster
		struct = monster_structural_pass(struct)
	else:
		# Multiple Monsters
		newsections = []
		for child in struct['sections']:
			newstruct = monster_structural_pass(child)
			if child == newstruct:
				newsections.append(child)
			else:
				newsections.extend(newstruct['sections'])
		struct['sections'] = newsections
	return struct

def animal_companion_pass(struct):
	newsections = []
	for section in struct['sections']:
		if section.get('name', '').endswith('Companion') or section.get('name', '').endswith('Companions'):
			name = section['name'].replace(' Animal Companion', '')
			name = name.replace(' Companions', '')
			nsec = section['sections'].pop(0)
			nsec['name'] = name
			nsec['sections'] = section['sections']
			animalsec = newsections[-1].setdefault('sections', [])
			animalsec.append(nsec)
		else:
			newsections.append(section)
	struct['sections'] = newsections
	return struct

def rule_pass(struct):
	newsections = []
	last_creature = None
	for section in struct['sections']:
		if section['type'] == 'creature':
			newsections.append(section)
			last_creature = section
		else:
			if not last_creature:
				newsections.append(section)
			else:
				csec = last_creature.setdefault('sections', [])
				csec.append(section)
	struct['sections'] = newsections
	return struct

def parse_creature(filename, output, book):
	struct = parse_universal(filename, output, book, max_title=4)
	struct = stat_block_pass(struct, book)
	struct = structural_pass(struct)
	struct = animal_companion_pass(struct)
	struct = rule_pass(struct)
	print_struct(struct)
	struct = ability_pass(struct)
	if struct['type'] == 'section':
		for child in struct['sections']:
			if child['type'] == 'creature':
				write_creature(output, book, child)
			elif child['type'] == 'race':
				makedirs(output, book, 'races')
				write_race(output, book, child)
			else:
				write_rules(output, child, book, child['name'])
	else:
		raise Exception("Uh Oh")

def write_creature(output, book, creature):
	print "%s: %s" %(creature['source'], creature['name'])
	filename = create_creature_filename(output, book, creature)
	fp = open(filename, 'w')
	json.dump(creature, fp, indent=4)
	fp.close()

def create_creature_filename(output, book, creature):
	title = char_replace(book) + "/creatures/" + char_replace(creature['name'])
	return os.path.abspath(output + "/" + title + ".json")
