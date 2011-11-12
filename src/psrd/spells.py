import os
import json
from psrd.universal import parse_universal, print_struct
from psrd.sections import ability_pass, entity_pass
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

def parse_spell(filename, output, book):
	struct = parse_universal(filename, output, book, max_title=4)
	struct = stat_block_pass(struct, book)
	struct = heading_pass(struct)
	struct = entity_pass(struct)
	struct = ability_pass(struct)
	if struct['type'] == 'section':
		if struct.has_key('name'):
			write_rules(output, struct, book, struct['name'])
		else:
			parent = struct['sections'][0]
			for spell in struct['sections']:
				if spell != parent:
					spell['parent'] = parent['name']
				write_spell(output, book, spell)
	else:
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
