import re
from BeautifulSoup import BeautifulSoup
from psrd.stat_block.utils import colon_filter, default_closure
from psrd.stat_block.section import parse_section
from psrd.universal import filter_name

def is_talent(sb, book):
	fields = dict(sb.keys)
	if "Element" in fields.keys() and "Level" in fields.keys() and "Burn" in fields.keys():
		return True
	elif "Elements" in fields.keys() and "Level" in fields.keys() and "Burn" in fields.keys():
		return True
	return False

def talent_parse_function(field):
	functions = {
		'element': default_closure('element'),
		'elements': default_closure('elements'),
		'type': default_closure('talent_type'),
		'level': default_closure('level'),
		'burn': default_closure('burn'),
		'blast type': default_closure('blast_type'),
		'damage': default_closure('damage'),
		'prerequisite': default_closure('prerequisites'),
		'prerequisites': default_closure('prerequisites'),
		'associated blasts': default_closure('associated_blasts'),
		'saving throw': default_closure('saving_throw'),
		'spell resistance': default_closure('spell resistance'),
		'': default_closure(''),
	}
	return functions[field.lower()]

def parse_talent(sb, book):
	spell = parse_section(sb, book, keys=False)
	spell['type'] = 'talent'
	for key, value in sb.keys:
		talent_parse_function(key)(spell, value)
	return spell

