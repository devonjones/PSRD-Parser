def create_affliction_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE affliction_details (",
		"  affliction_details_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  contracted TEXT,",
		"  save TEXT,",
		"  onset TEXT,",
		"  frequency TEXT,",
		"  effect TEXT,",
		"  initial_effect TEXT,",
		"  secondary_effect TEXT,",
		"  cure TEXT",
		")"])
	curs.execute(sql)

def create_affliction_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX affliction_details_section_id",
		" ON affliction_details (section_id)"])
	curs.execute(sql)

def insert_affliction_detail(curs, section_id, contracted=None, save=None, onset=None, frequency=None, effect=None, initial_effect=None, secondary_effect=None, cure=None, **kwargs):
	values = [section_id, contracted, save, onset, frequency, effect, initial_effect, secondary_effect, cure]
	sql = '\n'.join([
		"INSERT INTO affliction_details",
		" (section_id, contracted, save, onset, frequency, effect, initial_effect, secondary_effect, cure)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_affliction_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM affliction_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_affliction_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM affliction_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

