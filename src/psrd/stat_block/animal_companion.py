from psrd.stat_block.utils import colon_filter, default_closure
from psrd.universal import StatBlockSection, filter_name

def is_animal_companion(sb, book):
	fields = dict(sb.keys)
	if fields.has_key('AC'):
		for detail in sb.details:
			if detail.__class__ == StatBlockSection and detail.name.endswith('th-Level Advancement'):
				return True
		if fields.has_key('Ability Scores'):
			return True
	return False

def animal_companion_parse_function(field):
	functions = {
		'ac': default_closure('ac'),
		'attack': default_closure('attack'),
		'ability scores': default_closure('ability_scores'),
		'special qualities': default_closure('special_qualities'),
		'special attacks': default_closure('special_attacks'),
		'size': default_closure('size'),
		'speed': default_closure('speed')
	}
	return functions[field.lower()]

def parse_animal_companion(sb, book):
	ac = {'type': 'animal_companion', 'source': book, 'name': filter_name(sb.name.strip()), 'sections': []}
	text = []
	for key, value in sb.keys:
		animal_companion_parse_function(key)(ac, value)
	for detail in sb.details:
		if detail.__class__ == StatBlockSection and detail.name.endswith('th-Level Advancement'):
			advancement = {'level': detail.name, 'source': book, 'type': 'animal_companion', 'name': filter_name(ac['name'])}
			for key, value in detail.keys:
				animal_companion_parse_function(key)(advancement, value)
			ac['sections'].append(advancement)
		else:
			text.append(detail)
	if len(text) > 0:
		ac['text'] = ''.join(text)
	return ac

