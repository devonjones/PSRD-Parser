# -*- coding: UTF8 -*-
import re
import sys
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup

def section_filter_ability_type(section):
	abilities = {
		'Ex': ['Extraordinary'],
		'Sp': ['Spell-Like'],
		'Su': ['Supernatural'],
		'Ex or Sp': ['Extraordinary', 'Spell-Like'],
		'Ex and Sp': ['Extraordinary', 'Spell-Like'],
		'Ex or Su': ['Extraordinary', 'Supernatural'],
		'Ex and Su': ['Extraordinary', 'Supernatural'],
		'Su or Sp': ['Supernatural', 'Spell-Like'],
		'Su and Sp': ['Supernatural', 'Spell-Like'],
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

def filter_quotes(text):
	if unicode(text).find(u'\u201c') > -1:
		text = unicode(text).replace(u'\u201c', '&ldquo;')
	if unicode(text).find(u'\u00e2&euro;&oelig;') > -1:
		text = unicode(text).replace(u'\u00e2&euro;&oelig;', '&ldquo;')
	if unicode(text).find(u'\u201d') > -1:
		text = unicode(text).replace(u'\u201d', '&rdquo;')
	if unicode(text).find(u'\u00e2&euro;?') > -1:
		text = unicode(text).replace(u'\u00e2&euro;?', '&rdquo;')
	return text

def quote_pass(section):
	for item in section.get('sections', []):
		quote_pass(item)
	if section.has_key('text'):
		section['text'] = filter_quotes(section['text'])
	if section.has_key('description'):
		section['description'] = filter_quotes(section['description'])
	return section

def entity_pass(section):
	for item in section.get('sections', []):
		entity_pass(item)
	if section.get('name') != None and section.get('name') != '':
		name = section['name']
		name = name.replace('&ndash;', '-')
		name = name.replace('&mdash;', '-')
		name = name.replace('&nbsp;', '')
		name = name.replace('&amp;', 'and')
		name = name.replace('&hellip;', '...')
		if name.endswith(":"):
			name = section['name'][:-1]
		section['name'] = name.strip()
	return section

def section_name_pass(struct):
	if section.has_key('name') and section['name']:
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
