from psrd.sql.utils import test_args

def create_animal_companion_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE animal_companion_details (",
		"  animal_companion_details_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  ac TEXT,",
		"  attack TEXT,",
		"  cmd TEXT,",
		"  ability_scores TEXT,",
		"  special_qualities TEXT,",
		"  special_attacks TEXT,",
		"  size TEXT,",
		"  speed TEXT,",
		"  level TEXT",
		")"])
	curs.execute(sql)

def create_animal_companion_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX animal_companion_details_section_id",
		" ON animal_companion_details (section_id)"])
	curs.execute(sql)

def insert_animal_companion_detail(curs, section_id, ac=None, attack=None,
		cmd=None, ability_scores=None, special_qualities=None,
		special_attacks=None, size=None, speed=None, level=None, **kwargs):
	values = [section_id, ac, attack, cmd, ability_scores, special_qualities,
		special_attacks, size, speed, level]
	test_args(kwargs)
	sql = '\n'.join([
		"INSERT INTO animal_companion_details",
		" (section_id, ac, attack, cmd, ability_scores, special_qualities, special_attacks, size, speed, level)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_animal_companion_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM animal_companion_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_animal_companion_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM animal_companion_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

