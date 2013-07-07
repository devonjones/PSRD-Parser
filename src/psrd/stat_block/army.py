import re
from psrd.stat_block.utils import colon_filter, default_closure
from psrd.stat_block.section import parse_section
from psrd.universal import StatBlockHeading, StatBlockSection, filter_name

def is_army(sb, book):
	fields = dict(sb.keys)
	if fields.has_key('ACR') and fields.has_key('DV') and fields.has_key('OM'):
		return True
	return False

def army_parse_function(field):
	functions = {
		'cr': parse_xp,
		'descriptor': parse_descriptor,
		'hp': default_closure('hp'),
		'acr': default_closure('acr'),
		'dv': default_closure('dv'),
		'om': default_closure('om'),
		'special': default_closure('special'),
		'speed': default_closure('speed'),
		'consumption': default_closure('consumption'),
		'tactics': default_closure('tactics'),
		'note': default_closure('note'),
		'resources': default_closure('resources'),
	}
	return functions[field.lower()]

def parse_descriptor(army, value):
	descriptor, creature_type = value.split(' army of ')
	align, size = descriptor.split(' ')
	army['creature_type'] = creature_type
	army['alignment'] = align
	army['size'] = size

def parse_xp(army, value):
	if value.startswith('XP '):
		army['xp'] = value.replace('XP ', '')
	else:
		raise Exception("Unknown XP line: %s " % value)

def parse_army(sb, book):
	details = []
	for detail in sb.details:
		details.append(detail)
	sb.details = details
	army = parse_section(sb, book, keys=False)
	for key, value in sb.keys:
		army_parse_function(key)(army, value)
	army['type'] = 'army'
	return army

