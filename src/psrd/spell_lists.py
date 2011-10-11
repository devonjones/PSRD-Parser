import os
import re
import json
from BeautifulSoup import BeautifulSoup
from psrd.rules import parse_simple_rules, write_rules
from psrd.files import char_replace
from psrd.parse import construct_stripped_line

def parse_spell_list(casting_class, level, rows):
	spells = []
	school = None
	descriptor = None
	for row in rows:
		material = None
		if row.name == 'p' and hasattr(row.contents[0].contents[0], 'name'):
			name = row.contents[0].contents[0].renderContents().strip()
			start = 1
			for i in range(1, len(row.contents)):
				tag = row.contents[i]
				if unicode(tag).find(':') == 0:
					start = i
					break
			if start > 1:
				sup = row.contents[start - 1]
				if hasattr(sup, 'name') and sup.name == 'sup':
					if ''.join(sup.findAll(text=True)).strip() != '':
						material = ''.join(sup.findAll(text=True)).strip()
			desc = construct_stripped_line(row.contents[start:])
			spell = {'name': name, 'short_description': desc}
			if material:
				spell['material'] = list(material)
			if school:
				spell['school'] = school
			if descriptor:
				spell['descriptor'] = descriptor
			spells.append(spell)
		elif row.name == 'p' and not hasattr(row.contents[0].contents[0], 'name'):
			descriptor = row.contents[0].renderContents()
		elif row.name == 'h3':
			school = row.renderContents()
	spell_list = {'class': casting_class.strip(), 'spells': spells, 'description': level.renderContents().strip()}
	m = re.search('(\d)', spell_list['description'])
	spell_list['level'] = int(m.group(0))
	return spell_list

def parse_body(div):
	if len(div.contents) <= 2:
		div = div.contents[0]
	rules = []
	casting_class = None
	level = None
	rows = []
	spell_lists = []
	spell_section = False
	for tag in div.contents:
		if not spell_section:
			if hasattr(tag, 'name') and tag.name == 'h1' and tag.string.endswith(' Spells'):
				spell_section = True
			else:
				save = True
				if unicode(tag).strip() == '':
					save = False
				if hasattr(tag, 'name') and tag.name == 'p' and len(tag.contents) == 1:
					subtag = tag.contents[0]
					if hasattr(subtag, 'name') and subtag.name == 'a':
						if re.match(r'#[a-z\-/]*-spells', subtag['href']):
							save = False
				if hasattr(tag, 'name') and tag.name == 'h1' and tag.renderContents().lower() == 'spells by class':
					save = False
				if save:
					rules.append(tag)
		if spell_section:
			if not unicode(tag).strip() == '':
				if hasattr(tag, 'name') and tag.name == 'h1':
					if casting_class:
						spell_lists.append(parse_spell_list(casting_class, level, rows))
						rows = []
					casting_class = tag.renderContents().replace(" Spells", '')
				elif hasattr(tag, 'name') and tag.name == 'h2':
					if level:
						spell_lists.append(parse_spell_list(casting_class, level, rows))
						rows = []
					level = tag
				elif hasattr(tag, 'name') and tag.name == 'h3':
					rows.append(tag)
				elif hasattr(tag, 'name') and tag.name == 'p':
					rows.append(tag)
				else:
					raise Exception("Unexpected line type: %s" % tag)
	spell_lists.append(parse_spell_list(casting_class, level, rows))
	rules = parse_simple_rules(rules, "Spell Lists")
	return rules, spell_lists

def parse_spell_lists(filename, output, book):
	fp = open(filename)
	try:
		soup = BeautifulSoup(fp)
		divs = soup.findAll('div')
		for div in divs:
			if div.has_key('id') and div['id'] == 'body':
				rules, spell_lists = parse_body(div)
				for spell_list in spell_lists:
					spell_list['source'] = book
					filename = create_spell_list_filename(output, book, spell_list)
					fp = open(filename, 'w')
					json.dump(spell_list, fp, indent=4)
					fp.close()
				if rules:
					write_rules(output, rules, book, "spell_lists")
	finally:
		fp.close()

def create_spell_list_filename(output, book, spell_list):
	title = char_replace(book) + "/spell_lists/" + char_replace(spell_list['class']) + "-" + unicode(spell_list['level'])
	return os.path.abspath(output + "/" + title + ".json")
