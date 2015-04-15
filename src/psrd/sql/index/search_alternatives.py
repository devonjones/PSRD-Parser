import re

def create_search_alternatives_table(curs):
	sql = '\n'.join([
		"CREATE TABLE search_alternatives (",
		"  search_alternative_id INTEGER PRIMARY KEY,",
		"  index_id INTEGER NOT NULL,",
		"  alternative TEXT NOT NULL",
		")"])
	curs.execute(sql)

def create_search_alternatives_index(curs):
	sql = '\n'.join([
		"CREATE INDEX search_alternatives_type",
		" ON search_alternatives (alternative)"])
	curs.execute(sql)

def fetch_alternative(curs, index_id=None):
	values = [type_name]
	sqla = [
		"SELECT *",
		" FROM search_alternatives",
		]
	if type_name:
		sqla.append(" WHERE index_id = ?")
		values.append(type_name)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def insert_alternative(curs, index_id, alternative):
	sql = '\n'.join([
		"INSERT INTO search_alternatives",
		" (index_id, alternative)",
		"VALUES",
		" (?, ?)"])
	curs.execute(sql, [index_id, alternative])
	return curs.lastrowid


def create_alternatives(curs, index_id, name):
	newname = name.lower()
	newname = re.sub('[^0-9a-z]+', '', newname)
	insert_alternative(curs, index_id, newname)
	if name.find(",") > -1:
		parts = name.split(", ")
		newname = "".join(reversed(parts))
		newname = newname.lower()
		newname = re.sub('[^0-9a-z]+', '', newname)
		insert_alternative(curs, index_id, newname)

