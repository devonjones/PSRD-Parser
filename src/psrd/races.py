import os
import json
from psrd.files import char_replace
from psrd.universal import parse_universal
from psrd.sections import entity_pass

def race_pass(race):
	race['type'] = 'race'

def attribute_pass(race):
	traits = race['sections'][-1]
	attributes = traits['sections'][0]
	attributes['description'] = attributes['name']
	attributes['name'] = 'Attributes'

def parse_races(filename, output, book):
	struct = parse_universal(filename, output, book)
	struct = entity_pass(struct)
	for race in struct['sections']:
		race_pass(race)
		attribute_pass(race)

	for race in struct['sections']:
		print "%s: %s" %(race['source'], race['name'])
		filename = create_race_filename(output, book, race)
		fp = open(filename, 'w')
		json.dump(race, fp, indent=4)
		fp.close()

def create_race_filename(output, book, race):
	title = char_replace(book) + "/races/" + char_replace(race['name'])
	return os.path.abspath(output + "/" + title + ".json")

