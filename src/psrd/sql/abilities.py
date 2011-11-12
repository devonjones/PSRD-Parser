def create_ability_types_table(curs):
	sql = '\n'.join([
		"CREATE TABLE ability_types (",
		"  ability_type_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  ability_type TEXT"
		")"])
	curs.execute(sql)

def create_ability_types_index(curs):
	sql = '\n'.join([
		"CREATE INDEX ability_types_section_id",
		" ON ability_types (section_id)"])
	curs.execute(sql)

def insert_ability_type(curs, section_id, ability_type):
	values = [section_id, ability_type]
	sql = '\n'.join([
		"INSERT INTO ability_types",
		" (section_id, ability_type)",
		" VALUES",
		" (?, ?)"])
	curs.execute(sql, values)

def delete_ability_type(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM ability_types",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_ability_type(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM ability_types",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_abilities_by_type(curs, ability_type):
	values = [ability_type]
	sql = '\n'.join([
		"SELECT s.*",
		" FROM sections s, ability_types at",
		" WHERE s.section_id = at.section_id",
		"  AND at.ability_type = ?"])
	curs.execute(sql, values)
