def create_central_index_table(curs):
	sql = '\n'.join([
		"CREATE TABLE central_index (",
		"  index_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  parent_id INTEGER NOT NULL,",
		"  parent_name TEXT,",
		"  database TEXT NOT NULL,",
		"  source TEXT NOT NULL,",
		"  type TEXT NOT NULL,",
		"  subtype TEXT,",
		"  name TEXT NOT NULL,",
		"  search_name TEXT NOT NULL,",
		"  description TEXT,",
		"  url TEXT NOT NULL,",
		"  feat_type_description TEXT,",
		"  feat_prerequisites TEXT,",
		"  skill_attribute TEXT,",
		"  skill_armor_check_penalty INTEGER,",
		"  skill_trained_only INTEGER,",
		"  spell_school TEXT,",
		"  spell_subschool_text TEXT,",
		"  spell_descriptor_text TEXT,",
		"  spell_list_text TEXT,",
		"  spell_component_text TEXT,",
		"  spell_source TEXT,",
		"  creature_type TEXT,",
		"  creature_subtype TEXT,",
		"  creature_super_race TEXT,",
		"  creature_cr TEXT,",
		"  creature_xp TEXT,",
		"  creature_size TEXT,",
		"  creature_alignment TEXT"
		")"])
	curs.execute(sql)

def create_central_index_indexes(curs):
	sql = '\n'.join([
		"CREATE INDEX central_index_type",
		" ON central_index (type)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX central_index_subtype",
		" ON central_index (subtype)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX central_index_parents",
		" ON central_index (parent_id)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX central_index_name",
		" ON central_index (name)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX central_index_source",
		" ON central_index (source)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX central_index_url",
		" ON central_index (url)"])
	curs.execute(sql)

def insert_central_index(curs, section_id=None, parent_id=None,
		parent_name=None, database=None, source=None, type=None,
		subtype=None, name=None, search_name=None, description=None, url=None,
		feat_type_description=None, feat_prerequisites=None,
		skill_attribute=None, skill_armor_check_penalty=None,
		skill_trained_only=None, 
		spell_school=None, spell_subschool_text=None,
		spell_descriptor_text=None, spell_list_text=None,
		spell_component_text=None, spell_source=None,
		creature_type=None, creature_subtype=None, creature_super_race=None,
		creature_cr=None, creature_xp=None, creature_size=None,
		creature_alignment=None):

	values = [section_id, parent_id, parent_name, database,
		source, type, subtype, name, search_name, description, url,
		feat_type_description, feat_prerequisites,
		skill_attribute, skill_armor_check_penalty, skill_trained_only,
		spell_school, spell_subschool_text, spell_descriptor_text,
		spell_list_text, spell_component_text, spell_source, 
		creature_type, creature_subtype, creature_super_race, creature_cr,
		creature_xp, creature_size, creature_alignment]
	sql = '\n'.join([
		"INSERT INTO central_index",
		" (section_id, parent_id, parent_name, database,",
		"  source, type, subtype, name, search_name, description, url,",
		"  feat_type_description, feat_prerequisites,",
		"  skill_attribute, skill_armor_check_penalty, skill_trained_only,",
		"  spell_school, spell_subschool_text, spell_descriptor_text,",
		"  spell_list_text, spell_component_text, spell_source,"
		"  creature_type, creature_subtype, creature_super_race, creature_cr,",
		"  creature_xp, creature_size, creature_alignment)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)
	return curs.lastrowid

def delete_central_index(curs, index_id):
	values = [section_id]
	sqla = [
		"DELETE FROM central_index",
		" WHERE index_id = ?"]
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_central_index(curs, index_id):
	values = [section_id]
	sqla = [
		"SELECT *",
		" FROM central_index",
		" WHERE index_id = ?"]
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_index_by_url(curs, url):
	values = [url]
	sql = '\n'.join([
		"SELECT *",
		" FROM central_index",
		" WHERE url = ?"])
	curs.execute(sql, values)

def select_section_types(curs):
	sql = '\n'.join([
		"SELECT DISTINCT type",
		" FROM central_index"])
	curs.execute(sql)

