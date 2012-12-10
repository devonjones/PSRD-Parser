import re
from psrd.stat_block.utils import colon_filter, default_closure
from psrd.stat_block.section import parse_section
from psrd.universal import StatBlockHeading, StatBlockSection, filter_name

def is_haunt(sb, book):
	fields = dict(sb.keys)
	if fields.has_key('Destruction'):
		if fields.has_key('Notice'):
			return True
	return False

def haunt_parse_function(field):
	functions = {
		'xp': parse_xp,
		'caster level': default_closure('caster_level'),
		'notice': default_closure('notice'),
		'hp': default_closure('hp'),
		'trigger': default_closure('trigger'),
		'reset': default_closure('reset'),
		'effect': default_closure('effect'),
		'destruction': default_closure('destruction'),
	}
	return functions[field.lower()]

def parse_xp(haunt, value):
	m = re.search(r'([LNC][GNE]?) ?([A-Za-z]* haunt) \((.*)\)', value)
	if m:
		haunt['alignment'] = m.group(1)
		haunt['haunt_type'] = m.group(2).strip()
		haunt['area'] = m.group(3)
	else:
		haunt['xp'] = value

def parse_haunt(sb, book):
	details = []
	for detail in sb.details:
		details.append(detail)
	sb.details = details
	haunt = parse_section(sb, book, keys=False)
	for key, value in sb.keys:
		haunt_parse_function(key)(haunt, value)
	haunt['type'] = 'haunt'
	if 'CR' in haunt['name']:
		names = haunt['name'].split('CR')
		haunt['name'] = filter_name(names.pop(0).strip())
		haunt['cr'] = int(names.pop(0).strip())
	return haunt

