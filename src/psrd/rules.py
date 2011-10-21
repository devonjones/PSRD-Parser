import os
import json
from psrd.files import char_replace
from psrd.parse import construct_line, get_subtitle

def parse_simple_rules(rules, subject):
	retarr = []
	if len(rules) == 0:
		return None
	for field in rules:
		retarr.append(unicode(field))
	return {'name': subject, 'type': 'section', 'text': u''.join(retarr).strip()}

def create_rules_filename(output, book, filename):
	title = char_replace(book) + "/rules/" + filename
	return os.path.abspath(output + "/" + title + ".json")

def write_rules(output, rules, book, filename):
	rules['source'] = book
	filename = create_rules_filename(output, book, filename)
	fp = open(filename, 'w')
	json.dump(rules, fp, indent=4)
	fp.close()

def subsection_b_rules_parse(book, section, tags):
	subsection = None
	lines = []
	for tag in tags:
		if len(tag.contents) > 0:
			data = tag.contents[0]
			if hasattr(data, 'name') and data.name == 'b' and not (tag.has_key('align') and tag['align'] == 'center'):
				if not subsection:
					description = construct_line(lines)
					if description:
						section['text'] = description
				else:
					subs = section.setdefault('subsections', [])
					subsection['text'] = construct_line(lines)
					subs.append(subsection)
				subsection = {'name': get_subtitle(tag), 'source': book, 'type': 'section'}
				text = "<p>" + construct_line(tag.contents[1:], strip_end_colon=False) + "</p>"
				lines = [text]
			else:
				lines.append(tag)
	if not subsection:
		description = construct_line(lines)
		if description:
			section['text'] = description
	else:
		subs = section.setdefault('subsections', [])
		subsection['text'] = construct_line(lines)
		subs.append(subsection)
	return section

def subsection_h2_rules_parse(book, section, tags):
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
				subs = section.setdefault('subsections', [])
				subs.append(subsection_b_rules_parse(book, subsection, lines))
			subsection = {'name': get_subtitle(tag), 'source': book, 'type': 'section'}
			lines = []
		else:
			lines.append(tag)
	if not subsection:
		description = construct_line(lines)
		if description:
			section['text'] = description
	else:
		subs = section.setdefault('subsections', [])
		subs.append(subsection_b_rules_parse(book, subsection, lines))
	return section
