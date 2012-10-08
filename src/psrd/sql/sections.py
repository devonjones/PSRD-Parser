from psrd.sql import append_child_section

def insert_section(curs, parent_id, section):
	sec_id = append_child_section(curs, parent_id, section['type'], section.get('name'), section.get('abbrev'), section.get('source'), section.get('description'), section.get('text'), section.get('image'), section.get('alt'), section.get('url'), section.get('create_index'))
	section['section_id'] = sec_id
	for s in section.get('sections', []):
		insert_section(curs, sec_id, s)
	return sec_id

def fetch_section_by_url(curs, url):
	values = [url]
	sql = '\n'.join([
		"SELECT *",
		" FROM sections",
		" WHERE url = ?"])
	curs.execute(sql, values)
