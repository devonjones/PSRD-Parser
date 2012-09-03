import os
import json
from psrd.files import char_replace
from psrd.universal import parse_universal
from psrd.sections import entity_pass, quote_pass
from psrd.stat_block import stat_block_pass

def race_pass(race):
	race['type'] = 'race'
	race['subtype'] = 'standard_race'

def arg_race_pass(race, subtype):
	race['type'] = 'race'
	race['subtype'] = subtype
	return race

def racial_trait_pass(race):
	traits = race['sections'][-1]
	attributes = traits['sections'][0]
	attributes['description'] = attributes['name']
	attributes['name'] = 'Attributes'
	for trait in traits['sections']:
		trait['type'] = 'racial_trait'
		trait['subtype'] = race['name'].lower()

def parse_races(filename, output, book):
	struct = parse_universal(filename, output, book)
	struct = stat_block_pass(struct, book)
	struct = quote_pass(struct)
	struct = entity_pass(struct)
	for race in struct['sections']:
		race_pass(race)
		racial_trait_pass(race)
	for race in struct['sections']:
		write_race(output, book, race)

def arg_restructure(struct, book):
	race = struct['sections'][0]
	del struct['sections'][0]
	if race.has_key('sections'):
		desc = race['sections']
		race['sections'] = [{'name': 'Description', 'type': 'section', 'source': book, 'sections': desc}]
	else:
		race['sections'] = []
	race['sections'].extend(struct['sections'])
	return race

def parse_arg_core_race(filename, output, book):
	struct = parse_universal(filename, output, book)
	struct = stat_block_pass(struct, book)
	struct = quote_pass(struct)
	struct = entity_pass(struct)
	struct = arg_restructure(struct, book)
	race = arg_race_pass(struct, 'core_race')
	write_race(output, book, race)

def parse_arg_featured_race(filename, output, book):
	struct = parse_universal(filename, output, book)
	struct = stat_block_pass(struct, book)
	struct = quote_pass(struct)
	struct = entity_pass(struct)
	struct = arg_restructure(struct, book)
	race = arg_race_pass(struct, 'featured_race')
	write_race(output, book, race)

def parse_arg_uncommon_race(filename, output, book):
	struct = parse_universal(filename, output, book)
	struct = stat_block_pass(struct, book)
	struct = quote_pass(struct)
	struct = entity_pass(struct)
	struct = arg_restructure(struct, book)
	race = arg_race_pass(struct, 'uncommon_race')
	write_race(output, book, race)

def write_race(output, book, race):
	print "%s: %s" %(race['source'], race['name'])
	filename = create_race_filename(output, book, race)
	fp = open(filename, 'w')
	json.dump(race, fp, indent=4)
	fp.close()

def create_race_filename(output, book, race):
	title = char_replace(book) + "/races/" + char_replace(race['name'])
	return os.path.abspath(output + "/" + title + ".json")

