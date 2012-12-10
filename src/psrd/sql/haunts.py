def create_haunt_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE haunt_details (",
		"  haunt_details_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  cr TEXT,",
		"  xp TEXT,",
		"  haunt_type TEXT,",
		"  notice TEXT,",
		"  area TEXT,",
		"  hp TEXT,",
		"  destruction TEXT,",
		"  alignment TEXT,",
		"  caster_level TEXT,",
		"  effect TEXT,",
		"  trigger TEXT,",
		"  reset TEXT",
		")"])
	curs.execute(sql)

def create_haunt_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX haunt_details_section_id",
		" ON haunt_details (section_id)"])
	curs.execute(sql)

def insert_haunt_detail(curs, section_id, cr=None, xp=None, haunt_type=None, notice=None, area=None, hp=None, destruction=None, alignment=None, caster_level=None, effect=None, trigger=None, reset=None, **kwargs):
	values = [section_id, cr, xp, haunt_type, notice, area, hp, destruction, alignment, caster_level, effect, trigger, reset]
	sql = '\n'.join([
		"INSERT INTO haunt_details",
		" (section_id, cr, xp, haunt_type, notice, area, hp, destruction, alignment, caster_level, effect, trigger, reset)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_haunt_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM haunt_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_haunt_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM haunt_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

