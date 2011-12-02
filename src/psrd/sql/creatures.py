def create_creature_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE creature_details (",
		"  creature_details_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  ac TEXT,",
		"  attack TEXT,",
		"  ability_scores TEXT,",
		"  special_qualities TEXT,",
		"  special_attacks TEXT,",
		"  size TEXT,",
		"  speed TEXT,",
		"  level TEXT",
		")"])
	curs.execute(sql)

def create_creature_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX creature_details_section_id",
		" ON creature_details (section_id)"])
	curs.execute(sql)

def insert_creature_detail(curs, section_id, ac=None, attack=None, ability_scores=None, special_qualities=None, special_attacks=None, size=None, speed=None, level=None, **kwargs):
	values = [section_id, ac, attack, ability_scores, special_qualities, special_attacks, size, speed, level]
	sql = '\n'.join([
		"INSERT INTO creature_details",
		" (section_id, ac, attack, ability_scores, special_qualities, special_attacks, size, speed, level)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_creature_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM creature_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_creature_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM creature_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

