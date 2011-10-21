import os
import re
import json
from BeautifulSoup import BeautifulSoup
from psrd.files import char_replace
from psrd.warnings import WarningReporting
from psrd.parse import construct_line, construct_stripped_line, get_subtitle
from psrd.tables import parse_tables, parse_table, write_tables, print_tables

def parse_function(field):
	functions = {
		'description': simple_closure('description'),
		'role': simple_closure('role'),
		'alignment': simple_closure('alignment'),
		'hit die': simple_closure('hit_die'),
		'class skills': parse_class_skills,
		'skill ranks per level': simple_closure('skill_ranks_per_level'),
	}
	field = field.strip()
	field = field.replace(":", '')
	return functions[field.lower()]

def simple_closure(field):
	def fxn(pcclass, contents):
		pcclass[field] = construct_stripped_line(contents)
	return fxn

def parse_level_table(pcclass, table):
	pass

def parse_spell_table(pcclass, table):
	pass

def parse_class_skills(pcclass, rows):
	text = construct_stripped_line(rows)
	cs = pcclass.setdefault('class_skills', {})
	cs['text'] = text
	skills = text.split('class skills are ')[1].split(", ")
	cs['skills'] = [clean_class_skill(skill) for skill in skills]

def clean_class_skill(skill):
	if skill[0:4] == "and ":
		skill = skill[4:].strip()
	if skill[-1] == '.':
		skill = skill[0:-1]
	m = re.search('([ a-zA-Z]*) \(([a-zA-Z]*)\)', skill)
	return {'name': m.group(1), 'attribute': m.group(2)}

def filter_ability_type(section, texts):
	for text in texts[0:3]:
		if text.strip().endswith('(Sp)'):
			section['type'] = 'Ability'
			section['ability_type'] = 'Special'
		elif text.strip().endswith('(Su)'):
			section['type'] = 'Ability'
			section['ability_type'] = 'Supernatural'
		elif text.strip().endswith('(Ex)'):
			section['type'] = 'Ability'
			section['ability_type'] = 'Extraordinary'
		elif text.strip().endswith('(Ex or Sp)'):
			section['type'] = 'Ability'
			section['ability_type'] = 'Extraordinary or Special'

def parse_section(section, rows, context):
	field = None
	bold = None
	subrows = []
	subsection = None
	for row in rows:
		if hasattr(row, 'name'):
			data = row.contents[0]
			if hasattr(data, 'name') and data.name in ['b', 'i']:
				if bold == None:
					if data.name == 'b':
						bold = True
					else:
						bold = False
				if (bold and data.name == 'b') or not bold:
					if not field:
						section['text'] = construct_stripped_line(subrows)
					elif subsection:
						newc = list(context)
						newc.append(subsection['name'])
						s = section.setdefault('sections', [])
						s.append(parse_section(subsection, subrows, newc))
					text = row.findAll(text=True)
					field = text[0].strip()
					subsection = {'name': field}
					subrows = ["<p>" + construct_stripped_line(row.contents[1:]) + "</p>"]
					filter_ability_type(subsection, text) 
				else:
					subrows.append(row)
			elif row.name == 'table':
				table = parse_table(row, context)
				subrows.append(unicode(table))
			else:
				subrows.append(row)
		else:
			subrows.append(row)
	if not field:
		section['text'] = construct_line(rows)
	elif subsection:
		newc = list(context)
		newc.append(subsection['name'])
		s = section.setdefault('sections', [])
		s.append(parse_section(subsection, subrows, newc))
	return section

def parse_core_class_body(div):
	core_class = {}
	rows = []
	field = None
	subfield = None
	special_h2 = False
	header = True
	section = None
	subsection = None
	for tag in div.contents:
		if unicode(tag).strip() != '':
			if header:
				if tag.name == 'h1':
					core_class['name'] = ''.join(tag.findAll(text=True)).strip()
				elif tag.name == 'h2' and ''.join(tag.findAll(text=True)).strip() == 'Class Features':
					field = 'Class Features'
					section = {'name': field}
					header = False
				elif tag.name == 'h2' and ''.join(tag.findAll(text=True)).strip() == 'Class Skills':
					parse_function(field)(core_class, rows)
					rows = []
					field = 'Class Skills'
				elif hasattr(tag.contents[0], 'name') and tag.contents[0].name == 'b':
					if not field:
						field = 'description'
					parse_function(field)(core_class, rows)
					field = ''.join(tag.contents[0].findAll(text=True))
					rows = [construct_stripped_line(tag.contents[1:])]
				elif tag.name == 'table':
					if field:
						parse_function(field)(core_class, rows)
						field = None
						rows = []
					level_table = parse_table(tag, ["Classes"])
					sections = core_class.setdefault('sections', [])
					sections.append(level_table)
					parse_level_table(core_class, level_table)
				elif tag.name == 'div' and tag.findAll(text=False)[0].name == 'table':
					table = tag.findAll(text=False)[0]
					spell_table = parse_table(table, ["Classes"])
					sections = core_class.setdefault('sections', [])
					sections.append(spell_table)
					parse_spell_table(core_class, spell_table)
				else:
					rows.append(tag)
			else:
				if tag.name == 'h2':
					text = ''.join(tag.findAll(text=True))
					if text in ['Sorcerer Bloodlines', 'Domains', 'Arcane Schools']:
						special_h2 = True
					elif text in ['Familiars']:
						special_h2 = False
					if special_h2:
						if not subfield:
							sections = core_class.setdefault('sections', [])
							sections.append(parse_section(section, rows, ["Classes", core_class['name'], section['name']]))
							field = text
							section = {'name': field}
							rows = []
						else:
							s = section.setdefault('sections', [])
							s.append(parse_section(subsection, rows, ["Classes", core_class['name'], section['name'], subsection['name']]))
							rows = []
						subfield = text
						subsection = {'name': text}
					else:
						sections = core_class.setdefault('sections', [])
						sections.append(parse_section(section, rows, ["Classes", core_class['name'], section['name']]))
						rows = []
						field = text
						section = {'name': field}
				else:
					rows.append(tag)
	sections = core_class.setdefault('sections', [])
	sections.append(parse_section(section, rows, ["Classes", core_class['name'], section['name']]))
	return core_class


def parse_core_classes(filename, output, book):
	WarningReporting().book = book
	fp = open(filename)
	try:
		soup = BeautifulSoup(fp)
		divs = soup.findAll('div')
		for div in divs:
			if div.has_key('id') and div['id'] == 'body':
				core_class = parse_core_class_body(div)
				core_class['source'] = book
				filename = create_core_class_filename(output, book, core_class)
				fp = open(filename, 'w')
				json.dump(core_class, fp, indent=4)
				fp.close()
				write_tables(output, book)
	finally:
		fp.close()

def create_core_class_filename(output, book, core_class):
	title = char_replace(book) + "/core_classes/" + char_replace(core_class['name'])
	return os.path.abspath(output + "/" + title + ".json")

