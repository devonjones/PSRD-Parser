import os
import json
from BeautifulSoup import BeautifulSoup
from psrd.universal import parse_universal, print_struct
from psrd.sections import ability_pass, entity_pass, cap_words, find_section, find_all_sections, remove_section
from psrd.rules import write_rules
from psrd.stat_block import stat_block_pass
from psrd.files import char_replace, makedirs
from psrd.races import write_race

def structural_pass(struct):
	for child in struct.get('sections', []):
		if child.get('name', '').strip().endswith('Characters'):
			child['type'] = 'race'
			child['subtype'] = 'monster_race'
		else:
			structural_pass(child)
	return struct

def animal_companion_pass(struct):
	newsections = []
	for section in struct.get('sections', []):
		if section.get('name', '').endswith('Companion') or section.get('name', '').endswith('Companions'):
			name = section['name'].replace(' Animal Companion', '')
			name = name.replace(' Companions', '')
			nsec = section['sections'].pop(0)
			nsec['name'] = name
			nsec['sections'] = section['sections']
			animalsec = newsections[-1].setdefault('sections', [])
			animalsec.append(nsec)
		else:
			newsections.append(animal_companion_pass(section))
	struct['sections'] = newsections
	return struct

def familiar_pass(rules, basename):
	if basename in ['familiar.html', 'newFamiliars.html']:
		creatures = find_all_sections(rules, section_type='creature')
		for creature in creatures:
			creature['subtype'] = 'familiar'
	return rules

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
	basename = os.path.basename(filename)
	struct = parse_universal(filename, output, book, max_title=4)
	struct = stat_block_pass(struct, book)
	struct = animal_companion_pass(struct)
	struct = rule_pass(struct)
	struct = ability_pass(struct)
	struct = familiar_pass(struct, basename)
	currrules = []
	if struct['type'] == 'section':
		struct['name'] = struct['sections'][0]['name']
		write_creature(output, book, struct)
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
