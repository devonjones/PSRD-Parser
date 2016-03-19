from psrd.sections import cap_words
from psrd.stat_block.utils import colon_filter, default_closure, noop
from psrd.stat_block.utils import parse_stat_block, collapse_text, has_heading
from psrd.stat_block.utils import  sections_pass
from psrd.universal import StatBlockSection, Heading, filter_name
from psrd.universal import title_collapse_pass

def is_npc(sb, book):
	if is_creature(sb, book):
		for detail in sb.details:
			if detail.__class__ == StatBlockSection and detail.name.lower(
					).strip() in ['boon']:
				return True
	return False

def is_creature(sb, book):
	for detail in sb.details:
		if detail.__class__ == StatBlockSection and detail.name.lower(
				).strip() in ['ecology', 'statistics']:
			return True
	return False

def parse_npc(sb, book):
	npc = parse_creature(sb, book)
	npc['subtype'] = 'npc'
	return npc

def parse_creature(sb, book):
	name = sb.name
	cr = None
	if name.find('CR') > -1:
		name, cr = name.split('CR')
	creature = {'type': 'creature', 'source': book, 'name': filter_name(name)}
	if cr:
		creature['cr'] = cr.strip()
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
		if detail.name.lower() == 'base statistics':
			detail.name = 'Statistics'
		if detail.name.lower() == 'environment':
			detail.name = 'Ecology'
		if detail.__class__ == StatBlockSection and detail.name.lower() in [
				'defense', 'offense', 'statistics', 'ecology']:
			for key, value in detail.keys:
				creature_parse_function(key)(creature, value)
			for subd in detail.details:
				if isinstance(subd, dict) or isinstance(subd, Heading):
					sections.append(subd)
				else:
					newsec = {
						'type': 'section',
						'source': book,
						'text': unicode(subd)}
					sections.append(newsec)
		elif detail.__class__ == StatBlockSection and detail.name.lower() in [
				'special abilities']:
			special_abilities = {
					'type': 'section',
					'subtype': 'special_abilities',
					'source': book,
					'name': 'Special Abilities',
					'sections': []}
			for key in detail.keys:
				newsec = {
						'type': 'section',
						'source': book,
						'name': key[0],
						'text': key[1]}
				special_abilities['sections'].append(newsec)
			sections.append(special_abilities)
			for subd in detail.details:
				if isinstance(subd, dict) or isinstance(subd, Heading):
					sections.append(subd)
				else:
					newsec = {
							'type': 'section',
							'source': book,
							'text': unicode(subd)}
					sections.append(newsec)
		elif detail.__class__ == StatBlockSection and detail.name.lower() in [
				'tactics']:
			sections.append(parse_stat_block(detail, book, no_sb=True))
		else:
			if isinstance(detail, dict) or isinstance(detail, Heading):
				text.append(detail)
			else:
				text.append(unicode(detail))
	if len(text) > 0:
		collapse_text(creature, text)
	if len(sections) > 0:
		level = has_heading(sections)
		while level:
			sections = title_collapse_pass(sections, level)
			level = level - 1
		if level == 0:
			sections = sections_pass(sections, creature['source'])
		creature['sections'] = sections
	return creature

