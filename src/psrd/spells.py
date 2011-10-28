import os
import re
import json
from BeautifulSoup import BeautifulSoup
from psrd.files import char_replace
from psrd.warnings import WarningReporting
from psrd.parse import get_subtitle, construct_stripped_line, href_filter
from psrd.tables import parse_table
from psrd.sections import filter_sections

def parse_function(field):
	functions = {
		'school': parse_school,
		'level': parse_level,
		'components': parse_components,
		'component': parse_components,
		'saving throw': parse_saving_throw,
		'saving': parse_saving_throw,
		'save': warning_closure(
			parse_saving_throw,
			"Save used instead of Saving Throw"),
		'casting time': parse_casting_time,
		'casting': parse_casting_time,
		'preparation time': attribute_closure('preparation_time'),
		'range': attribute_closure('range'),
		'duration': attribute_closure('duration'),
		'spell resistance': attribute_closure('spell_resistance'),
		'sr': warning_closure(
			attribute_closure('spell_resistance'),
			"SR used instead of Spell Resistance"),
		'effect': effect_closure('Effect'),
		'targets': effect_closure('Targets'),
		'target': effect_closure('Target'),
		'area': effect_closure('Area'),
		'target or area': effect_closure('Target or Area'),
		'area or target': warning_closure(
			effect_closure('Target or Area'),
			"Area or Target used instead of Target or Area"),
		'target or targets': effect_closure('Target or Targets'),
		'target, effect, or area': effect_closure('Target, Effect, or Area'),
		'target, effect, area': warning_closure(
			effect_closure('Target, Effect, or Area'),
			"Target, Effect, Area used instead of Target, Effect, or Area"),
		'target/effect': warning_closure(
			effect_closure('Target or Effect'),
			"Target/Effect used instead of Target or Effect"),
	}
	return functions[field.lower()]

def warning_closure(function, warning):
	def fxn(race, contents):
		WarningReporting().report(warning)
		function(race, contents)
	return fxn

def effect_closure(field):
	def fxn(spell, contents):
		effect = spell.setdefault('effects', [])
		effect.append({'name': field, 'text': construct_stripped_line(contents)})
	return fxn

def attribute_closure(field):
	def fxn(spell, contents):
		spell[field] = construct_stripped_line(contents)
	return fxn

def parse_casting_time(spell, contents):
	casting_time = construct_stripped_line(contents)
	if casting_time.find('Time ') == 0:
		# Ultimate Magic: Vision of Hell: the text for casting time is broken.
		WarningReporting().report("Broken <b> tag for Casting Time")
		casting_time = casting_time.replace('Time', '')
	spell['casting_time'] = casting_time

def parse_saving_throw(spell, contents):
	contents = handle_subline(spell, contents, "Spell Resistance")
	contents = handle_subline(spell, contents, "SR")
	st = construct_stripped_line(contents)
	st = st.replace(';', '')
	if st.find('Throw ') == 0:
		# Ultimate Magic: Unholy Sword: the text for saving throw is broken.
		WarningReporting().report("Broken <b> tag for Saving Throw")
		st = st.replace('Throw ', '')
	spell['saving_throw'] = st

def parse_components(spell, contents):
	components = construct_stripped_line(contents)
	m = re.search('\(.*?[^\)],.*?\)', components)
	while m:
		components = re.sub(r"\((.*?)[^\)],(.*?)\)", r"(\1|\2)", components)
		m = re.search('\(.*?[^\)],.*?\)', components)
	comps = components.split(', ')
	finalcomps = []
	for comp in comps:
		if comp.find('(') > -1:
			m = re.search('(.*) \((.*)\)', comp)
			name = m.group(1)
			comments = m.group(2)
			comments = comments.replace('|', ',')
			finalcomps.append({'type': name, 'text': comments})
		else:
			finalcomps.append({'type': comp})
	spell['components'] = finalcomps

def parse_school(spell, contents):
	contents = handle_subline(spell, contents, "Level")
	school = construct_stripped_line(contents)
	school = school.replace(';', '')
	m = re.search('\((.*)\)', school)
	if m:
		spell['subschool'] = m.group(1)
		school = re.sub('\(.*\)', '', school)
	m = re.search('\[(.*)\]', school)
	if m:
		descriptor = m.group(1)
		spell['descriptor'] = descriptor.split(', ')
		school = re.sub('\[.*\]', '', school)
	spell['school'] = school.strip()

