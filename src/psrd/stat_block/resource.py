import re
from psrd.stat_block.utils import colon_filter, default_closure
from psrd.stat_block.section import parse_section
from psrd.universal import StatBlockHeading, StatBlockSection, filter_name

def is_resource(sb, book):
	fields = dict(sb.keys)
	if is_manager(sb):
		return True
	if is_room(sb):
		return True
	if is_building(sb):
		return True
	if is_organization(sb):
		return True
	return False

def is_manager(sb):
	fields = dict(sb.keys)
	if fields.has_key('Wage'):
		if fields.has_key('Skills'):
			return True
	return False

def is_room(sb):
	fields = dict(sb.keys)
	if fields.has_key('Create'):
		if fields.has_key('Time'):
			if fields.has_key('Size'):
				return True

def is_building(sb):
	fields = dict(sb.keys)
	if fields.has_key('Create'):
		if fields.has_key('Rooms'):
			return True

def is_organization(sb):
	fields = dict(sb.keys)
	if fields.has_key('Create'):
		if fields.has_key('Teams'):
			return True

def resource_parse_function(field):
	functions = {
		'benefit': default_closure('benefit'),
		'create': default_closure('create'),
		'earnings': default_closure('earnings'),
		'rooms': default_closure('rooms'),
		'size': default_closure('size'),
		'skills': default_closure('skills'),
		'teams': default_closure('teams'),
		'time': default_closure('time'),
		'upgrades from': default_closure('upgrade_from'),
		'upgrade from': default_closure('upgrade_from'),
		'upgrades to': default_closure('upgrade_to'),
		'upgrade to': default_closure('upgrade_to'),
		'wage': default_closure('wage'),
	}
	return functions[field.lower()]

def parse_resource(sb, book):
	details = []
	for detail in sb.details:
		details.append(detail)
	sb.details = details
	resource = parse_section(sb, book, keys=False)
	for key, value in sb.keys:
		resource_parse_function(key)(resource, value)
	resource['type'] = 'resource'
	if is_manager(sb):
		resource['subtype'] = 'manager'
	if is_room(sb):
		resource['subtype'] = 'room'
	if is_building(sb):
		resource['subtype'] = 'building'
	if is_organization(sb):
		resource['subtype'] = 'organization'
	return resource

