import re
from psrd.stat_block.utils import colon_filter, default_closure
from psrd.stat_block.section import parse_section
from psrd.universal import filter_name

def is_spell(sb, book):
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
