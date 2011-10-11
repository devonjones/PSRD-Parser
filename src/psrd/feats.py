import os
import re
import json
from BeautifulSoup import BeautifulSoup
from psrd.rules import subsection_h2_rules_parse, write_rules
from psrd.files import char_replace
from psrd.warnings import WarningReporting
from psrd.parse import construct_line, get_subtitle, store_section
from psrd.tables import parse_tables, write_tables, print_tables

def parse_title_line(tag):
	text = get_subtitle(tag)
	m = re.search('(.*)\((.*)\)', text)
	if m:
		name = m.group(1).strip()
		types = m.group(2).split(", ")
		return {'name': name, 'types': types}
	else:
		return {'name': text.strip()}

def parse_feat_descriptions(div):
	feats = []
	feat = None
	field_name = None
	details = []
	for tag in div.contents:
		if unicode(tag).strip() != '':
			if len(tag.contents) > 0:
				data = tag.contents[0]
				if hasattr(tag, 'name') and tag.name == 'h2':
					if feat:
						store_section(feat, field_name, details)
						parse_tables(details, ('Feats', feat['name'], field_name))
						feats.append(feat)
					feat = parse_title_line(tag)
					field_name = None
					details = []
				elif hasattr(data, 'name') and data.name == 'b':
					store_section(feat, field_name, details)
					parse_tables(details, ['Feats', feat['name'], field_name])
					field_name = construct_line([data.renderContents()])
					text = "<p>" + construct_line(tag.contents[1:], strip_end_colon=False) + "</p>"
					details = [text]
				else:
					details.append(tag)
			else:
				details.append(tag)
	store_section(feat, field_name, details)
	parse_tables(details, ['Feats', feat['name'], field_name])
	feats.append(feat)
	return feats

def parse_body(div):
	sections = []
	feats = None
	section = None
	lines = []
	tags = [tag for tag in div.contents if unicode(tag).strip() != '']
	if tags[0].name == 'div':
		div = tags[0]
	for tag in div.contents:
		if unicode(tag).strip() != '':
			if hasattr(tag, 'name') and tag.name == 'h1':
				if section:
					sections.append(subsection_h2_rules_parse(section, lines))
					parse_tables(lines, ["Feats", section['name']])
				lines = []
				section = {'name': get_subtitle(tag)}
			elif (hasattr(tag, 'name') and tag.name != 'div') or not hasattr(tag, 'name'):
				lines.append(tag)
			else:
				name = section['name']
				if name.find('Feat Descriptions') > -1 or name.find('Monster Feats')> -1:
					feats = parse_feat_descriptions(tag)
				elif hasattr(tag, 'name') and tag.name == 'div':
					for line in tag.contents:
						if unicode(line).strip() != '':
							lines.append(line)
	sections.append(subsection_h2_rules_parse(section, lines))
	parse_tables(lines, ["Feats", section['name']])
	rules = {'subject': 'Feats', 'sections': sections}
	return rules, feats

def parse_feats(filename, output, book):
	WarningReporting().book = book
	fp = open(filename)
	try:
		soup = BeautifulSoup(fp)
		divs = soup.findAll('div')
		for div in divs:
			if div.has_key('id') and div['id'] == 'body':
				rules, feats = parse_body(div)
				for feat in feats:
					feat['source'] = book
					filename = create_feat_filename(output, book, feat)
					fp = open(filename, 'w')
					json.dump(feat, fp, indent=4)
					fp.close()
				if rules:
					write_rules(output, rules, book, "feats")
		write_tables(output, book)
	finally:
		fp.close()

def create_feat_filename(output, book, feat):
	title = char_replace(book) + "/feats/" + char_replace(feat['name'])
	return os.path.abspath(output + "/" + title + ".json")
