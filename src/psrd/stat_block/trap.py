from psrd.stat_block.utils import colon_filter, default_closure
from psrd.stat_block.section import parse_section
from psrd.universal import StatBlockHeading, StatBlockSection, filter_name

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
