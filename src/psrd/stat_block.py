import re
from BeautifulSoup import BeautifulSoup
from psrd.universal import StatBlockHeading, StatBlockSection, Heading, filter_name

def colon_filter(value):
	if value.startswith(":"):
		value = value[1:]
	return value.strip()

def default_closure(field):
	def fxn(sb, value):
		value = colon_filter(value)
		value = value.replace('&ndash;', '-')
		sb[field] = value
	return fxn

def is_animal_companion(sb):
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

def is_spell(sb):
	fields = dict(sb.keys)
	if "Spell Resistance" in fields.keys() or "School" in fields.keys():
		return True
	if "Level" in fields.keys():
		return True
	return False

def spell_parse_function(field):
	functions = {
		'school': parse_school,
		'level': parse_level,
		'components': parse_components,
		'component': parse_components,
		'saving throw': parse_saving_throw,
		'saving': parse_saving_throw,
		'save': parse_saving_throw,
		'casting time': parse_casting_time,
		'casting': parse_casting_time,
		'preparation time': default_closure('preparation_time'),
		'range': default_closure('range'),
		'duration': default_closure('duration'),
		'spell resistance': default_closure('spell_resistance'),
		'sr': default_closure('spell_resistance'),
		'effect': effect_closure('Effect'),
		'targets': effect_closure('Targets'),
		'target': effect_closure('Target'),
		'area': effect_closure('Area'),
		'target or area': effect_closure('Target or Area'),
		'area or target': effect_closure('Target or Area'),
		'target or targets': effect_closure('Target or Targets'),
		'target, effect, or area': effect_closure('Target, Effect, or Area'),
		'target, effect, area': effect_closure('Target, Effect, or Area'),
		'target/effect': effect_closure('Target or Effect'),
		'fortitude': icy_prison_fuckup,
	}
	return functions[field.lower()]

def parse_spell(sb, book):
	spell = parse_section(sb, book)
	spell['type'] = 'spell'
	for key, value in sb.keys:
		spell_parse_function(key)(spell, value)
	return spell

def icy_prison_fuckup(spell, value):
	parse_saving_throw(spell, "Reflex partial, Fortitude negates (see text)", override=True)

def effect_closure(field):
	def fxn(spell, value):
		value = colon_filter(value)
		effect = spell.setdefault('effects', [])
		effect.append({'name': filter_name(field), 'text': value})
	return fxn

def parse_casting_time(spell, value):
	value = colon_filter(value)
	if value.find('Time ') == 0:
		value = value.replace('Time', '')
	spell['casting_time'] = value

def parse_saving_throw(spell, value, override=False):
	value = colon_filter(value)
	if value.find('Throw ') == 0:
		value = value.replace('Throw ', '')
	if spell.has_key('saving_throw') and override:
		spell['saving_throw'] = value
	elif not spell.has_key('saving_throw'):
		spell['saving_throw'] = value

def parse_components(spell, value):
	value = colon_filter(value)
	m = re.search('\(.*?[^\)],.*?\)', value)
	while m:
		value = re.sub(r"\((.*?)[^\)],(.*?)\)", r"(\1|\2)", value)
		m = re.search('\(.*?[^\)],.*?\)', value)
	comps = value.split(', ')
	finalcomps = []
	for comp in comps:
		if comp.find('(') > -1:
			m = re.search('(.*) \((.*)\)', comp)
			name = m.group(1)
			comments = m.group(2)
			comments = comments.replace('|', ',')
			finalcomps.append({'type': name, 'text': comments})
		else:
			finalcomps.append({'type': comp})
	spell['components'] = finalcomps

def parse_school(spell, value):
	value = value.replace(';', '')
	value = colon_filter(value)
	m = re.search('\((.*)\)', value)
	if m:
		spell['subschool'] = m.group(1)
		value= re.sub('\(.*\)', '', value)
	m = re.search('\[(.*)\]', value)
	if m:
		descriptor = m.group(1)
		spell['descriptor'] = descriptor.split(', ')
		value = re.sub('\[.*\]', '', value)
	spell['school'] = value.strip()

