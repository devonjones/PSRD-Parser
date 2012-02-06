from psrd.stat_block.utils import colon_filter, default_closure
from psrd.universal import filter_name

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
