from psrd.universal import StatBlockHeading, StatBlockSection

def default_closure(field):
	def fxn(companion, value):
		companion[field] = value
	return fxn

def parse_function(field):
	functions = {
		'ac': default_closure('ac'),
		'attack': default_closure('attack'),
		'ability scores': default_closure('ability_score'),
		'special qualities': default_closure('special_qualities'),
		'special attacks': default_closure('special_attacks'),
		'size': default_closure('size'),
		'speed': default_closure('speed')
	}
	return functions[field.lower()]

def is_animal_companion(sb):
	fields = dict(sb.keys)
	if fields.has_key('AC'):
		for detail in sb.details:
			if detail.__class__ == StatBlockSection and detail.name.endswith('th-Level Advancement'):
				return True
	return False

def parse_animal_companion(sb, book):
	ac = {'type': 'animal_companion', 'source': book, 'name': sb.name, 'advancement': []}
	text = []
	for key, value in sb.keys:
		parse_function(key)(ac, value)
	for detail in sb.details:
		if detail.__class__ == StatBlockSection and detail.name.endswith('th-Level Advancement'):
			advancement = {'level': detail.name}
			for key, value in detail.keys:
				parse_function(key)(advancement, value)
			ac['advancement'].append(advancement)
		else:
			text.append(detail)
	if len(text) > 0:
		ac['text'] = ''.join(text)
	return ac

def parse_stat_block(sb, book):
	if is_animal_companion(sb):
		return parse_animal_companion(sb, book)
	return sb

def stat_block_pass(section, book):
	if section.has_key('sections'):
		newsections = []
		for s in section['sections']:
			if s.__class__ == StatBlockHeading:
				newsections.append(parse_stat_block(s, book))
			elif s.__class__ == dict:
				newsections.append(stat_block_pass(s, book))
			else:
				newsections.append(s)
		section['sections'] = newsections
	return section