def creature_parse_function(field):
	functions = {
		'cr': parse_cr,
		'size': default_closure('size'),
		'hit dice': default_closure('hit_dice'),
		'natural armor': default_closure('natural_armor'),
		'breath weapon': default_closure('breath_weapon'),

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
		'resist': default_closure('resist'),
		'sr': default_closure('sr'),
		'weaknesses': default_closure('weaknesses'),
		'vulnerability': default_closure('weaknesses'),
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
		'spell-like ability': creature_spell_closure('spell-like abilities'),
		'bloodline spell-like ability': creature_spell_closure(
			'bloodline spell-like ability'),
		'bloodline spell-like abilities': creature_spell_closure(
			'bloodline spell-like abilities'),
		'arcane spell-like abilities': creature_spell_closure(
			'arcane spell-like abilities'),
		'arcane school spell-like abilities': creature_spell_closure(
			'arcane school spell-like abilities'),
		'domain spell-like abilities': creature_spell_closure(
			'domain spell-like abilities'),
		'ifrit spell-like abilities': creature_spell_closure(
				'ifrit spell-like abilities'),
		'gnome spell-like abilities': creature_spell_closure(
				'gnome spell-like abilities'),
		'sorcerer spell-like abilities': creature_spell_closure(
				'sorcerer spell-like abilities'),
		'antipaladin spell-like abilities': creature_spell_closure(
				'antipaladin spell-like abilities'),
		'paladin spell-like abilities': creature_spell_closure(
				'paladin spell-like abilities'),
		'rogue spell-like abilities': creature_spell_closure(
				'rogue spell-like abilities'),
		'conjurer spell-like abilities': creature_spell_closure(
				'conjurer spell-like abilities'),
		'transmuter spell-like abilities': creature_spell_closure(
				'transmuter spell-like abilities'),
		'enchanter spell-like abilities': creature_spell_closure(
				'enchanter spell-like abilities'),
		'evoker spell-like abilities': creature_spell_closure(
				'evoker spell-like abilities'),
		'dragon disciple spell-like abilities': creature_spell_closure(
				'dragon disciple spell-like abilities'),
		'shadowdancer spell-like abilities': creature_spell_closure(
				'shadowdancer spell-like abilities'),
		'devilbound spell-like abilities': creature_spell_closure(
				'devilbound spell-like abilities'),
		'gathlain spell-like abilities': creature_spell_closure(
				'gathlain spell-like abilities'),
		'kitsune spell-like abilities': creature_spell_closure(
				'kitsune spell-like abilities'),
		'wayang spell-like abilities': creature_spell_closure(
				'wayang spell-like abilities'),
		'utility spell-like abilities': creature_spell_closure(
				'utility spell-like abilities'),
		'defensive spell-like abilities': creature_spell_closure(
				'defensive spell-like abilities'),
		'attack spell-like abilities': creature_spell_closure(
				'attack spell-like abilities'),

		'spells prepared': creature_spell_closure('spells prepared'),
		'alchemist extracts prepared': creature_spell_closure(
				'alchemist extracts prepared'),
		'adept spells prepared': creature_spell_closure(
				'adept spells prepared'),
		'bard spells prepared': creature_spell_closure(
				'bard spells prepared'),
		'cleric spells prepared': creature_spell_closure(
				'cleric spells prepared'),
		'conjurer spells prepared': creature_spell_closure(
				'conjurer spells prepared'),
		'druid spells prepared': creature_spell_closure(
				'druid spells prepared'),
		'magus spells prepared': creature_spell_closure(
				'magus spells prepared'),
		'antipaladin spells prepared': creature_spell_closure(
				'antipaladin spells prepared'),
		'paladin spells prepared': creature_spell_closure(
				'paladin spells prepared'),
		'ranger spells prepared': creature_spell_closure(
				'ranger spells prepared'),
		'witch spells prepared': creature_spell_closure(
				'witch spells prepared'),
		'wizard spells prepared': creature_spell_closure(
				'wizard spells prepared'),
		'necromancer spells prepared': creature_spell_closure(
				'necromancer spells prepared'),
		'enchanter spells prepared': creature_spell_closure(
				'enchanter spells prepared'),
		'diviner spells prepared': creature_spell_closure(
				'diviner spells prepared'),
		'transmuter spells prepared': creature_spell_closure(
				'transmuter spells prepared'),
		'evoker spells prepared': creature_spell_closure(
				'evoker spells prepared'),
		'illusionist spells prepared': creature_spell_closure(
				'illusionist spells prepared'),
		'abjurer spells prepared': creature_spell_closure(
				'abjurer spells prepared'),
		'utility spells': creature_spell_closure(
				'utility spells'),
		'utility options': creature_spell_closure(
				'utility options'),
		'defensive spells': creature_spell_closure(
				'defensive spells'),
		'attack spells': creature_spell_closure(
				'attack spells'),

		'spells known': creature_spell_closure('spells known'),
		'bard spells known': creature_spell_closure('bard spells known'),
		'inquisitor spells known': creature_spell_closure(
				'inquisitor spells known'),
		'oracle spells known': creature_spell_closure('oracle spells known'),
		'sorcerer spells known': creature_spell_closure(
				'sorcerer spells known'),

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
		'concentration': default_closure('concentration'),
		'feats': default_closure('feats'),
		'skills': default_closure('skills'),
		'racial modifiers': default_closure('racial_modifiers'),
		'racial modifier': default_closure('racial_modifiers'),
		'languages': default_closure('languages'),
		'language': default_closure('languages'),
		'gear': default_closure('gear'),
		'combat gear': default_closure('combat_gear'),
		'other gear': default_closure('other_gear'),
		'boon': default_closure('boon'),

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

def parse_cr(sb, value):
	try:
		v = int(value)
		sb['cr'] = value
		return
	except:
		pass
	if value.startswith('CR '):
		mr = None
		cr = value
		if cr.find('/MR') > -1:
			cr, mr = cr.split('/MR')
		if mr:
			sb['mr'] = mr.strip()
		sb['cr'] = cr.replace('CR ', '')
	else:
		raise Exception("Unknown CR line: %s " % value)

def creature_spell_closure(field):
	def fxn(sb, value):
		value = colon_filter(value)
		value = value.replace('&ndash;', '-')
		value = value.replace('&mdash;', '-')
		spells = sb.setdefault('spells', {})
		spells[field] = value
	return fxn

def parse_broken_environment(sb, value):
	sb['environment'] = 'any'

def xp_closure(field):
	def fxn(sb, value):
		sb['xp'] = value.replace('XP', '').strip()
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
				if second == "animal companion":
					creature['super_race'] = second
				else:
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
	print "%s: %s" %(creature, value)
	if value.startswith('AC'):
		default_closure('ac')(creature, value[2:])
		return
	bsb = None
	if value.find('(but see below) ') > -1:
		value = value.replace('(but see below) ', '')
		bsb = " (but see below)"
	any_al = None
	if value.find('Any alignment (same as creator)') > -1:
		any_al = 'Any alignment (same as creator)'
		value = value.replace(any_al, 'Any')
	descsplit = value.split("(")
	if len(descsplit) > 1:
		value = descsplit.pop(0)
		subtype = ''.join(descsplit)
		subtype = subtype.replace(')', '')
		creature['creature_subtype'] = subtype
	values = value.split()
	if len(values) == 2:
		creature['alignment'] = values.pop(0)
		creature['creature_type'] = cap_words(values.pop(0))
	elif len(values) >= 3:
		creature['alignment'] = values.pop(0)
		if any_al:
			creature['alignment'] = any_al
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
		creature['creature_type'] = cap_words(values.pop(0))
	if len(values) > 0:
		if values[0] in ['beast', 'humanoid']:
			creature['creature_type'] = creature['creature_type'] + \
				" " + cap_words(values.pop(0))
	if len(values) > 0:
		raise Exception('well fuck: %s' %(values))

