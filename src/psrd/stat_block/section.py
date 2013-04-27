from psrd.stat_block.utils import colon_filter, default_closure, parse_stat_block, collapse_text
from psrd.universal import StatBlockHeading, StatBlockSection, Heading, filter_name

def is_section(sb, book):
	if len(sb.keys) == 0:
		return True
	return False

def parse_section(sb, book, no_sb=False, keys=True):
	section = {'type': 'section', 'source': book, 'name': filter_name(sb.name.strip())}
	text = []
	sections = []
	sectiontext = []
	ns = None
	if keys:
		for key in sb.keys:
			text.append("<p class='stat-block-1'><b>%s </b>%s</p>" % key)
	for detail in sb.details:
		if detail.__class__ == StatBlockSection:
			sections.append(parse_stat_block(detail, book, no_sb=no_sb))
		elif detail.__class__ == StatBlockHeading:
			sections.append(parse_stat_block(sb, book, no_sb=no_sb))
		elif isinstance(detail, dict):
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
				if isinstance(detail, dict):
					text.append(detail)
				else:
					text.append(unicode(detail))
			else:
				if not ns:
					ns = {'type': 'section', 'source': book}
					sections.append(ns)
				if isinstance(detail, dict):
					sectiontext.append(detail)
				else:
					sectiontext.append(unicode(detail))
	if len(text) > 0:
		collapse_text(section, text)
	if len(sectiontext) > 0:
		collapse_text(ns, sectiontext)
	if len(sections) > 0:
		section['sections'] = sections
	return section
