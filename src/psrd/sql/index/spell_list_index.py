def create_spell_list_index_table(curs):
	sql = '\n'.join([
		"CREATE TABLE spell_list_index (",
		"  spell_list_id INTEGER PRIMARY KEY,",
		"  index_id INTEGER,",
		"  level INTEGER NOT NULL,",
		"  type TEXT NOT NULL,",
		"  name TEXT,",
		"  notes TEXT,",
		"  magic_type TEXT",
		")"])
	curs.execute(sql)

def create_spell_list_index_indexes(curs):
	sql = '\n'.join([
		"CREATE INDEX spell_list_index_level",
		" ON spell_list_index (level)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX spell_list_index_type",
		" ON spell_list_index (type)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX spell_list_index_name",
		" ON spell_list_index (name)"])
	curs.execute(sql)

def insert_spell_list_index(curs, index_id, level, type, name, notes, magic_type):
	values = [index_id, level, type, name, notes, magic_type]
	sql = '\n'.join([
		"INSERT INTO spell_list_index",
		" (index_id, level, type, name, notes, magic_type)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)
	return curs.lastrowid

def delete_spell_list_index(curs, index_id, class_name=None):
	values = [section_id]
	sqla = [
		"DELETE FROM spell_list_index",
		" WHERE index_id = ?"]
	if class_name:
		sqla.append("  AND class = ?")
		values.append(class_name)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_spell_list_index(curs, index_id, type=None, name=None):
	values = [index_id]
	sqla = [
		"SELECT *",
		" FROM spell_list_index",
		" WHERE index_id = ?"]
	if type:
		sqla.append("  AND type = ?")
		values.append(type)
	if name:
		sqla.append("  AND name = ?")
		values.append(name)
	sqla.append(" ORDER BY type, name")
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

