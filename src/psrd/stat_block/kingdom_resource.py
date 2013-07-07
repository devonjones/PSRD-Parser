import re
from psrd.stat_block.utils import colon_filter, default_closure
from psrd.stat_block.section import parse_section
from psrd.universal import StatBlockHeading, StatBlockSection, filter_name

def is_kingdom_resource(sb, book):
	fields = dict(sb.keys)
	if fields.has_key('Kingdom'):
		return True
	if fields.has_key('CR') and fields.has_key('Special'):
		return True
	return False

def kingdom_resource_parse_function(field):
	functions = {
		'cr': parse_cr,
		'kingdom': default_closure('kingdom'),
		'discount': default_closure('discount'),
		'upgrades from': default_closure('upgrade_from'),
		'upgrade from': default_closure('upgrade_from'),
		'upgrades to': default_closure('upgrade_to'),
		'upgrade to': default_closure('upgrade_to'),
		'magic items': default_closure('magic_items'),
		'settlement': default_closure('settlement'),
		'special': default_closure('special'),
		'limit': default_closure('limit'),
	}
	return functions[field.lower()]

def parse_cr(kingdom_resource, value):
	for part in value.split(", "):
		if part.endswith(" BP"):
			kingdom_resource['bp'] = part.replace(" BP", "")
		elif part.endswith(" lot"):
			kingdom_resource['lot'] = part.replace(" lot", "")
		elif part.endswith(" lots"):
			kingdom_resource['lot'] = part.replace(" lots", "")
		else:
			raise Exception("Unknown BP line: %s " % value)

def parse_kingdom_resource(sb, book):
	details = []
	for detail in sb.details:
		details.append(detail)
	sb.details = details
	kingdom_resource = parse_section(sb, book, keys=False)
	for key, value in sb.keys:
		kingdom_resource_parse_function(key)(kingdom_resource, value)
	kingdom_resource['type'] = 'kingdom_resource'
	return kingdom_resource

