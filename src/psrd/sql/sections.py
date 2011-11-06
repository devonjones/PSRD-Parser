from psrd.sql import append_child_section

def insert_section(curs, parent_id, section):
	sec_id = append_child_section(curs, parent_id, section['type'], section.get('name'), section.get('abbrev'), section.get('source'), section.get('description'), section.get('text'))
	section['section_id'] = sec_id
	for s in section.get('sections', []):
		insert_section(curs, sec_id, s)
	return sec_id
