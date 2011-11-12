import os
import re
import json
from psrd.files import char_replace
from psrd.stat_block import stat_block_pass
from psrd.universal import parse_universal, print_struct
from psrd.sections import ability_pass, entity_pass, find_section

def structure_pass(rules, basename):
	if basename == 'glossary.html':
		c = find_section(rules, name="Conditions", section_type='section')
		for cond in c['sections']:
			cond['subtype'] = 'condition'
	return rules

def title_pass(rules, book, title):
	if not rules.has_key('name'):
		rules['name'] = title
		return rules
	elif title == rules['name']:
		return rules
	else:
		return {'type': 'section', 'source': book, 'name': title, 'sections': [rules]}

def abbrev_pass(rules):
	m = re.search('\s*\((.*)\)', rules.get('name', ''))
	if m:
		name = re.sub('\s*\(%s\)' % m.group(1), '', rules['name']).strip()
		if name != '':
			rules['abbrev'] = m.group(1)
			rules['name'] = re.sub('\s*\(%s\)' % m.group(1), '', rules['name']).strip()
	for s in rules.get('sections', []):
		abbrev_pass(s)
	return rules

def parse_rules(filename, output, book, title):
	basename = os.path.basename(filename)
	rules = parse_universal(filename, output, book)
	rules = stat_block_pass(rules, book)
	if not basename == 'glossary.html':
		rules = ability_pass(rules)
	rules = entity_pass(rules)
	rules = title_pass(rules, book, title)
	rules = structure_pass(rules, basename)
	rules = abbrev_pass(rules)
	print_struct(rules)
	print "%s: %s" %(rules['source'], rules['name'])
	write_rules(output, rules, book, title)

def write_rules(output, rules, book, filename):
	filename = create_rules_filename(output, book, filename)
	fp = open(filename, 'w')
	json.dump(rules, fp, indent=4)
	fp.close()

def create_rules_filename(output, book, filename):
	title = char_replace(book) + "/rules/" + char_replace(filename)
	return os.path.abspath(output + "/" + title + ".json")
