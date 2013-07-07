import os
import re
import json
from BeautifulSoup import BeautifulSoup
from psrd.files import char_replace
from psrd.stat_block import stat_block_pass, parse_section
from psrd.universal import parse_universal, print_struct, StatBlockHeading
from psrd.sections import ability_pass, entity_pass, find_section, find_all_sections, remove_section, quote_pass

def mark_subtype_pass(struct, name, subtype):
	s = find_section(struct, name=name)
	if s:
		for section in s['sections']:
			section['subtype'] = subtype
	return struct

def core_rulebook_structure_pass(rules, basename):
	if basename == 'glossary.html':
		c = find_section(rules, name="Conditions", section_type='section')
		for cond in c['sections']:
			cond['subtype'] = 'condition'
	elif basename == 'rods.html':
		newsections = []
		for section in rules['sections']:
			if section.__class__ == StatBlockHeading:
				newsections.append(parse_section(section, rules['source']))
			else:
				newsections.append(section)
		rules['sections'] = newsections
	return rules

def advanced_players_guide_structure_pass(rules, basename):
	if basename == 'advancedRaces.html':
		newsections = []
		racesections = []
		currparent = None
		isnew = True
		for section in rules['sections']:
			if section['name'] in ['Dwarves', 'Elves', 'Gnomes', 'Half-Elves', 'Half-Orcs', 'Halflings', 'Humans']:
				isnew = False
				currparent = section
				newsections.append(section)
				racesections = currparent.setdefault('sections', [])
			elif isnew:
				newsections.append(section)
			else:
				if section['name'] == 'Alternate Racial Traits':
					for trait in section['sections']:
						trait['type'] = 'racial_trait'
						trait['subtype'] = currparent['name'].lower()
				racesections.append(section)
			rules['sections'] = newsections
	elif basename == 'ranger.html':
		cl = rules['sections'][0]
		weap = find_section(rules, name='New Combat Styles')
		remove_section(rules, weap)
		newsec = []
		for section in weap['sections']:
			section['subtype'] = 'ranger_combat_style'
		last = weap['sections'][len(weap['sections']) -1]
		soup = BeautifulSoup(last['text'])
		last['text'] = unicode(soup.contents[0])
		newtext = ''.join([unicode(c) for c in soup.contents[1:]])
		newsec = {'type': 'section', 'source': rules['source'], 'text': newtext}
		weap['sections'].append(newsec)
		cl.setdefault('sections', []).append(weap)
	elif basename == 'cleric.html':
		subdomains = rules['sections'][1]
		for section in subdomains['sections']:
			if section['type'] == 'section':
				section['subtype'] = 'cleric_subdomain'
	elif basename == 'sorcerer.html':
		newsections = []
		cl = rules['sections'].pop(0)
		newsections.append(cl)
		arch = {'type': 'section', 'source': rules['source'], 'name': 'Sorcerer Bloodlines', 'sections': rules['sections']}
		for section in arch['sections']:
			section['subtype'] = 'sorcerer_bloodline'
		newsections.append(arch)
		rules['sections'] = newsections
	elif basename == 'wizard.html':
		rules = mark_subtype_pass(rules, "Elemental Arcane Schools", "elemental_arcane_school")
		rules = mark_subtype_pass(rules, "Focused Arcane Schools", "focused_arcane_school")
	if basename in ['barbarian.html', 'bard.html', 'druid.html', 'fighter.html', 'monk.html', 'paladin.html', 'ranger.html', 'rogue.html']:
		return ap_archetype_pass(rules)
	return rules

def ap_archetype_pass(rules):
	newsections = []
	cl = rules['sections'].pop(0)
	cl = mark_subtype_pass(cl, "Rage Powers (Ex)", "barbarian_rage_power")
	cl = mark_subtype_pass(cl, "Rogue Talents", "rogue_talent")
	cl = mark_subtype_pass(cl, "Advanced Rogue Talents", "rogue_advanced_talent")
	newsections.append(cl)
	arch = {'type': 'section', 'source': rules['source'], 'name': cl['name'] + ' Archetypes', 'sections': rules['sections']}
	newsections.append(arch)
	for section in arch['sections']:
		section['type'] = 'class_archetype'
		section['subtype'] = cl['name'].lower()
	rules['sections'] = newsections
	return rules

def ultimate_combat_structure_pass(rules, basename):
	if basename == 'classArchetypes.html':
		topsections = []
		newsections = []
		topsections.append(rules)
		top = {'type': 'section', 'source': rules['source'], 'name': 'Class Archetypes', 'sections': topsections}
		isnew = True
		for section in rules['sections']:
			if section['name'] == 'Using Archetypes':
				isnew = False
			if isnew:
				newsections.append(section)
			else:
				topsections.append(section)
		del rules['name']
		rules['sections'] = newsections
		return top
	return rules

def structure_pass(rules, basename, book):
	if book == 'Core Rulebook':
		return core_rulebook_structure_pass(rules, basename)
	elif book == "Advanced Player's Guide":
		return advanced_players_guide_structure_pass(rules, basename)
	#elif book == 'Ultimate Magic':
	#	return ultimate_magic_structure_pass(rules, basename)
	elif book == 'Ultimate Combat':
		return ultimate_combat_structure_pass(rules, basename)
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
	m = re.search('\s*\((.*?)\)', rules.get('name', ''))
	if m:
		name = re.sub('\s*\(%s\)' % m.group(1), '', rules['name']).strip()
		if name != '':
			rules['abbrev'] = m.group(1)
			rules['name'] = re.sub('\s*\(%s\)' % m.group(1), '', rules['name']).strip()
	for s in rules.get('sections', []):
		abbrev_pass(s)
	return rules

def parse_rules_no_sb(filename, output, book, title):
	return parse_rules(filename, output, book, title, no_sb=True)

def parse_rules(filename, output, book, title, no_sb=False):
	basename = os.path.basename(filename)
	rules = parse_universal(filename, output, book)
	rules = stat_block_pass(rules, book, no_sb=no_sb)
	rules = structure_pass(rules, basename, book)
	if not basename in ['glossary.html']:
		rules = ability_pass(rules)
	rules = title_pass(rules, book, title)
	rules = quote_pass(rules)
	rules = entity_pass(rules)
	if not basename in ['ranger.html', 'universalMonsterRules.html', 'buildingAndModifyingConstructs.html', 'spellbooks.html', 'rings.html', 'massCombat.html']:
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
