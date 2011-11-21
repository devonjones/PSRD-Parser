import re
import sys
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup

def section_filter_ability_type(section):
	abilities = {
		'Ex': ['Extraordinary'],
		'Sp': ['Special'],
		'Su': ['Supernatural'],
		'Ex or Sp': ['Extraordinary', 'Special'],
		'Ex and Sp': ['Extraordinary', 'Special'],
		'Ex or Su': ['Extraordinary', 'Supernatural'],
		'Ex and Su': ['Extraordinary', 'Supernatural'],
		'Su or Sp': ['Supernatural', 'Special'],
		'Su and Sp': ['Supernatural', 'Special'],
	}
	if section.has_key('name'):
		m = re.search('\((.*)\)', section['name'])
		if m:
			if m.group(1) in abilities.keys():
				section['type'] = 'ability'
				section['ability_types'] = abilities[m.group(1)]
				section['name'] = re.sub('\(.*\)', '', section['name']).strip()
				return
	if section.has_key('text'):
		tag = BeautifulSoup(section['text'])
		text = ''.join(tag.findAll(text=True))
		m = re.search('\((.*?)\):?\s?', text)
		if m:
			if m.group(1) in abilities.keys():
				section['type'] = 'ability'
				section['ability_types'] = abilities[m.group(1)]
				sec = "(%s)" % m.group(1)
				for t in [sec + ": ", sec + ":", sec]:
					r = tag.find(text=re.compile("\(%s\):?\s?" % m.group(1)))
					if r:
						nt = re.sub("\(%s\):?\s?" % m.group(1), "", unicode(r))
						r.replaceWith(nt)
						section['text'] = unicode(tag)
						return

def is_anonymous_section(section):
	if section['type'] == 'section':
		if not section.has_key('name'):
			return True
	return False

def has_subsections(section):
	if section.has_key('section'):
		if len(section['sections']) > 0:
			return True
	return False

def ability_pass(section):
	section_filter_ability_type(section)
	if section.has_key('sections'):
		for s in section['sections']:
			ability_pass(s)
	return section

def entity_pass(section):
	for item in section.get('sections', []):
		entity_pass(item)
	if section.get('name') != None and section.get('name') != '':
		section['name'] = BeautifulStoneSoup(section['name'], convertEntities=BeautifulStoneSoup.HTML_ENTITIES).contents[0]
		section['name'] = section['name'].replace(u'\u2013', '-')
		if section['name'].endswith(":"):
			section['name'] = section['name'][:-1]
	if section.get('description') != None:
		section['description'] = BeautifulStoneSoup(section['description'], convertEntities=BeautifulStoneSoup.HTML_ENTITIES).contents[0]
		section['description'] = section['description'].replace(u'\u2013', '-')
	return section

def find_section(section, name=None, section_type=None):
	if __test_name(name, section) and __test_type(section_type, section):
		return section

	for s in section.get('sections', []):
		if section.__class__ == dict:
			retval = find_section(s, name, section_type)
			if retval:
				return retval

def find_all_sections(section, name=None, section_type=None):
	if __test_name(name, section) and __test_type(section_type, section):
		return [section]
	retlist = []
	for s in section.get('sections', []):
		if section.__class__ == dict:
			retval = find_all_sections(s, name, section_type)
			retlist.extend(retval)
	return retlist

def add_section(top, section):
	sections = top.setdefault('sections', [])
	sections.append(section)

def remove_section(section, rem):
	if section.__class__ == dict:
		for s in section.get('sections', []):
			if s == rem:
				section['sections'].remove(rem)
				if len(section['sections']) == 0:
					del section['sections']
				return
			else:
				remove_section(s, rem)

def __test_name(name, section):
	if hasattr(name, 'match'):
		m = name.match(section.get('name', '').strip())
		if not name.match(section.get('name', '').strip()):
			return False
	elif name:
		if not section.get('name') == name:
			return False
	return True

def __test_type(section_type, section):
	if section_type:
		if not section.has_key('type'):
			return False
		if section['type'] != section_type:
			return False
	return True

def cap_words(st):
	parts = st.split(" ")
	fps = []
	for part in parts:
		word = part[0].upper() + part[1:]
		word = _handle_parens(word)
		word = _handle_slash(word)
		fps.append(word)
	return ' '.join(fps)

def _handle_parens(st):
	if st.find("(") > -1:
		p = st.find("(")
		return st[0:p + 1] + st[p + 1].upper() + st[p+2:]
	return st

def _handle_slash(st):
	if st.find("/"):
		parts = st.split("/")
		fps = []
		for part in parts:
			word = part[0].upper() + part[1:]
			fps.append(word)
		return '/'.join(fps)
	return st
