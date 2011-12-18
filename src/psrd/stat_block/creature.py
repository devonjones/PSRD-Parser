from psrd.stat_block.utils import colon_filter, default_closure, noop
from psrd.universal import StatBlockSection, filter_name

def is_creature(sb, book):
	fields = dict(sb.keys)
	for detail in sb.details:
		if detail.__class__ == StatBlockSection and detail.name.lower().strip() in ['ecology', 'statistics']:
			return True
	return False

def parse_creature(sb, book):
	names = sb.name.split('CR')
	creature = {'type': 'creature', 'source': book, 'name': filter_name(names[0])}
	if len(names) > 1:
		creature['cr'] = names[1].strip()
	sections = []
	text = []
	descriptors = []
	for tup in sb.keys:
		if tup[0] == 'descriptor':
			descriptors.append(tup)
	for tup in descriptors:
		sb.keys.remove(tup)
	if len(descriptors) > 0:
		parse_creature_descriptors(creature, descriptors)
	
	for key, value in sb.keys:
		creature_parse_function(key)(creature, value)
	for detail in sb.details:
		if detail.__class__ == StatBlockSection and detail.name.lower() in ['defense', 'offense', 'statistics', 'ecology']:
			for key, value in detail.keys:
				creature_parse_function(key)(creature, value)
			for subd in detail.details:
				newsec = {'type': 'section', 'source': book, 'text': unicode(subd)}
				sections.append(newsec)
		elif detail.__class__ == StatBlockSection and detail.name.lower() in ['special abilities']:
			special_abilities = {'type': 'section', 'subtype': 'special_abilities', 'source': book, 'name': 'Special Abilities', 'sections': []}
			for key in detail.keys:
				newsec = {'type': 'section', 'source': book, 'name': key[0], 'text': key[1]}
				special_abilities['sections'].append(newsec)
			sections.append(special_abilities)
			for subd in detail.details:
				newsec = {'type': 'section', 'source': book, 'text': unicode(subd)}
				sections.append(newsec)
		else:
			text.append(unicode(detail))
	if len(text) > 0:
		creature['text'] = ''.join(text)
	if len(sections) > 0:
		creature['sections'] = sections
	return creature

def creature_parse_function(field):
	functions = {
		'xp': default_closure('xp'),
		'init': default_closure('init'),
		'senses': default_closure('senses'),
		'perception': perception_fix,
		'aura': default_closure('aura'),

		'ac': default_closure('ac'),
		'hp': default_closure('hp'),
		'fort': default_closure('fortitude'),
		'ref': default_closure('reflex'),
		'will': default_closure('will'),
		'defensive abilities': default_closure('defensive_abilities'),
		'defensive ability': default_closure('defensive_abilities'),
		'dr': default_closure('dr'),
		'immune': default_closure('immune'),
		'vulnerability': default_closure('vulnerability'),
		'resist': default_closure('resist'),
		'sr': default_closure('sr'),
		'weaknesses': default_closure('weaknesses'),
		'weakness': default_closure('weaknesses'),
		'sq': default_closure('special_qualities'),
		'special qualities': default_closure('special_qualities'),

		'speed': default_closure('speed'),
		'melee': default_closure('melee'),
		'ranged': default_closure('ranged'),
		'special attacks': default_closure('special_attacks'),
		'special attack': default_closure('special_attacks'),
		'attacks': default_closure('special_attacks'),

		'spell-like abilities': creature_spell_closure('spell-like abilities'),
		'spell-lilke abilities': creature_spell_closure('spell-like abilities'),
		'bloodline spell-like ability': creature_spell_closure('bloodline spell-like ability'),
		'ifrit spell-like abilities': creature_spell_closure('ifrit spell-like abilities'),
		'arcane school spell-like abilities': creature_spell_closure('arcane school spell-like abilities'),
		'spells prepared': creature_spell_closure('spells prepared'),
		'cleric spells prepared': creature_spell_closure('cleric spells prepared'),
		'ranger spells prepared': creature_spell_closure('ranger spells prepared'),
		'spells known': creature_spell_closure('spells known'),
		'sorcerer spells known': creature_spell_closure('sorcerer spells known'),
		'opposition schools': creature_spell_closure('opposition schools'),
		'd': creature_spell_closure('d'),
		'domains': creature_spell_closure('domains'),
		'domain spell-like abilities': creature_spell_closure('domain spell-like abilities'),
		'conjurer spells prepared': creature_spell_closure('conjurer spells prepared'),
		'sorcerer spell-like abilities': creature_spell_closure('sorcerer spell-like abilities'),
		'bloodline': creature_spell_closure('bloodline'),

		'str': default_closure('strength'),
		'dex': default_closure('dexterity'),
		'con': default_closure('constitution'),
		'int': default_closure('intelligence'),
		'wis': default_closure('wisdom'),
		'cha': default_closure('charisma'),
		'base atk': default_closure('base_attack'),
		'atk': default_closure('base_attack'),
		'cmb': default_closure('cmb'),
		'cmd': default_closure('cmd'),
		'feats': default_closure('feats'),
		'skills': default_closure('skills'),
		'racial modifiers': default_closure('racial_modifiers'),
		'racial modifier': default_closure('racial_modifiers'),
		'languages': default_closure('languages'),
		'language': default_closure('languages'),
		'gear': default_closure('gear'),

		'space': default_closure('space'),
		'reach': default_closure('reach'),

		'environment': default_closure('environment'),
		'environment any': parse_broken_environment,
		'organization': default_closure('organization'),
		'treasure': default_closure('treasure'),
		'base': noop,
		'special': noop,
		'descriptor': parse_creature_descriptor
	}
	if field.lower().startswith('xp'):
		return xp_closure('field')
	return functions[field.lower()]

