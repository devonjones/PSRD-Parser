def create_spell_descriptor_index_table(curs):
	sql = '\n'.join([
		"CREATE TABLE spell_descriptor_index (",
		"  spell_descriptor_id INTEGER PRIMARY KEY,",
		"  index_id INTEGER,",
		"  descriptor TEXT",
		")"])
	curs.execute(sql)

def create_spell_descriptor_index_indexes(curs):
	sql = '\n'.join([
		"CREATE INDEX spell_descriptor_index_descriptor",
		" ON spell_descriptor_index (descriptor)"])
	curs.execute(sql)

def insert_spell_descriptor_index(curs, index_id, descriptor):
	values = [index_id, descriptor]
	sql = '\n'.join([
		"INSERT INTO spell_descriptor_index",
		" (index_id, descriptor)",
		" VALUES",
		" (?, ?)"])
	curs.execute(sql, values)
	return curs.lastrowid

def delete_spell_descriptor_index(curs, index_id, descriptor=None):
	values = [section_id]
	sqla = [
		"DELETE FROM spell_descriptor_index",
		" WHERE index_id = ?"]
	if descriptor:
		sqla.append("  AND descriptor = ?")
		values.append(descriptor)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_spell_descriptor_index(curs, index_id, descriptor=None):
	values = [section_id]
	sqla = [
		"SELECT *",
		" FROM spell_descriptor_index",
		" WHERE index_id = ?"]
	if class_name:
		sqla.append("  AND descriptor = ?")
		values.append(descriptor)
	sqla.append(" ORDER BY descriptor")
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

