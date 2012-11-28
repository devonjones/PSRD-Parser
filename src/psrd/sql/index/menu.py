def create_menu_table(curs):
	sql = '\n'.join([
		"CREATE TABLE menu (",
		"  menu_id INTEGER PRIMARY KEY,",
		"  parent_menu_id INTEGER,",
		"  name TEXT,"
		"  type TEXT,"
		"  subtype TEXT,"
		"  url TEXT,"
		"  db TEXT,"
		"  grouping TEXT,"
		"  priority INTEGER"
		")"])
	curs.execute(sql)

def create_menu_index(curs):
	sql = '\n'.join([
		"CREATE INDEX parent_menu_id",
		" ON menu (parent_menu_id)"])
	curs.execute(sql)

def insert_menu(curs, parent_menu_id=None, name=None, type=None, subtype=None,
		url=None, db=None, group=None, priority=None):
	values = [parent_menu_id, name, type, subtype, url, db, group, priority]
	sql = '\n'.join([
		"INSERT INTO menu",
		" (parent_menu_id, name, type, subtype, url, db, grouping, priority)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)
	return curs.lastrowid

def delete_menu(curs, menu_id):
	values = [menu_id]
	sql = '\n'.join([
		"DELETE FROM menu",
		" WHERE menu_id = ?"])
	curs.execute(sql, values)

def fetch_menu(curs, menu_id):
	values = [menu_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM menu",
		" WHERE menu_id = ?"])
	curs.execute(sql, values)
