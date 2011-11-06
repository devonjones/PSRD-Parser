import os
import json
import re
from BeautifulSoup import BeautifulSoup
from psrd.rules import write_rules
from psrd.files import char_replace
from psrd.universal import parse_universal
from psrd.sections import ability_pass, is_anonymous_section, has_subsections, entity_pass

def parse_attr_line(text):
	attr = None
	armor_check = False
	trained = False
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

def skill_pass(skill):
	t = skill['sections'][0]
	skill['sections'] = t['sections']
	soup = BeautifulSoup(t['text'])
	skill['description'] = ''.join(soup.findAll(text=True))
	attr, armor_check, trained = parse_attr_line(t['name'])
	skill['attribute'] = attr
	skill['armor_check_penalty'] = armor_check
	skill['trained_only'] = trained

def parse_skills(filename, output, book):
	skill = parse_universal(filename, output, book)
	skill = entity_pass(skill)
	skill_pass(skill)
	print "%s: %s" %(skill['source'], skill['name'])
	filename = create_skill_filename(output, book, skill)
	fp = open(filename, 'w')
	json.dump(skill, fp, indent=4)
	fp.close()

def create_skill_filename(output, book, skill):
	title = char_replace(book) + "/skills/" + char_replace(skill['name'])
	return os.path.abspath(output + "/" + title + ".json")

