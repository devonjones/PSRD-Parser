import os
import json
import re
from BeautifulSoup import BeautifulSoup
from psrd.rules import write_rules
from psrd.files import char_replace
from psrd.universal import parse_universal, print_struct
from psrd.sections import ability_pass, is_anonymous_section, has_subsections, entity_pass

def core_structure_pass(section, filename):
	section['name'] = 'Spell Lists'
	sections = []
	spell_lists = []
	for s in section['sections']:
		if s['name'].endswith('Spells'):
			spell_lists.append(s)
		elif s['name'] != 'Spells by Class':
			sections.append(s)
	section['sections'] = sections
	return section, spell_lists

def advanced_structure_pass(section, filename):
	sections = []
	spell_lists = []
	top = section['sections'].pop(0)
	top['name'] = "Spell Lists"
	for s in section['sections']:
		if s['name'].endswith('Spells'):
			spell_lists.append(s)
	return top, spell_lists

def ultimate_magic_structure_pass(section, filename):
	section['sections'].pop(0)
	return None, section['sections']

def spell_list_structure_pass(section, filename):
	spell_lists = []
	if filename in ('spellLists.html'):
		section, spell_lists = core_structure_pass(section, filename)
	elif filename in ('advancedSpellLists.html', 'ultimateCombatSpellLists.html'):
		section, spell_lists = advanced_structure_pass(section, filename)
	elif filename in ('ultimateMagicSpellLists.html'):
		section, spell_lists = ultimate_magic_structure_pass(section, filename)
	else:
		del section['sections']
		print section
	return section, spell_lists

def spell_list_name_pass(spell_lists):
	retlists = []
	for casting_class in spell_lists:
		clname = casting_class['name']
		clname = clname.replace('Spells', '').strip()
		for sl in casting_class['sections']:
			sl['type'] = 'spell_list'
			sl['class'] = clname
			m = re.search('(\d)', sl['name'])
			sl['level'] = int(m.group(0))
			retlists.append(sl)
	return retlists

def spell_pass(spell_list):
	spells = []
	school = None
	descriptor = None
	school_type = True
	if spell_list['class'] in ['Elementalist Wizard']:
		school_type = False
	for s in spell_list['sections']:
		if s.has_key('sections'):
			if school_type:
				school = s['name']
			else:
				descriptor = s['name']
			for ss in s['sections']:
				soup = BeautifulSoup(ss['text'])
				spells.append(create_spell(ss['name'], soup, school, descriptor))
		else:
			soup = BeautifulSoup(s['text'])
			if ''.join(soup.findAll(text=True)) == '':
				if school_type:
					school = s['name']
				else:
					descriptor = s['name']
			else:
				spells.append(create_spell(s['name'], soup, school, descriptor))
	spell_list['spells'] = spells
	del spell_list['sections']
	return spell_list

def create_spell(name, soup, school=None, descriptor=None):
	if name.endswith(":"):
		name = name[:-1]
	comps = ""
	if soup.find('sup'):
		sup = soup.find('sup')
		comps = sup.renderContents()
		sup.replaceWith('')
	desc = ''.join(soup.findAll(text=True))
	if desc.startswith(":"):
		desc = desc[1:].strip()
	spell = {'name': name, 'description': desc}
	if len(comps) > 0:
		spell['material'] = list(comps)
	if school:
		spell['school'] = school
	if descriptor:
		spell['descriptor'] = descriptor
	return spell

def parse_spell_lists(filename, output, book):
	struct = parse_universal(filename, output, book)
	entity_pass(struct)
	rules, spell_lists = spell_list_structure_pass(struct, os.path.basename(filename))
	spell_lists = spell_list_name_pass(spell_lists)
	for spell_list in spell_lists:
		sl = spell_pass(spell_list)
		print "%s: %s" %(sl['source'], sl['name'])
		filename = create_spell_list_filename(output, book, sl)
		fp = open(filename, 'w')
		json.dump(sl, fp, indent=4)
		fp.close()
	if rules:
		write_rules(output, rules, book, "spell_lists")

def create_spell_list_filename(output, book, spell_list):
	title = char_replace(book) + "/spell_lists/" + char_replace(spell_list['class']) + "-" + unicode(spell_list['level'])
	return os.path.abspath(output + "/" + title + ".json")
