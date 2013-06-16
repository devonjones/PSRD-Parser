def create_spell_component_index_table(curs):
	sql = '\n'.join([
		"CREATE TABLE spell_component_index (",
		"  spell_component_id INTEGER PRIMARY KEY,",
		"  index_id INTEGER,",
		"  component TEXT",
		")"])
	curs.execute(sql)

def create_spell_component_index_indexes(curs):
	sql = '\n'.join([
		"CREATE INDEX spell_component_index_component",
		" ON spell_component_index (component)"])
	curs.execute(sql)

def insert_spell_component_index(curs, index_id, component):
	values = [index_id, component]
	sql = '\n'.join([
		"INSERT INTO spell_component_index",
		" (index_id, component)",
		" VALUES",
		" (?, ?)"])
	curs.execute(sql, values)
	return curs.lastrowid

def delete_spell_component_index(curs, index_id, component=None):
	values = [section_id]
	sqla = [
		"DELETE FROM spell_component_index",
		" WHERE index_id = ?"]
	if component:
		sqla.append("  AND component = ?")
		values.append(component)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_spell_component_index(curs, index_id, component=None):
	values = [section_id]
	sqla = [
		"SELECT *",
		" FROM spell_component_index",
		" WHERE index_id = ?"]
	if class_name:
		sqla.append("  AND component = ?")
		values.append(component)
	sqla.append(" ORDER BY component")
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

