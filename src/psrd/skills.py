import os
import re
import json
from BeautifulSoup import BeautifulSoup
from psrd.files import char_replace
from psrd.warnings import WarningReporting
from psrd.parse import construct_line, has_name, get_subtitle, href_filter
from psrd.sections import store_section, filter_sections

def parse_skill(book, name, attr, armor_check, trained, lines):
	skill = {'name': name, 'source': book, 'type': 'skill', 'attribute': attr, 'armor_check_penalty': armor_check, 'trained_only': trained}
	field_name = 'description'
	details = []
	for tag in lines:
		if len(tag.contents) > 0:
			data = tag.contents[0]
			if has_name(data, 'b'):
				store_section(skill, ['Skills', skill['name'], field_name], details, field_name)
				field_name = construct_line([data.renderContents()])
				text = "<p>" + construct_line(tag.contents[1:]) + "</p>"
				details = [text]
			else:
				details.append(tag)
		else:
			details.append(tag)
	store_section(skill, ['Skills', skill['name'], field_name], details, field_name)
	print "%s: %s" %(skill['source'], skill['name'])
	filter_sections(skill)
	return skill

def parse_attr_line(tag):
	attr = None
	armor_check = False
	trained = False
	text = ''.join(tag.findAll(text=True))
	m = re.search('\((.*)\)', text)
	if m:
		parts = m.group(1).split("; ")
		attr = parts.pop(0)
		for part in parts:
			if part.lower() == 'armor check penalty':
				armor_check = True
			if part.lower() == 'trained only':
				trained = True
	return attr, armor_check, trained

def parse_body(div, book):
	name = None
	attr = None
	armor_check = False
	trained = False
	lines = []
	for tag in div.contents:
		if not str(tag).strip() == '':
			if has_name(tag, 'h1'):
				if not name:
					name = tag.renderContents()
					WarningReporting().context = name
				else:
					raise Exception("Skill has more then one name")
			elif has_name(tag, 'h2'):
				if not attr:
					attr, armor_check, trained = parse_attr_line(tag)
				else:
					raise Exception("Skill has more then one attribute line")
			else:
				lines.append(tag)
	return parse_skill(book, name, attr, armor_check, trained, lines)

def parse_skills(filename, output, book):
	WarningReporting().book = book
	fp = open(filename)
	try:
		soup = BeautifulSoup(fp)
		href_filter(soup)
		divs = soup.findAll('div')
		for div in divs:
			if div.has_key('id') and div['id'] == 'body':
				skill = parse_body(div, book)
				filename = create_skill_filename(output, book, skill)
				fp = open(filename, 'w')
				json.dump(skill, fp, indent=4)
				fp.close()
	finally:
		fp.close()

def create_skill_filename(output, book, skill):
	title = char_replace(book) + "/skills/" + char_replace(skill['name'])
	return os.path.abspath(output + "/" + title + ".json")