def parse_level(spell, value):
	value = colon_filter(value)
	if value.find(";"):
		value = value.replace(";", ",")
	levels = value.split(', ')
	finallevels = []
	for level in levels:
		m = re.search('(.*) (\d*)', level)
		c = m.group(1)
		l = int(m.group(2))
		if c.lower().strip() == 'sorcerer/wizard':
			finallevels.append({'class': 'sorcerer', 'level': l})
			finallevels.append({'class': 'wizard', 'level': l})
		elif c.lower().strip() == 'cleric':
			finallevels.append({'class': 'cleric', 'level': l})
			finallevels.append({'class': 'oracle', 'level': l})
		else:
			finallevels.append({'class': c, 'level': l})
	spell['level'] = finallevels

def is_trap(sb, book):
	fields = dict(sb.keys)
	if fields.has_key('Disable Device'):
		# It's a trap!!!
		return True
	if book == 'Ultimate Magic' and sb.name.find('Trap') > -1:
		return True
	return False

def trap_parse_function(field):
	functions = {
		'type': default_closure('trap_type'),
		'perception': default_closure('perception'),
		'disable device': default_closure('disable_device'),
		'duration': default_closure('duration'),
		'effect': default_closure('effect'),
		'trigger': default_closure('trigger'),
		'reset': default_closure('reset'),
	}
	return functions[field.lower()]

def parse_trap(sb, book):
	details = []
	for detail in sb.details:
		if detail.__class__ in (StatBlockHeading, StatBlockSection) and detail.name == 'Effects':
			sb.keys.extend(detail.keys)
			details.extend(detail.details)
		else:
			details.append(detail)
	sb.details = details
	trap = parse_section(sb, book)
	for key, value in sb.keys:
		trap_parse_function(key)(trap, value)
	trap['type'] = 'trap'
	if 'CR' in trap['name']:
		names = trap['name'].split('CR')
		trap['name'] = filter_name(names.pop(0).strip())
		trap['cr'] = int(names.pop(0).strip())
	return trap

def is_affliction(sb):
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
	affliction = parse_section(sb, book)
	affliction['type'] = 'affliction'
	for key, value in sb.keys:
		affliction_parse_function(key)(affliction, value)
	return affliction 

def is_item(sb, book):
	fields = dict(sb.keys)
	if fields.has_key('Aura') or fields.has_key('Price') or fields.has_key('Cost'):
		if fields.has_key('Slot') or fields.has_key('CL') or fields.has_key('Requirements'):
			return True
	return False

def parse_item_slot(item, value):
	item['slot'] = value
	if value in ['armor', 'arms', 'belt', 'body', 'chest', 'eyes', 'feet', 'hands', 'head', 'headband', 'neck', 'ring', 'shield', 'shoulders', 'wrist', 'wrists']:
		if value == 'wrists':
			item['subtype'] = 'wrist'
		else:
			item['subtype'] = value

def item_parse_function(field):
	functions = {
		'aura': default_closure('aura'),
		'cl': default_closure('cl'),
		'slot': parse_item_slot,
		'price': default_closure('price'),
		'skill': default_closure('skill'),
		'weight': default_closure('weight'),
		'requirements': default_closure('requirements'),
		'cr increase': default_closure('cr_increase'),
		'cost': default_closure('cost'),
	}
	return functions[field.lower()]

def parse_item(sb, book):
	item = {'type': 'item', 'source': book, 'name': filter_name(sb.name.strip())}
	text = []
	for key, value in sb.keys:
		item_parse_function(key)(item, value)
	for detail in sb.details:
		if detail.__class__ == StatBlockSection and detail.name == "Construction":
			for key, value in detail.keys:
				item_parse_function(key)(item, value)
		elif detail.__class__ == StatBlockSection:
			sections = item.setdefault('sections', [])
			sections.append(parse_section(detail, book))
		else:
			text.append(unicode(detail))
	if len(text) > 0:
		item['text'] = ''.join(text)
	return item 

def is_settlement(sb, book):
	fields = dict(sb.keys)
	if fields.has_key('Corruption'):
		if fields.has_key('Crime'):
			return True
	return False

