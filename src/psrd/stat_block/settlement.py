from psrd.stat_block.utils import colon_filter, default_closure, noop
from psrd.stat_block.section import parse_section
from psrd.universal import filter_name

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
			sec = parse_section(detail, book, keys=False)
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
