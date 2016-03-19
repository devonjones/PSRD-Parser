def create_talent_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE talent_details (",
		"  talent_details_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  element TEXT,",
		"  talent_type TEXT,",
		"  level INT,",
		"  burn TEXT,",
		"  damage TEXT,",
		"  prerequisite TEXT,",
		"  associated_blasts TEXT,",
		"  saving_throw TEXT",
		"  spell_resistance TEXT",
		")"])
	curs.execute(sql)

def create_talent_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX talent_details_section_id",
		" ON talent_details (section_id)"])
	curs.execute(sql)

def insert_talent_detail(curs, section_id, element=None, talent_type=None, level=None, burn=None, damage=None, prerequisite=None, associated_blasts=None, saving_throw=None, spell_resistance=None, **kwargs):
	values = [section_id, element, talent_type, level, burn, damage, prerequisite, associated_blasts, saving_throw, spell_resistance]
	sql = '\n'.join([
		"INSERT INTO talent_details",
		" (section_id, element, talent_type, level, burn, damage, prerequisite, associated_blasts, saving_throw, spell_resistance)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_talent_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM talent_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_talent_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM talent_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

