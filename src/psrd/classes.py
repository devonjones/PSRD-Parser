import os
import json
import re
from BeautifulSoup import BeautifulSoup
from psrd.rules import write_rules
from psrd.files import char_replace
from psrd.universal import parse_universal, print_struct, StatBlockHeading, StatBlockSection
from psrd.sections import ability_pass, entity_pass, find_section, find_all_sections, add_section, remove_section
from psrd.stat_block import stat_block_pass

def druid_animal_companion_fix(section):
	tuples = section.keys
	keys = []
	details = []
	s = section
	for tup in tuples:
		if tup[0] == 'Starting Statistics':
			pass
		elif tup[0] in ('4th-Level Advancement', '7th-Level Advancement'):
			s.keys = keys
			keys = []
			if s != section:
				details.append(s)
			s = StatBlockSection(tup[0])
		else:
			keys.append(tup)
	s.keys = keys
	if s != section:
		details.append(s)
	section.details = details
	return section

def druid_structural_pass(section):
	if section.has_key('sections'):
		newsections = []
		for s in section['sections']:
			if s.__class__ == StatBlockHeading:
				newsections.append(druid_animal_companion_fix(s))
			elif s.__class__ == dict:
				newsections.append(druid_structural_pass(s))
			else:
				newsections.append(s)
		section['sections'] = newsections
	return section
	
def structural_pass(struct, filename):
	if filename in ('druid.html'):
		struct = druid_structural_pass(struct)
	cs = find_section(struct, name="Class Skills", section_type='section')
	table = find_section(cs, name=struct['name'], section_type='table')
	idx = struct['sections'].index(cs)
	while table:
		idx = idx + 1
		if table:
			remove_section(struct, table)
			struct['sections'].insert(idx, table)
		table = find_section(cs, name=struct['name'], section_type='table')
	return struct

def domain_pass(struct):
	d = find_section(struct, name="Domains", section_type='section')
	if d:
		domains = find_all_sections(struct, name=re.compile('^.*Domain$'), section_type='section')
		for domain in domains:
			remove_section(struct, domain)
			add_section(d, domain)
	return struct

def bloodline_pass(struct):
	s = find_section(struct, name="Sorcerer Bloodlines", section_type='section')
	if s:
		collect = False
		bloodlines = []
		for section in struct['sections']:
			if collect:
				bloodlines.append(section)
			elif s == section:
				collect = True
		for bloodline in bloodlines:
			remove_section(struct, bloodline)
			add_section(s, bloodline)
	return struct

def arcane_school_pass(struct):
	s = find_section(struct, name="Arcane Schools", section_type='section')
	if s:
		collect = False
		schools = []
		for section in struct['sections']:
			if section.get('name') == 'Familiars':
				collect = False
			elif collect:
				schools.append(section)
			elif s == section:
				collect = True
		for school in schools:
			remove_section(struct, school)
			add_section(s, school)
	return struct
	
def core_class_pass(struct):
	struct['type'] = 'class'
	struct['class_type'] = 'core'
	align = find_section(struct, name="Alignment", section_type='section')
	if align:
		remove_section(struct, align)
		soup = BeautifulSoup(align['text'])
		struct['alignment'] = ''.join(soup.findAll(text=True))
	hd = find_section(struct, name="Hit Die", section_type='section')
	if hd:
		remove_section(struct, hd)
		soup = BeautifulSoup(hd['text'])
		hit = ''.join(soup.findAll(text=True))
		if hit.endswith("."):
			hit = hit[:-1]
		struct['hit_dice'] = hit
	return struct

def parse_core_classes(filename, output, book):
	struct = parse_universal(filename, output, book)
	struct = structural_pass(struct, os.path.basename(filename))
	struct = stat_block_pass(struct, book)
	core_class = core_class_pass(struct)
	core_class = domain_pass(core_class)
	core_class = bloodline_pass(core_class)
	core_class = arcane_school_pass(core_class)
	core_class = ability_pass(core_class)
	core_class = entity_pass(core_class)
	print "%s: %s" %(core_class['source'], core_class['name'])
	filename = create_core_class_filename(output, book, core_class)
	fp = open(filename, 'w')
	json.dump(core_class, fp, indent=4)
	fp.close()


def create_core_class_filename(output, book, core_class):
	title = char_replace(book) + "/core_classes/" + char_replace(core_class['name'])
	return os.path.abspath(output + "/" + title + ".json")
