def create_trap_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE trap_details (",
		"  trap_details_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  trap_type TEXT,",
		"  perception TEXT,",
		"  disable_device TEXT,",
		"  duration TEXT,",
		"  effect TEXT,",
		"  trigger TEXT,",
		"  reset TEXT",
		")"])
	curs.execute(sql)

def create_trap_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX trap_details_section_id",
		" ON trap_details (section_id)"])
	curs.execute(sql)

def insert_trap_detail(curs, section_id, trap_type=None, perception=None, disable_device=None, duration=None, effect=None, trigger=None, reset=None, **kwargs):
	values = [section_id, trap_type, perception, disable_device, duration, effect, trigger, reset]
	sql = '\n'.join([
		"INSERT INTO trap_details",
		" (section_id, trap_type, perception, disable_device, duration, effect, trigger, reset)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_trap_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM trap_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_trap_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM trap_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

