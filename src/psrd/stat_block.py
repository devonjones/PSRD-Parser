import re
from psrd.universal import StatBlockHeading, StatBlockSection, Heading, filter_name

def colon_filter(value):
	if value.startswith(":"):
		value = value[1:]
	return value.strip()

def default_closure(field):
	def fxn(sb, value):
		value = colon_filter(value)
		sb[field] = value
	return fxn

def is_animal_companion(sb):
	fields = dict(sb.keys)
	if fields.has_key('AC'):
		for detail in sb.details:
			if detail.__class__ == StatBlockSection and detail.name.endswith('th-Level Advancement'):
				return True
	return False

def animal_companion_parse_function(field):
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
	if fields.has_key('Aura'):
		if fields.has_key('Slot') or fields.has_key('CL'):
			return True
	return False

def parse_item_slot(item, value):
	item['subtype'] = value
	item['slot'] = value

def item_parse_function(field):
	functions = {
		'aura': default_closure('aura'),
		'cl': default_closure('cl'),
		'slot': parse_item_slot,
		'price': default_closure('price'),
		'weight': default_closure('weight'),
		'requirements': default_closure('requirements'),
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
			text.append(detail)
	if len(text) > 0:
		item['text'] = ''.join(text)
	return item 

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

def parse_stat_block(sb, book):
	if is_animal_companion(sb):
		return parse_animal_companion(sb, book)
	elif is_spell(sb):
		return parse_spell(sb, book)
	elif is_trap(sb, book):
		return parse_trap(sb, book)
	elif is_affliction(sb):
		return parse_affliction(sb, book)
	elif is_item(sb, book):
		return parse_item(sb, book)
	elif is_section(sb, book):
		return parse_section(sb, book)
	else:
		print sb
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

