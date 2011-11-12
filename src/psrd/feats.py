import os
import json
import re
from BeautifulSoup import BeautifulSoup
from psrd.rules import write_rules
from psrd.files import char_replace
from psrd.universal import parse_universal
from psrd.sections import ability_pass, is_anonymous_section, has_subsections, entity_pass

def adjust_core_pass(struct, filename):
	first = 3
	second = 6
	if filename in ('advancedFeats.html', 'ultimateMagicFeats.html'):
		first = 2
	fdesc = struct['sections'][first]
	special = fdesc['sections'][second - 2]
	table = special['sections'][0]
	del special['sections']
	fdesc['sections'].insert(second - 1, table)
	feats = fdesc['sections'][second:]
	del fdesc['sections'][second:]
	sections = struct['sections']
	struct = sections.pop(0)
	struct['sections'] = sections
	return struct, feats

def adjust_ultimate_combat_pass(struct):
	first = 3
	second = 6
	table = struct['sections'][2]['sections'][0]
	fdesc = struct['sections'][first]
	fdesc['sections'].insert(second - 1, table)
	del struct['sections'][2]
	feats = fdesc['sections'][second:]
	del fdesc['sections'][second:]
	sections = struct['sections']
	struct = sections.pop(0)
	struct['sections'] = sections
	return struct, feats

def adjust_feat_structure_pass(struct, filename):
	feats = []
	if filename in ('feats.html', 'advancedFeats.html', 'ultimateMagicFeats.html'):
		struct, feats = adjust_core_pass(struct, filename)
	elif filename in ('monsterFeats.html'):
		feats = struct['sections']
		del struct['sections']
	elif filename in ('ultimateCombatFeats.html'):
		struct, feats = adjust_ultimate_combat_pass(struct)
	return struct, feats

def feat_pass(feat):
	feat['type'] = 'feat'
	name = feat['name']
	m = re.search('(.*)\s*\((.*)\)', name)
	if m:
		newname = m.group(1).strip()
		types = m.group(2).split(", ")
		feat['name'] = newname
		feat['feat_types'] = types
	if not feat.has_key('text') and not feat.has_key('description'):
		for section in feat['sections']:
			if is_anonymous_section(section) and not has_subsections(section):
				feat['text'] = section['text']
				feat['sections'].remove(section)
	if feat.has_key('text') and not feat.has_key('description'):
		soup = BeautifulSoup(feat['text'])
		feat['description'] = ''.join(soup.findAll(text=True))
		del feat['text']

def parse_feats(filename, output, book):
	struct = parse_universal(filename, output, book)
	struct = entity_pass(struct)
	rules, feats = adjust_feat_structure_pass(struct, os.path.basename(filename))

	for feat in feats:
		feat_pass(feat)
		ability_pass(feat)

	for feat in feats:
		print "%s: %s" %(feat['source'], feat['name'])
		filename = create_feat_filename(output, book, feat)
		fp = open(filename, 'w')
		json.dump(feat, fp, indent=4)
		fp.close()
	if rules:
		write_rules(output, rules, book, "feats")

def create_feat_filename(output, book, feat):
	title = char_replace(book) + "/feats/" + char_replace(feat['name'])
	return os.path.abspath(output + "/" + title + ".json")

