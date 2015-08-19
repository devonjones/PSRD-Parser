from psrd.sql.utils import test_args

def create_mythic_spell_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE mythic_spell_details (",
		"  spell_detail_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NO NULL,",
		"  spell_source TEXT NOT NULL",
		")"])
	curs.execute(sql)

def create_mythic_spell_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX mythic_spell_details_section_id",
		" ON mythic_spell_details (section_id)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX mythic_spell_details_source",
		" ON mythic_spell_details (spell_source)"])
	curs.execute(sql)

def insert_mythic_spell_detail(curs, section_id, spell_source=None, **kwargs):
	values = [section_id, spell_source]
	test_args(kwargs)
	sql = '\n'.join([
		"INSERT INTO mythic_spell_details",
		" (section_id, spell_source)",
		" VALUES",
		" (?, ?)"])
	curs.execute(sql, values)

def update_mythic_spell_detail(curs, section_id, **kwargs):
	values = []
	sqla = [
		"UPDATE mythic_spell_details",
		" SET"]
	comma = " "
	for key in kwargs.keys():
		sqla.append(comma + key + " = ?")
		values.append(kwargs[key])
		comma = ", "
	sqla.append(" WHERE section_id = ?")
	values.append(section_id)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def delete_mythic_spell_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM mythic_spell_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_mythic_spell_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM mythic_spell_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