def parse_settlement(sb, book):
	settlement = {'type': 'settlement', 'source': book, 'name': filter_name(sb.name.strip())}
	text = []
	for key, value in sb.keys:
		settlement_parse_function(key)(settlement, value)
	for detail in sb.details:
		for key, value in detail.keys:
			settlement_parse_function(key)(settlement, value)
		if len(detail.details) > 0:
			sections = settlement.setdefault('sections', [])
			sec = parse_section(detail, book)
			if sec['name'] == 'DEMOGRAPHICS':
				sec['name'] = 'Notable NPCs'
			sections.append(sec)
	return settlement

def parse_settlement_descriptor(settlement, value):
	values = value.split(' ')
	settlement['alignment'] = values.pop(0)
	settlement['settlement_type'] = values.pop()
	if len(values) > 0:
		settlement['size'] = values.pop(0)
	if len(values) > 0:
		raise Exception("Unexpected values still in settlement descriptor: %s" % values)

def settlement_parse_function(field):
	functions = {
		'descriptor': parse_settlement_descriptor,
		'corruption': default_closure('corruption'),
		'crime': default_closure('crime'),
		'economy': default_closure('economy'),
		'law': default_closure('law'),
		'lore': default_closure('lore'),
		'society': default_closure('society'),
		'qualities': default_closure('qualities'),
		'danger': default_closure('danger'),
		'disadvantages': default_closure('disadvantages'),
		'government': default_closure('government'),
		'population': default_closure('population'),
		'notable npcs': noop,
		'base value': default_closure('base_value'),
		'purchase limit': default_closure('purchase_limit'),
		'spellcasting': default_closure('spellcasting'),
		'minor items': default_closure('minor_items'),
		'medium items': default_closure('medium_items'),
		'major items': default_closure('major_items'),
	}
	return functions[field.lower()]

def is_spellbook(sb, book):
	fields = dict(sb.keys)
	if book == 'Ultimate Magic':
		if fields.has_key('Value') or sb.name == 'Preparation Ritual':
			return True
	return False

def parse_spellbook(sb, book):
	newdetails = []
	for detail in sb.details:
		if hasattr(detail, 'level') and detail.level == 5:
			newdetails.append(detail.name)
		else:
			newdetails.append(detail)
	sb.details = newdetails
	section = parse_section(sb, book)
	for key in sb.keys:
		newsec = {'type': 'section', 'source': book, 'name': key[0], 'text': key[1]}
		sections = section.setdefault('sections', [])
		sections.insert(1, newsec)
	section['subtype'] = 'spellbook'
	return section

def is_section(sb, book):
	if len(sb.keys) == 0:
		return True
	return False

def parse_section(sb, book):
	section = {'type': 'section', 'source': book, 'name': filter_name(sb.name.strip())}
	text = []
	sections = []
	sectiontext = []
	ns = None
	for detail in sb.details:
		if detail.__class__ == StatBlockSection:
			sections.append(parse_stat_block(detail, book))
		elif detail.__class__ == StatBlockHeading:
			sections.append(parse_stat_block(sb, book))
		elif detail.__class__ == dict:
			if len(sectiontext) > 0:
				section['text'] = ''.join(sectiontext)
				sectiontext = []
				ns = None
			sections.append(detail)
		elif detail.__class__ == Heading:
			if len(sectiontext) > 0:
				ns['text'] = ''.join(sectiontext)
				sectiontext = []
			ns = {'type': 'section', 'source': book, 'name': filter_name(detail.name)}
			sections.append(ns)
		else:
			if len(sections) == 0:
				text.append(unicode(detail))
			else:
				if not ns:
					ns = {'type': 'section', 'source': book}
					sections.append(ns)
				sectiontext.append(unicode(detail))
	if len(text) > 0:
		section['text'] = ''.join(text)
	if len(sectiontext) > 0:
		ns['text'] = ''.join(sectiontext)
	if len(sections) > 0:
		section['sections'] = sections
	return section

def is_vehicle(sb, book):
	fields = dict(sb.keys)
	if fields.has_key('Squares'):
		if fields.has_key('Cost'):
			return True
	return False