def parse_level(spell, contents):
	level = construct_stripped_line(contents)
	levels = level.split(', ')
	finallevels = []
	for level in levels:
		m = re.search('(.*) (\d*)', level)
		finallevels.append({'class': m.group(1), 'level': int(m.group(2))})
	spell['level'] = finallevels

def parse_subline(spell, subtitle, field):
	if subtitle != u'':
		function = parse_function(subtitle.strip())
		function(spell, field)
	else:
		raise Exception('field has no title')

def handle_subline(spell, contents, title):
	levelval = None
	for i in range(0, len(contents)):
		sub = get_subtitle(contents[i])
		if sub and sub.strip() == title:
			levelval = i
			break
	if levelval:
		parse_subline(spell, get_subtitle(contents[levelval]), contents[levelval+1:])
		contents = contents[0:levelval]
	return contents

def handle_text(spell, spell_text):
	sections = []
	section = []
	lastname = None
	for line in spell_text:
		if not lastname:
			lastname = line.name
		if line.name != lastname:
			sections.append(section)
			section = [line]
			lastname = line.name
		else:
			section.append(line)
	sections.append(section)
	if len(sections) == 1:
		spell['text'] = u''.join([unicode(line) for line in sections[0]])
	else:
		for section in sections:
			create_section(spell, section)

def create_section(spell, section):
	sections = spell.setdefault('sections', [])
	if len(section) == 1 and section[0].name == 'table':
		table = parse_table(section[0], ["Spells", spell['name']], spell['source'])
		sections.append(table)
	elif len(section) == 1 and len(section[0].contents) == 1 and hasattr(section[0].contents[0], 'name') and section[0].contents[0].name == 'table':
		table = parse_table(section[0].contents[0], ["Spells", spell['name']], spell['source'])
		sections.append(table)
	else:
		newsec = {'source': spell['source'], 'type': 'text'}
		newsec['text'] = u''.join([unicode(line) for line in section])
		sections.append(newsec)

def create_spell(title, book, attributes, spell_text):
	spell = {'name': title, 'source': book, 'type': 'spell'}
	WarningReporting().context = spell['name']
	for attribute in attributes:
		parse_subline(spell, get_subtitle(attribute.contents[0]), attribute.contents[1:])
	handle_text(spell, spell_text)
	print "%s: %s" %(spell['source'], spell['name'])
	filter_sections(spell)
	return spell

def parse_body(div, book):
	title = None
	attributes = []
	spell_text = []
	spells = []
	for tag in div.contents:
		if not hasattr(tag, 'contents'):
			if unicode(tag).strip() != '':
				spell_text.append(tag)
		elif tag.has_key('class') and tag['class'].find('stat-block-title') > -1:
			if not title:
				title = ''.join(tag.findAll(text=True)).strip()
			else:
				spells.append(create_spell(title, book, attributes, spell_text))
				title = ''.join(tag.findAll(text=True)).strip()
				attributes = []
				spell_text = []
		elif tag.has_key('class') and tag['class'].find('stat-block-1') > -1:
			attributes.append(tag)
		else:
			spell_text.append(tag)
	spells.append(create_spell(title, book, attributes, spell_text))
	if len(spells) > 1:
		for i in range(1, len(spells)):
			spells[i]['parent'] = spells[0]['name']
	return spells

def parse_spell(filename, output, book):
	WarningReporting().book = book
	fp = open(filename)
	try:
		soup = BeautifulSoup(fp)
		href_filter(soup)
		divs = soup.findAll('div')
		for div in divs:
			if div.has_key('id') and div['id'] == 'body':
				spells = parse_body(div, book)
				for spell in spells:
					filename = create_spell_filename(output, book, spell)
					fp = open(filename, 'w')
					json.dump(spell, fp, indent=4)
					fp.close()
	finally:
		fp.close()

def create_spell_filename(output, book, spell):
	title = char_replace(book) + "/spells/" + char_replace(spell['name'])
	return os.path.abspath(output + "/" + title + ".json")

