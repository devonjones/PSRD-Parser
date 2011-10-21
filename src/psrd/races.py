import os
import re
import json
from BeautifulSoup import BeautifulSoup
from psrd.rules import parse_simple_rules, write_rules
from psrd.files import char_replace
from psrd.warnings import WarningReporting
from psrd.parse import construct_line, get_subtitle
from psrd.sections import store_section

def parse_function(field):
	functions = {
		'description': description_closure('description'),
		'physical description': description_closure('Physical Description'),
		'society': description_closure('Society'),
		'relations': description_closure('Relations'),
		'alignment and religion': description_closure('Alignment and Religion'),
		'alignment &amp; religion': warning_closure(
			description_closure('Alignment and Religion'),
			"Alignment & Religion used instead of Alignment and Religion"),
		'adventurers': description_closure('Adventurers'),
		'attributes': parse_attributes,
	}
	return functions[field.lower()]

def warning_closure(function, warning):
	def fxn(race, contents):
		WarningReporting().report(warning)
		function(race, contents)
	return fxn

def description_closure(field):
	def fxn(race, contents):
		store_section(race, ["Races", race['name'], field], contents, field)
	return fxn

def parse_attributes(race, contents):
	attributes = {'modifiers': []}
	tags = [content for content in contents.contents]
	attrs = tags.pop(0)
	attributes['description'] = construct_line(tags)
	num = None
	attr = None
	for tag in attrs.contents:
		if hasattr(tag, 'name') and tag.name == 'a':
			attr = tag.renderContents()
			attributes['modifiers'].append({'name': attr, 'modifier': num})
		else:
			m = re.search('\+(\d+)', tag)
			if m:
				num = int(m.group(1))
			m = re.search('&ndash;(\d+)', tag)
			if m:
				num = -1 * int(m.group(1))
	race['attributes'] = attributes

def parse_trait(race, contents):
	tags = [content for content in contents.contents]
	name = get_subtitle(tags.pop(0))
	description = construct_line(tags)
	traits = race.setdefault('traits', [])
	traits.append({'name': name, 'text': description})

def parse_race(race, book, rows):
	race = {'name': race, 'source': book}
	WarningReporting().context = race['name']
	field_name = None
	buffer = []
	traits = False
	attributes = True
	for tag in rows:
		if traits:
			if attributes:
				attributes = False
				parse_attributes(race, tag)
			else:
				parse_trait(race, tag)
		else:
			if hasattr(tag, 'name') and tag.name == 'h2':
				traits = True
			elif hasattr(tag.contents[0], 'name') and tag.contents[0].name == 'b':
				if not field_name:
					field_name = 'description'
				parse_function(field_name)(race, buffer)
				buffer = []
				field_name = tag.contents[0].renderContents()
				for i in range(1, len(tag.contents)):
					if unicode(tag.contents[i]) != '':
						buffer.append(tag.contents[i])
			else:
				for content in tag.contents:
					if unicode(content) != '':
						buffer.append(content)
	return race

def parse_body(div, book):
	rules = []
	races = []
	race = None
	rows = []
	for tag in div.contents:
		if unicode(tag).strip() != '':
			if hasattr(tag, 'name') and tag.name == 'h1':
				if race:
					races.append(parse_race(race, book, rows))
					rows = []
				race = tag.renderContents()
			else:
				if race:
					rows.append(tag)
				else:
					rules.append(tag)
	races.append(parse_race(race, book, rows))
	rules = parse_simple_rules(rules, "Races")
	return rules, races

def parse_races(filename, output, book):
	WarningReporting().book = book
	fp = open(filename)
	try:
		soup = BeautifulSoup(fp)
		divs = soup.findAll('div')
		for div in divs:
			if div.has_key('id') and div['id'] == 'body':
				rules, races = parse_body(div, book)
				for race in races:
					filename = create_race_filename(output, book, race)
					fp = open(filename, 'w')
					json.dump(race, fp, indent=4)
					fp.close()
				if rules:
					write_rules(output, rules, book, "races")
	finally:
		fp.close()

def create_race_filename(output, book, race):
	title = char_replace(book) + "/races/" + char_replace(race['name'])
	return os.path.abspath(output + "/" + title + ".json")

