import os
import re
import json
from BeautifulSoup import BeautifulSoup
from psrd.rules import write_rules
from psrd.files import char_replace
from psrd.warnings import WarningReporting
from psrd.parse import construct_line, get_subtitle, has_name
from psrd.tables import parse_table, is_table
from psrd.sections import store_section, set_section_text, filter_sections, href_filter

def parse_title_line(tag, book):
	text = get_subtitle(tag)
	m = re.search('(.*)\((.*)\)', text)
	if m:
		name = m.group(1).strip()
		types = m.group(2).split(", ")
		return {'name': name, 'source': book, 'feat_types': types, 'type': 'feat', 'sections': []}
	else:
		return {'name': text.strip(), 'source': book, 'type': 'feat', 'sections': []}

def parse_feat_descriptions(div, book):
	feats = []
	feat = None
	field_name = 'description'
	details = []
	for tag in div.contents:
		if unicode(tag).strip() != '':
			if len(tag.contents) > 0:
				data = tag.contents[0]
				if has_name(tag, 'h2'):
					if feat:
						set_section_text(feat, ['Feats', feat['name'], field_name], details)
						print "%s: %s" %(feat['source'], feat['name'])
						filter_sections(feat)
						feats.append(feat)
					feat = parse_title_line(tag, book)
					field_name = 'description'
					details = []
				elif has_name(tag, 'table') and field_name == 'description':
					feat['sections'].append(parse_table(tag, ['Feats', feat['name']], book))
				elif has_name(data, 'b'):
					if field_name == 'description':
						store_section(feat, ['Feats', feat['name'], field_name], details, field_name)
						details = [tag]
					else:
						details.append(tag)
					field_name = None
				else:
					details.append(tag)
			else:
				details.append(tag)
	set_section_text(feat, ['Feats', feat['name'], field_name], details)
	print "%s: %s" %(feat['source'], feat['name'])
	filter_sections(feat)
	feats.append(feat)
	return feats

def subsection_h2_rules_parse(book, rule, section, tags, context):
	lines = []
	if section['name'] == 'Feat Descriptions':
		table = None
		for tag in tags:
			if is_table(tag):
				table = parse_table(tag, context[:-1], book)
			else:
				lines.append(tag)
		store_section(rule, context, lines, section['name'])
		if table:
			rule['sections'].append(table)
		return
	subsections = []
	subsection = None
	for tag in tags:
		if has_name(tag, 'h2'):
			if not subsection:
				description = construct_line(lines)
				if description:
					section['text'] = description
			else:
				section.setdefault('sections', [])
				nc = []
				nc.extend(context)
				nc.append(subsection['name'])
				store_section(section, nc, lines, subsection['name'])
			subsection = {'name': get_subtitle(tag), 'source': book, 'type': 'section'}
			lines = []
		elif is_table(tag):
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
		store_section(section, nc, lines, subsection['name'])
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
			if has_name(tag, 'h1'):
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
				elif has_name(tag, 'div'):
					for line in tag.contents:
						if unicode(line).strip() != '':
							lines.append(line)
	subsection_h2_rules_parse(book, rules, section, lines, ["Feats", section['name']])
	filter_sections(rules)
	return rules, feats

def parse_feats(filename, output, book):
	WarningReporting().book = book
	fp = open(filename)
	try:
		soup = BeautifulSoup(fp)
		href_filter(soup)
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