def parse_vehicle(sb, book):
	vehicle = {'type': 'vehicle', 'source': book, 'name': filter_name(sb.name.strip())}
	text = []
	for key, value in sb.keys:
		vehicle_parse_function(key)(vehicle, value)
	for detail in sb.details:
		for key, value in detail.keys:
			vehicle_parse_function(key)(vehicle, value)
	return vehicle
	
def parse_vehicle_descriptor(vehicle, value):
	values = value.split(' ')
	vehicle['size'] = values.pop(0)
	vehicle['vehicle_type'] = values.pop(0)
	if len(values) > 1:
		values.pop(0)
		raise Exception("Unexpected values still in vehicle descriptor: %s" % values)

def vehicle_parse_function(field):
	functions = {
		'descriptor': parse_vehicle_descriptor,
		'squares': default_closure('squares'),
		'cost': default_closure('squares'),
		'ac': default_closure('ac'),
		'hardness': default_closure('hardness'),
		'hp': default_closure('hp'),
		'base save': default_closure('base_save'),
		'maximum speed': default_closure('maximum_speed'),
		'acceleration': default_closure('acceleration'),
		'cmb': default_closure('cmb'),
		'cmd': default_closure('cmd'),
		'ramming damage': default_closure('ramming_damage'),
		'propulsion': default_closure('propulsion'),
		'driving check': default_closure('driving_check'),
		'forward facing': default_closure('forward_facing'),
		'driving device': default_closure('driving_device'),
		'driving space': default_closure('driving_space'),
		'decks': default_closure('decks'),
		'deck': default_closure('decks'),
		'weapons': default_closure('weapons'),
		'crew': default_closure('crew'),
		'passengers': default_closure('passengers'),
	}
	return functions[field.lower()]

def is_creature(sb):
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

def noop(creature, value):
	print value

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

def is_creature_type(sb, book):
	if len(sb.keys) == 2:
		fields = dict(sb.keys)
		if fields.has_key('Traits') and fields.has_key('descriptor'):
			return True
	return False

def parse_creature_type(sb, book):
	section = {'type': 'section', 'subtype': 'creature_type', 'source': book, 'name': filter_name(sb.name.strip())}
	fields = dict(sb.keys)
	section['text'] = _list_text(fields['descriptor'])
	traits =  {'type': 'section', 'source': book, 'name': 'Traits'}
	traits['text'] = _list_text(fields['Traits'])
	section['sections'] = [traits]
	return section

def _list_text(text):
	num = text.find(u'\u2022')
	newtext = text[0:num] + "<ul><li>" + text[num + 1:]
	newtext = newtext.replace(u'\u2022', "</li><li>") + "</li></ul>"
	return newtext

def is_haunt(sb, book):
	fields = dict(sb.keys)
	if fields.has_key('Destruction'):
		if fields.has_key('Notice'):
			return True
	return False

def parse_haunt(sb, book):
	section = {'type': 'haunt', 'source': book, 'name': filter_name(''.join(sb.html.pop(0).findAll(text=True)))}
	section['body'] = ''.join([unicode(elem) for elem in sb.html])
	return section

def parse_stat_block(sb, book):
	if is_animal_companion(sb):
		return parse_animal_companion(sb, book)
	if is_creature(sb):
		return parse_creature(sb, book)
	elif is_spell(sb):
		return parse_spell(sb, book)
	elif is_trap(sb, book):
		return parse_trap(sb, book)
	elif is_affliction(sb):
		return parse_affliction(sb, book)
	elif is_item(sb, book):
		return parse_item(sb, book)
	elif is_creature_type(sb, book):
		return parse_creature_type(sb, book)
	elif is_spellbook(sb, book):
		return parse_spellbook(sb, book)
	elif is_vehicle(sb, book):
		return parse_vehicle(sb, book)
	elif is_settlement(sb, book):
		return parse_settlement(sb, book)
	elif is_haunt(sb, book):
		return parse_haunt(sb, book)
	elif is_section(sb, book):
		return parse_section(sb, book)
	else:
		print sb
		print sb.html
	return sb

def stat_block_pass(section, book):
	if section.__class__ == dict:
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
	return parse_stat_block(section, book)

