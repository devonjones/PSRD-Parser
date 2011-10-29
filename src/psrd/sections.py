import re
import sys
from psrd.tables import has_table, is_table, parse_table
from psrd.parse import construct_stripped_line, construct_line, has_name, has_first_child, get_first_child_text
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup

def store_section(parent, context, details, name=None):
	if name == 'description':
		parent[name] = construct_stripped_line(details)
	else:
		section = {'source': parent['source'], 'type': 'section'}
		if name:
			section['name'] = construct_stripped_line(name)
		set_section_text(section, context, details)
		if section.has_key('text') or section.has_key('sections'):
			sections = parent.setdefault('sections', [])
			if not section.has_key('text') and not section.has_key('description') and not section.has_key('name'):
				sections.extend(section['sections'])
			else:
				sections.append(section)

def set_section_text(section, context, details):
	if has_table(details) and at_lowest(details):
		section['sections'] = []
		lines = []
		for detail in details:
			if is_table(detail):
				if len(lines) > 0:
					store_section(section, context, lines)
					lines = []
				if detail.name == 'div':
					detail = detail.findAll(text=False)[0]
				section['sections'].append(parse_table(detail, context, section['source']))
			else:
				if not has_name(detail, 'br'):
					lines.append(detail)
		if len(lines) > 0:
			store_section(section, context, lines)
	else:
		text = construct_line(details)
		if text:
			check_for_breakouts(section, context, text)

def at_lowest(details):
	text = construct_line(details)
	soup = BeautifulSoup(text)
	if has_section(subtag_closure('h1'), soup.contents):
		return False
	elif has_section(subtag_closure('h2'), soup.contents):
		return False
	elif has_section(subtag_closure('b'), soup.contents):
		return False
	return True

def check_for_breakouts(section, context, text):
	soup = BeautifulSoup(text)
	if has_section(subtag_closure('h1'), soup.contents):
		handle_titled_section(section, context, soup.contents, "h1")
	elif has_section(subtag_closure('h2'), soup.contents):
		handle_titled_section(section, context, soup.contents, "h2")
	elif has_section(subtag_closure('b'), soup.contents) or has_section(subtag_closure('h3'), soup.contents):
		handle_section(section, context, soup.contents, "b")
	elif has_section(subtag_closure('i'), soup.contents):
		handle_section(section, context, soup.contents, "i")
	else:
		section['text'] =  text

def handle_titled_section(section, context, details, tag_name):
	title = None
	lines = []
	for detail in details:
		if has_name(detail, tag_name):
			if title:
				_handle_section_storage(section, context, lines, title)
			else:
				if len(lines) > 0:
					set_section_text(section, context, lines)
			title = ''.join(detail.findAll(text=True))
			lines = []
		else:
			if not has_name(detail, 'br'):
				lines.append(detail)
	_handle_section_storage(section, context, lines, title)

def handle_section(section, context, details, tag_name):
	title = None
	lines = []
	for detail in details:
		if has_first_child(detail, tag_name) and not (detail.has_key('align') and detail['align'] == 'center'):
			if title:
				_handle_section_storage(section, context, lines, title)
			else:
				if len(lines) > 0:
					set_section_text(section, context, lines)
			title = get_first_child_text(detail, tag_name).strip()
			if title.endswith(':'):
				title = title[:-1]
			lines = ["<" + detail.name + ">" + construct_line(detail.contents[1:]) + "</" + detail.name + ">"]
		elif tag_name == 'b' and has_name(detail, 'h3'):
			if title:
				_handle_section_storage(section, context, lines, title)
			else:
				if len(lines) > 0:
					set_section_text(section, context, lines)
			title = ''.join(detail.findAll(text=True))
			lines = []
		else:
			if not has_name(detail, 'br'):
				lines.append(detail)
	_handle_section_storage(section, context, lines, title)

def _handle_section_storage(section, context, lines, title):
	if lines:
		if title:
			ct = []
			ct.extend(context)
			ct.append(title)
			store_section(section, ct, lines, title)
		else:
			if section.has_key('text'):
				store_section(section, context, lines)
			else:
				section['text'] = construct_line(lines)

def has_section(test_fxn, details):
	for detail in details:
		if hasattr(detail, 'name'):
			if test_fxn(detail):
				return True
	return False

