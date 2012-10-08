def create_url_references_table(curs):
	sql = '\n'.join([
		"CREATE TABLE url_references (",
		"  url_reference_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  url TEXT"
		")"])
	curs.execute(sql)

def create_url_references_index(curs):
	sql = '\n'.join([
		"CREATE INDEX url_references_section_id",
		" ON url_references (section_id)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX url_references_url",
		" ON url_references (url)"])
	curs.execute(sql)

def insert_url_reference(curs, section_id, url):
	values = [section_id, url]
	sql = '\n'.join([
		"INSERT INTO url_references",
		" (section_id, url)",
		" VALUES",
		" (?, ?)"])
	curs.execute(sql, values)

def delete_url_reference(curs, url):
	values = [urk]
	sql = '\n'.join([
		"DELETE FROM url_references",
		" WHERE url = ?"])
	curs.execute(sql, values)

def fetch_url_references(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM url_references",
		" WHERE section_id = ?"])
	curs.execute(sql, values)
