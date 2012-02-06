from psrd.stat_block.utils import colon_filter, default_closure
from psrd.stat_block.section import parse_section
from psrd.universal import StatBlockSection, filter_name

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