def subtag_closure(subtag):
	def is_subtag(detail):
		if has_first_child(detail, subtag):
			if subtag == 'b':
				if (detail.has_key('align') and detail['align'] == 'center'):
					return False
			if subtag in ('b', 'i'):
				if get_first_child_text(detail, subtag).strip().endswith(':'):
					return True
				elif unicode(detail.contents[1]).strip().startswith(':'):
					return True
			if subtag in ('h1', 'h2', 'h3'):
				if has_name(detail, subtag):
					return True
		return False
	return is_subtag 

def filter_sections(section, ability=True):
	if section:
		#section_filter_deanonymize(section)
		if section.has_key('sections'):
			for s in section['sections']:
				if section.has_key('name') and section['name'] == 'Common Terms':
					ability = False
				else:
					ability = True
				filter_sections(s, ability)
		if section['type'] == 'section' and ability:
			section_filter_ability_type(section)
		section_filter_abbrev(section)
		section_filter_entities(section)

def section_filter_ability_type(section):
	abilities = {
		'Ex': 'Extraordinary',
		'Sp': 'Special',
		'Su': 'Supernatural',
		'Ex or Sp': 'Extraordinary or Special',
		'Ex and Sp': 'Extraordinary and Special',
		'Ex or Su': 'Extraordinary or Supernatural',
		'Ex and Su': 'Extraordinary and Supernatural',
		'Su or Sp': 'Supernatural or Special',
		'Su and Sp': 'Supernatural and Special',
	}
	if section.has_key('name'):
		m = re.search('\((.*)\)', section['name'])
		if m:
			if m.group(1) in abilities.keys():
				section['type'] = 'ability'
				section['ability_type'] = abilities[m.group(1)]
				section['name'] = re.sub('\(.*\)', '', section['name']).strip()
				return
	if section.has_key('text'):
		tag = BeautifulSoup(section['text'])
		text = ''.join(tag.findAll(text=True))
		m = re.search('\((.*?)\):?\s?', text)
		if m:
			if m.group(1) in abilities.keys():
				section['type'] = 'ability'
				section['ability_type'] = abilities[m.group(1)]
				sec = "(%s)" % m.group(1)
				for t in [sec + ": ", sec + ":", sec]:
					r = tag.find(text=re.compile("\(%s\):?\s?" % m.group(1)))
					if r:
						nt = re.sub("\(%s\):?\s?" % m.group(1), "", unicode(r))
						r.replaceWith(nt)
						section['text'] = unicode(tag)
						return

def section_filter_deanonymize(section):
	if section.get('text') == None and section.get('description') == None:
		sections = section.get('sections', [])
		if len(sections) >= 1 and sections[0].get('name', '') == '' and sections[0]['type'] == 'section':
			s = sections.pop(0)
			if s.has_key('text'):
				section['text'] = s['text']
			if s.has_key('description'):
				section['description'] = s['description']
			if s.has_key('sections'):
				while len(s['sections']) > 0:
					ns = s['sections'].pop()
					section['sections'].insert(0, ns)

def section_filter_abbrev(section):
	if section['type'] != 'spell':
		if section.has_key('name') and section['type'] != 'table':
			m = re.search('\s*\((.*)\)', section['name'])
			if m:
				name = re.sub('\s*\(%s\)' % m.group(1), '', section['name']).strip()
				if name != '':
					section['abbrev'] = m.group(1)
					section['name'] = re.sub('\s*\(%s\)' % m.group(1), '', section['name']).strip()

def section_filter_entities(section):
	if section.get('name') != None:
		section['name'] = BeautifulStoneSoup(section['name'], convertEntities=BeautifulStoneSoup.HTML_ENTITIES).contents[0]
	if section.get('description') != None:
		section['description'] = BeautifulStoneSoup(section['description'], convertEntities=BeautifulStoneSoup.HTML_ENTITIES).contents[0]


def print_struct(section, level=0):
	sys.stderr.write(''.join(["-" for i in range(0, level)]))
	if section.has_key('name'):
		print section['name']
	else:
		print "<Anonymous>"
	if section.has_key('sections'):
		for s in section['sections']:
			print_struct(s, level + 2)

