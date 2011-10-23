import os
import re
import json
from BeautifulSoup import BeautifulSoup
from psrd.rules import write_rules
from psrd.files import char_replace
from psrd.warnings import WarningReporting
from psrd.parse import construct_line, get_subtitle
from psrd.tables import parse_table
from psrd.sections import store_section

def parse_title_line(tag, book):
	text = get_subtitle(tag)
	m = re.search('(.*)\((.*)\)', text)
	if m:
		name = m.group(1).strip()
		types = m.group(2).split(", ")
		return {'name': name, 'source': book, 'feat_types': types, 'type': 'feat'}
	else:
		return {'name': text.strip(), 'source': book, 'type': 'feat'}

def parse_feat_descriptions(div, book):
	feats = []
	feat = None
	field_name = 'description'
	details = []
	for tag in div.contents:
		if unicode(tag).strip() != '':
			if len(tag.contents) > 0:
				data = tag.contents[0]
				if hasattr(tag, 'name') and tag.name == 'h2':
					if feat:
						store_section(feat, ['Feats', feat['name'], field_name], details, field_name)
						print "%s: %s" %(feat['source'], feat['name'])
						feats.append(feat)
					feat = parse_title_line(tag, book)
					field_name = 'description'
					details = []
				elif hasattr(data, 'name') and data.name == 'b':
					store_section(feat, ['Feats', feat['name'], field_name], details, field_name)
					field_name = construct_line([data.renderContents()])
					text = "<p>" + construct_line(tag.contents[1:], strip_end_colon=False) + "</p>"
					details = [text]
				else:
					details.append(tag)
			else:
				details.append(tag)
	store_section(feat, ['Feats', feat['name'], field_name], details, field_name)
	print "%s: %s" %(feat['source'], feat['name'])
	feats.append(feat)
	return feats

def subsection_b_rules_parse(book, rule, section, tags, context):
	subsection = None
	lines = []
	for tag in tags:
		if hasattr(tag, 'name') and tag.name == 'table':
			rule['sections'].append(parse_table(tag, context[:-1], book))
		elif len(tag.contents) > 0:
			data = tag.contents[0]
			if hasattr(data, 'name') and data.name == 'b' and not (tag.has_key('align') and tag['align'] == 'center'):
				if not subsection:
					description = construct_line(lines)
					if description:
						section['text'] = description
				else:
					subs = section.setdefault('sections', [])
					subsection['text'] = construct_line(lines)
					subs.append(subsection)
				subsection = {'name': get_subtitle(tag), 'source': book, 'type': 'section'}
				subsection['name'] = subsection['name'].replace(':', '')
				text = "<p>" + construct_line(tag.contents[1:], strip_end_colon=False) + "</p>"
				lines = [text]
			else:
				lines.append(tag)
	if not subsection:
		description = construct_line(lines)
		if description:
			section['text'] = description
	else:
		subs = section.setdefault('sections', [])
		subsection['text'] = construct_line(lines)
		subs.append(subsection)
	rule['sections'].append(section)

def subsection_h2_rules_parse(book, rule, section, tags, context):
	if section['name'] == 'Feat Descriptions':
		return subsection_b_rules_parse(book, rule, section, tags, context)
	subsections = []
	subsection = None
	lines = []
	for tag in tags:
		if hasattr(tag, 'name') and tag.name == 'h2':
			if not subsection:
				description = construct_line(lines)
				if description:
					section['text'] = description
			else:
				section.setdefault('sections', [])
				nc = []
				nc.extend(context)
				nc.append(subsection['name'])
				subsection_b_rules_parse(book, section, subsection, lines, nc)
			subsection = {'name': get_subtitle(tag), 'source': book, 'type': 'section'}
			lines = []
		elif hasattr(tag, 'name') and tag.name == 'table':
			rule['sections'].append(parse_table(tag, context[:-1], book))
		else:
			lines.append(tag)
	if not subsection:
		description = construct_line(lines)
		if description:
			section['text'] = description
	else:
		section.setdefault('sections', [])
		nc = []
		nc.extend(context)
		nc.append(subsection['name'])
		subsection_b_rules_parse(book, section, subsection, lines, nc)
	if section.has_key('text') or section.has_key('sections'):
		rule['sections'].append(section)

def parse_body(div, book):
	sections = []
	feats = None
	section = None
	lines = []
	rules = {'name': 'Feats', 'type': 'section', 'source': book, 'sections': []}
	tags = [tag for tag in div.contents if unicode(tag).strip() != '']
	if tags[0].name == 'div':
		div = tags[0]
	for tag in div.contents:
		if unicode(tag).strip() != '':
			if hasattr(tag, 'name') and tag.name == 'h1':
				if section:
					if section['name'] == 'Feats':
						rules['text'] = construct_line(lines)
					else:
						subsection_h2_rules_parse(book, rules, section, lines, ["Feats", section['name']])
				lines = []
				section = {'name': get_subtitle(tag), 'type': 'section', 'source': book}
			elif (hasattr(tag, 'name') and tag.name != 'div') or not hasattr(tag, 'name'):
				lines.append(tag)
			else:
				name = section['name']
				if section['type'] == 'table' or name.find('Feat Descriptions') > -1 or name.find('Monster Feats')> -1:
					feats = parse_feat_descriptions(tag, book)
				elif hasattr(tag, 'name') and tag.name == 'div':
					for line in tag.contents:
						if unicode(line).strip() != '':
							lines.append(line)
	subsection_h2_rules_parse(book, rules, section, lines, ["Feats", section['name']])
	return rules, feats

def parse_feats(filename, output, book):
	WarningReporting().book = book
	fp = open(filename)
	try:
		soup = BeautifulSoup(fp)
		divs = soup.findAll('div')
		for div in divs:
			if div.has_key('id') and div['id'] == 'body':
				rules, feats = parse_body(div, book)
				for feat in feats:
					filename = create_feat_filename(output, book, feat)
					fp = open(filename, 'w')
					json.dump(feat, fp, indent=4)
					fp.close()
				if rules:
					write_rules(output, rules, book, "feats")
	finally:
		fp.close()

def create_feat_filename(output, book, feat):
	title = char_replace(book) + "/feats/" + char_replace(feat['name'])
	return os.path.abspath(output + "/" + title + ".json")
