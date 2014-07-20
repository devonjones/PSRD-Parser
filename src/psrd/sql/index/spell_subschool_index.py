def create_spell_subschool_index_table(curs):
	sql = '\n'.join([
		"CREATE TABLE spell_subschool_index (",
		"  spell_subschool_id INTEGER PRIMARY KEY,",
		"  index_id INTEGER,",
		"  subschool TEXT",
		")"])
	curs.execute(sql)

def create_spell_subschool_index_indexes(curs):
	sql = '\n'.join([
		"CREATE INDEX spell_subschool_index_subschool",
		" ON spell_subschool_index (subschool)"])
	curs.execute(sql)

def insert_spell_subschool_index(curs, index_id, subschool):
	values = [index_id, subschool]
	sql = '\n'.join([
		"INSERT INTO spell_subschool_index",
		" (index_id, subschool)",
		" VALUES",
		" (?, ?)"])
	curs.execute(sql, values)
	return curs.lastrowid

def delete_spell_subschool_index(curs, index_id, subschool=None):
	values = [section_id]
	sqla = [
		"DELETE FROM spell_subschool_index",
		" WHERE index_id = ?"]
	if subschool:
		sqla.append("  AND subschool = ?")
		values.append(subschool)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_spell_subschool_index(curs, index_id, subschool=None):
	values = [index_id]
	sqla = [
		"SELECT *",
		" FROM spell_subschool_index",
		" WHERE index_id = ?"]
	if subschool:
		sqla.append("  AND subschool = ?")
		values.append(subschool)
	sqla.append(" ORDER BY subschool")
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

