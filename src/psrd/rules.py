import os
import json
from psrd.files import char_replace
from psrd.parse import construct_line, get_subtitle

def parse_simple_rules(rules, subject):
	retarr = []
	if len(rules) == 0:
		return None
	for field in rules:
		retarr.append(unicode(field))
	return {'name': subject, 'type': 'section', 'text': u''.join(retarr).strip()}

def create_rules_filename(output, book, filename):
	title = char_replace(book) + "/rules/" + filename
	return os.path.abspath(output + "/" + title + ".json")

def write_rules(output, rules, book, filename):
	rules['source'] = book
	filename = create_rules_filename(output, book, filename)
	fp = open(filename, 'w')
	json.dump(rules, fp, indent=4)
	fp.close()

