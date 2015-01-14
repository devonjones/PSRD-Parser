import re
from BeautifulSoup import BeautifulSoup
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
	}
	return functions[field.lower()]

def parse_spell(sb, book):
	spell = parse_section(sb, book, keys=False)
	spell['type'] = 'spell'
	for key, value in sb.keys:
		spell_parse_function(key)(spell, value)
	if spell['source'] == 'Advanced Race Guide':
		text = ''.join(BeautifulSoup(spell['text']).findAll(text=True))
		spell['description'] = text.split(".")[0] + "."
	return spell

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
	spell['component_text'] = value
	value = colon_filter(value)
	m = re.search ('(\(.*?\))', value)
	content = []
	while m:
		value = re.sub('\(.*?\)', '{%s}' % len(content), value, count=1)
		content.append(m.groups()[0].replace(",", "|"))
		m = re.search('(\(.*?\))', value)
	comps = value.split(', ')
	finalcomps = []
	for comp in comps:
		if comp.find('{') > -1:
			m = re.search('(.*) {([0-9]*)}(.*)', comp)
			name = m.group(1)
			content_index = int(m.group(2))
			comments = content[content_index].replace('|', ',').replace('(', '').replace(')', '')
			finalcomps.extend(component_list(name, comments))
			if m.group(3) != '':
				finalcomps.append({'text': m.group(3)})
		else:
			finalcomps.extend(component_list(comp))
	spell['components'] = finalcomps

def component_list(component, text=None):
	components = []
	component = component.replace("/", ",")
	component = component.replace(" or ", ",")
	if component.find("; see text") > -1:
		if text:
			text = text + "; see text"
		else:
			text = "see text"
		component = component.replace("; see text", "")
	for c in component.split(","):
		comp = {'type': c.strip()}
		if text:
			comp['text'] = text
		components.append(comp)
	return components

def parse_school(spell, value):
	value = value.replace(';', '')
	value = colon_filter(value)
	m = re.search('\((.*)\)', value)
	if m:
		spell['subschool_text'] = m.group(1)
		spell['subschool'] = subschool_list(spell['subschool_text'])
		value= re.sub('\(.*\)', '', value)
	m = re.search('\[(.*)\]', value)
	if m:
		descriptor = m.group(1)
		spell['descriptor_text'] = descriptor
		descriptors = descriptor.split(', ')
		repaired_descriptors = []
		for d in descriptors:
			if d.startswith('or '):
				d = d[3:]
			if d.endswith(' see text'):
				d = d[:-9]
			repaired_descriptors.append(d)
		spell['descriptor'] = repaired_descriptors
		value = re.sub('\[.*\]', '', value)
	spell['school'] = value.strip()

def subschool_list(subschool):
	subschool = subschool.replace(', or ', ',')
	subschool = subschool.replace(' or ', ',')
	return [s.strip() for s in subschool.split(",")]

def parse_level(spell, value):
	value = colon_filter(value)
	if value.find(";"):
		value = value.replace(";", ",")
	levels = value.split(', ')
	finallevels = []
	hunterlevels = None
	for level in levels:
		m = re.search('(.*) (\d*)', level)
		c = m.group(1)
		l = int(m.group(2))
		if c.lower().strip() == 'sorcerer/wizard':
			finallevels.append({'class': 'sorcerer', 'level': l})
			finallevels.append({'class': 'wizard', 'level': l})
			finallevels.append({'class': 'arcanist', 'level': l})
		elif c.lower().strip() == 'bard':
			finallevels.append({'class': 'bard', 'level': l})
			finallevels.append({'class': 'skald', 'level': l})
		elif c.lower().strip() == 'alchemist':
			finallevels.append({'class': 'alchemist', 'level': l})
			finallevels.append({'class': 'investigator', 'level': l})
		elif c.lower().strip() == 'cleric':
			finallevels.append({'class': 'cleric', 'level': l})
			finallevels.append({'class': 'oracle', 'level': l})
			finallevels.append({'class': 'warpriest', 'level': l})
		elif c.lower().strip() in ['druid', 'ranger']:
			finallevels.append({'class': c, 'level': l})
			if l <= 6:
				if not hunterlevels:
					hunterlevels = {'class': 'hunter', 'level': l}
				elif hunterlevels['level'] > l:
					hunterlevels['level'] = l
		else:
			finallevels.append({'class': c, 'level': l})
		if hunterlevels:
			finallevels.append(hunterlevels)
	spell['level'] = finallevels
