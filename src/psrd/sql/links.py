def create_link_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE link_details (",
		"  link_detail_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  url TEXT,"
		"  display BOOLEAN"
		")"])
	curs.execute(sql)

def create_link_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX link_details_section_id",
		" ON link_details (section_id)"])
	curs.execute(sql)

def insert_link_detail(curs, section_id, url, display):
	if display == None:
		display = False
	values = [section_id, url, display]
	sql = '\n'.join([
		"INSERT INTO link_details",
		" (section_id, url, display)",
		" VALUES",
		" (?, ?, ?)"])
	curs.execute(sql, values)

def delete_link_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM link_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_link_details(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM link_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

