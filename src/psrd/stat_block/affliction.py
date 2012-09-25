from psrd.stat_block.utils import colon_filter, default_closure
from psrd.stat_block.section import parse_section

def is_affliction(sb, book):
	fields = dict(sb.keys)
	if fields.has_key('Type'):
		if fields.has_key('Cure') or fields.has_key('Frequency') or fields.has_key('Effect') or fields.has_key('Onset'):
			return True
		if fields.has_key('Addiction'):
			return True
	return False

def affliction_parse_function(field):
	functions = {
		'type': parse_affliction_type,
		'addiction': parse_addiction,
		'price': default_closure('price'),
		'damage': default_closure('damage'),
		'save': default_closure('save'),
		'frequency': default_closure('frequency'),
		'effect': default_closure('effect'),
		'effects': default_closure('effect'),
		'cure': default_closure('cure'),
		'onset': default_closure('onset'),
		'initial effect': default_closure('initial_effect'),
		'secondary effect': default_closure('secondary_effect'),
	}
	return functions[field.lower()]

def parse_addiction(affliction, value):
	affliction['contracted'] = affliction['subtype']
	affliction['subtype'] = 'addiction'
	affliction['addiction'] = value

def parse_affliction_type(affliction, value):
	values = value.split(", ")
	affliction['subtype'] = values.pop(0)
	if len(values) > 0:
		affliction['contracted'] = ', '.join(values).strip()

def parse_affliction(sb, book):
	affliction = parse_section(sb, book, keys=False)
	affliction['type'] = 'affliction'
	for key, value in sb.keys:
		affliction_parse_function(key)(affliction, value)
	return affliction 
