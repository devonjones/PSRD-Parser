import re
from psrd.stat_block.utils import colon_filter, default_closure
from psrd.stat_block.section import parse_section
from psrd.universal import filter_name

def is_mythic_spell(sb, book):
	fields = dict(sb.keys)
	if set(fields.keys()) == set(['Source']):
		return True
	return False

def mythic_spell_parse_function(field):
	functions = {
		'source': default_closure('spell_source'),
	}
	return functions[field.lower()]

def parse_mythic_spell(sb, book):
	spell = parse_section(sb, book, keys=False)
	spell['type'] = 'mythic_spell'
	for key, value in sb.keys:
		mythic_spell_parse_function(key)(spell, value)
	return spell

