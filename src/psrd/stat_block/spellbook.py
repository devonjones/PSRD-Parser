from psrd.stat_block.utils import colon_filter, default_closure
from psrd.stat_block.section import parse_section
from psrd.universal import filter_name

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
	section = parse_section(sb, book, keys=False)
	for key in sb.keys:
		newsec = {'type': 'section', 'source': book, 'name': key[0], 'text': key[1]}
		sections = section.setdefault('sections', [])
		sections.insert(1, newsec)
	section['subtype'] = 'spellbook'
	return section
