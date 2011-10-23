import os
import json
from psrd.files import char_replace
from psrd.parse import construct_line, get_subtitle
from psrd.sections import set_section_text

def parse_simple_rules(book, details, name):
	retarr = []
	if len(details) == 0:
		return None
	section = {'name': name, 'type': 'section', 'source': book}
	set_section_text(section, [name], details)
	return section

def create_rules_filename(output, book, filename):
	title = char_replace(book) + "/rules/" + filename
	return os.path.abspath(output + "/" + title + ".json")

def write_rules(output, rules, book, filename):
	rules['source'] = book
	filename = create_rules_filename(output, book, filename)
	fp = open(filename, 'w')
	json.dump(rules, fp, indent=4)
	fp.close()

