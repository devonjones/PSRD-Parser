from psrd.tables import has_table, is_table, parse_table
from psrd.parse import construct_stripped_line, construct_line

def store_section(parent, context, details, name=None):
	if name == 'description':
		parent[name] = construct_stripped_line(details)
	else:
		section = {'source': parent['source'], 'type': 'section'}
		if name:
			section['name'] = construct_stripped_line(name)
		set_section_text(section, context, details)
		if section.has_key('text') or section.has_key('sections'):
			sections = parent.setdefault('sections', [])
			sections.append(section)

def set_section_text(section, context, details):
	if has_table(details):
		section['sections'] = []
		for detail in details:
			if is_table(detail):
				if detail.name == 'div':
					detail = detail.findAll(text=False)[0]
				section['sections'].append(parse_table(detail, context))
			else:
				store_section(section, context, detail)
	else:
		text = construct_line(details)
		if text:
			section['text'] =  text

