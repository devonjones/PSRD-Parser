def create_url_references_table(curs):
	sql = '\n'.join([
		"CREATE TABLE url_references (",
		"  url_reference_id INTEGER PRIMARY KEY,",
		"  index_id INTEGER NOT NULL,",
		"  url TEXT"
		")"])
	curs.execute(sql)

def create_url_references_index(curs):
	sql = '\n'.join([
		"CREATE INDEX url_references_index_id",
		" ON url_references (index_id)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX url_references_url",
		" ON url_references (url)"])
	curs.execute(sql)

def insert_url_reference(curs, index_id, url):
	values = [index_id, url]
	sql = '\n'.join([
		"INSERT INTO url_references",
		" (index_id, url)",
		" VALUES",
		" (?, ?)"])
	curs.execute(sql, values)

def delete_url_reference(curs, url):
	values = [url]
	sql = '\n'.join([
		"DELETE FROM url_references",
		" WHERE url = ?"])
	curs.execute(sql, values)

def fetch_url_references(curs, index_id):
	values = [index_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM url_references",
		" WHERE index_id = ?"])
	curs.execute(sql, values)
