import re
from psrd.tables import has_table, is_table, parse_table
from psrd.parse import construct_stripped_line, construct_line, has_name, has_first_child, get_first_child_text
from BeautifulSoup import BeautifulSoup


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
	if has_section(subtag_closure('h2'), soup.contents):
		return False
	elif has_section(subtag_closure('b'), soup.contents):
		return False
	return True

def check_for_breakouts(section, context, text):
	soup = BeautifulSoup(text)
	if has_section(subtag_closure('h2'), soup.contents):
		print "H2"
	elif has_section(subtag_closure('b'), soup.contents):
		handle_section(section, context, soup.contents, "b")
	elif has_section(subtag_closure('i'), soup.contents):
		handle_section(section, context, soup.contents, "i")
	else:
		section['text'] =  text

def handle_section(section, context, details, tag_name):
	title = None
	lines = []
	for detail in details:
		tag = {}
		if has_first_child(detail, tag_name) and not (detail.has_key('align') and detail['align'] == 'center'):
			_handle_section_storage(section, context, lines, title)
			title = get_first_child_text(detail, tag_name).strip()
			if title.endswith(':'):
				title = title[:-1]
			lines = ["<" + detail.name + ">" + construct_line(detail.contents[1:]) + "</" + detail.name + ">"]
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
		return False
	return is_subtag 

def filter_sections(section):
	if section:
		if section.has_key('sections'):
			for s in section['sections']:
				filter_sections(s)
		if section['type'] == 'section':
			section_filter_ability_type(section)
		section_filter_abbrev(section)

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

def section_filter_abbrev(section):
	if section.has_key('name') and section['type'] != 'table':
		m = re.search('\s*\((.*)\)', section['name'])
		if m:
			section['abbrev'] = m.group(1)
			section['name'] = re.sub('\s*\(%s\)' % m.group(1), '', section['name']).strip()