def creature_spell_closure(field):
	def fxn(sb, value):
		value = colon_filter(value)
		value = value.replace('&ndash;', '-')
		spells = sb.setdefault('spells', {})
		spells[field] = value
	return fxn

def parse_broken_environment(sb, value):
	sb['environment'] = 'any'

def xp_closure(field):
	def fxn(sb, value):
		values = field.split(' ')
		values.pop(0)
		sb['xp'] = ' '.join(values).strip()
	return fxn

def perception_fix(sb, value):
	sb['senses'] = sb['senses'] + "; Perception " + value

def parse_creature_classes(creature, value):
	name = creature['name'].split("(")[0].strip().lower()
	values = value.lower().split(name)
	if len(values) == 2:
		first = values[0].strip()
		second = values[1].strip()
		if len(first) > 0:
			parse_super_race(creature, first)
		if len(second) > 0:
			second = second.split("(")[0].strip()
			parts = second.split(" ")
			try:
				int(parts[-1])
				creature['level'] = second
			except ValueError:
				raise Exception("Not a level, not sure what to do: %s" % second)
	elif len(values) == 1:
		parse_super_race(creature, values[0])
	else:
		raise Exception("Not sure what to do here: %s" % value)

def parse_super_race(creature, snippet):
	fields = snippet.split(' ')
	sr = []
	for field in fields:
		if field in ['male', 'female']:
			creature['sex'] = field
		else:
			sr.append(field)
	if len(sr) > 0:
		creature['super_race'] = ' '.join(sr)

def parse_creature_descriptors(creature, value):
	real = []
	for tup in value:
		key, val = tup
		if val.startswith('AC'):
			default_closure('ac')(creature, val[2:])
		else:
			real.append(val)
	parse_creature_descriptor(creature, real.pop())
	if len(real) > 0:
		parse_creature_classes(creature, real.pop(0))
	if len(real) > 0:
		raise Exception("Too many descriptors: %s" % value)

def parse_creature_descriptor(creature, value):
	if value.startswith('AC'):
		default_closure('ac')(creature, value[2:])
		return
	bsb = None
	if value.find('(but see below) ') > -1:
		value = value.replace('(but see below) ', '')
		bsb = " (but see below)"
	descsplit = value.split("(")
	if len(descsplit) > 1:
		value = descsplit.pop(0)
		subtype = ''.join(descsplit)
		subtype.replace(')', '')
		creature['creature_subtype'] = subtype
	values = value.split()
	if len(values) == 2:
		creature['alignment'] = values.pop(0)
		creature['creature_type'] = values.pop(0)
	elif len(values) >= 3:
		creature['alignment'] = values.pop(0)
		if values[0] == 'alignment':
			creature['alignment'] = creature['alignment'] + " " + values.pop(0)
		if bsb:
			creature['alignment'] = creature['alignment'] + bsb
		if values[0] == 'or':
			alignment = creature['alignment']
			alignment = alignment + " " + values.pop(0)
			alignment = alignment + " " + values.pop(0)
			creature['alignment'] = alignment
		creature['size'] = values.pop(0)
		creature['creature_type'] = values.pop(0)
	if len(values) > 0:
		if values[0] in ['beast', 'humanoid']:
			creature['creature_type'] = creature['creature_type'] + " " + values.pop(0)
	if len(values) > 0:
		raise Exception('well fuck: %s' %(values))

