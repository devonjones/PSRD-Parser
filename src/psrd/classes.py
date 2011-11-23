import os
import json
import re
from BeautifulSoup import BeautifulSoup
from psrd.rules import write_rules
from psrd.files import char_replace
from psrd.universal import parse_universal, print_struct, StatBlockHeading, StatBlockSection
from psrd.sections import ability_pass, entity_pass, find_section, find_all_sections, add_section, remove_section, cap_words
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
			domain['subtype'] = 'cleric_domain'
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
			bloodline['subtype'] = 'sorcerer_bloodline'
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
			school['subtype'] = 'arcane_school'
			remove_section(struct, school)
			add_section(s, school)
	return struct

def mark_subtype_pass(struct, name, section_type, subtype):
	s = find_section(struct, name=name, section_type=section_type)
	if s:
		for section in s['sections']:
			section['subtype'] = subtype
	return struct

def core_class_pass(struct):
	struct['subtype'] = 'core'
	return struct
	
def npc_class_pass(struct):
	struct['subtype'] = 'npc'
	return struct
	
def base_class_pass(struct):
	struct['subtype'] = 'base'
	return struct
	
def prestige_class_pass(struct):
	struct['subtype'] = 'prestige'
	return struct
	
def class_pass(struct):
	struct['type'] = 'class'
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

def anon_pass(cl):
	if not cl.has_key('name'):
		sections = cl['sections']
		top = sections.pop(0)
		top['sections'].extend(sections)
		return top
	return cl

def spell_list_pass(cl):
	field_dict = {
		"Alchemist": "Alchemist Formulae",
		"Inquisitor": "Inquisitor Spells",
		"Witch": "Witch Spells",
		"Summoner": "Summoner Spells",
		"Magus": "Magus Spell List"
	}
	if cl['name'] in field_dict.keys():
		name = field_dict[cl['name']]
		sl = find_section(cl, name=name, section_type='section')
		sections = sl['sections']
		for section in sections:
			section['type'] = 'spell_list'
			section['class'] = cl['name']
			m = re.search('(\d)', section['name'])
			section['level'] = int(m.group(0))
			soup = BeautifulSoup(section['text'])
			text = ''.join(soup.findAll(text=True))
			text = text.replace('&mdash;', '')
			text = text.replace('*', '')
			text = text.replace('.', '')
			del section['text']
			spells = []
			section['spells'] = spells
			for spell_name in text.split(", "):
				spell_name = spell_name.strip()
				spell_name = cap_words(spell_name)
				spell_name = spell_name.replace(" (Mass)", ", Mass")
				spell_name = spell_name.replace(" (Greater)", ", Greater")
				spell_name = spell_name.replace(" (Lesser)", ", Lesser")
				spell_name = spell_name.replace("Topoison", "To Poison")
				spells.append({"name": spell_name})
	return cl

def parse_class(cl, book):
	cl = stat_block_pass(cl, book)
	cl = class_pass(cl)
	cl = domain_pass(cl)
	cl = bloodline_pass(cl)
	cl = arcane_school_pass(cl)
	cl = ability_pass(cl)
	cl = mark_subtype_pass(cl, "Discovery", "ability", "alchemist_discovery")
	cl = mark_subtype_pass(cl, "Rage Powers", "ability", "barbarian_rage_power")
	cl = mark_subtype_pass(cl, "Bardic Performance", "section", "bardic_performance")
	cl = mark_subtype_pass(cl, "Deeds", "section", "gunslinger_deed")
	cl = mark_subtype_pass(cl, "Magus Arcana", "section", "magus_arcana")
	cl = mark_subtype_pass(cl, "Ninja Tricks", "section", "ninja_trick")
	cl = mark_subtype_pass(cl, "Oracle's Curse", "section", "oracle_curse")
	cl = mark_subtype_pass(cl, "Mysteries", "section", "oracle_mystery")
	cl = mark_subtype_pass(cl, "Rogue Talents", "section", "rogue_talent")
	cl = mark_subtype_pass(cl, "1-Point Evolutions", "section", "summoner_evolution_1")
	cl = mark_subtype_pass(cl, "2-Point Evolutions", "section", "summoner_evolution_2")
	cl = mark_subtype_pass(cl, "3-Point Evolutions", "section", "summoner_evolution_3")
	cl = mark_subtype_pass(cl, "4-Point Evolutions", "section", "summoner_evolution_4")
	cl = mark_subtype_pass(cl, "Cavalier Orders", "section", "warrior_order")
	cl = mark_subtype_pass(cl, "Samurai Orders", "section", "warrior_order")
	cl = mark_subtype_pass(cl, "Hex", "section", "witch_hex")
	cl = mark_subtype_pass(cl, "Major Hex", "section", "witch_major_hex")
	cl = mark_subtype_pass(cl, "Grand Hex", "section", "witch_grand_hex")
	cl = mark_subtype_pass(cl, "Patron Spells", "section", "witch_patron")
	cl = spell_list_pass(cl)
	cl = entity_pass(cl)
	return cl

def first_pass(filename, output, book):
	struct = parse_universal(filename, output, book)
	return struct

def parse_core_classes(filename, output, book):
	struct = first_pass(filename, output, book)
	struct = structural_pass(struct, os.path.basename(filename))
	core_class = parse_class(struct, book)
	core_class = core_class_pass(core_class)
	write_class(filename, output, book, core_class)

def parse_npc_classes(filename, output, book):
	struct = first_pass(filename, output, book)
	for n_class in struct['sections']:
		n_class = parse_class(n_class, book)
		n_class = npc_class_pass(n_class)
		write_class(filename, output, book, n_class)

def parse_base_classes(filename, output, book):
	struct = first_pass(filename, output, book)
	struct = anon_pass(struct)
	b_class = parse_class(struct, book)
	b_class = base_class_pass(b_class)
	write_class(filename, output, book, b_class)

def parse_prestige_classes(filename, output, book):
	struct = first_pass(filename, output, book)
	struct = anon_pass(struct)
	p_class = parse_class(struct, book)
	p_class = prestige_class_pass(p_class)
	write_class(filename, output, book, p_class)

def write_class(filename, output, book, cl):
	print "%s: %s" %(cl['source'], cl['name'])
	filename = create_class_filename(output, book, cl)
	fp = open(filename, 'w')
	json.dump(cl, fp, indent=4)
	fp.close()

def create_class_filename(output, book, cl):
	title = char_replace(book) + "/classes/" + char_replace(cl['name'])
	return os.path.abspath(output + "/" + title + ".json")

