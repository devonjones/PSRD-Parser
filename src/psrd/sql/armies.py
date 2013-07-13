from psrd.sql.utils import test_args

def create_army_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE army_details (",
		"  army_detail_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  cr TEXT,",
		"  xp TEXT,",
		"  creature_type TEXT,",
		"  alignment TEXT,",
		"  size TEXT,",
		"  descriptor TEXT,",
		"  hp TEXT,",
		"  acr TEXT,",
		"  dv TEXT,",
		"  om TEXT,",
		"  special TEXT,",
		"  speed TEXT,",
		"  consumption TEXT,",
		"  tactics TEXT,",
		"  resources TEXT,",
		"  note TEXT",
		")"])
	curs.execute(sql)

def create_army_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX army_details_section_id",
		" ON army_details (section_id)"])
	curs.execute(sql)

def insert_army_detail(curs, section_id, cr=None, xp=None, creature_type=None,
		alignment=None, size=None, descriptor=None, hp=None, acr=None, dv=None,
		om=None, special=None, speed=None, consumption=None, tactics=None,
		resources=None, note=None, **kwargs):
	values = [section_id, cr, xp, creature_type, alignment, size, descriptor,
		hp, acr, dv, om, special, speed, consumption, tactics, resources, note]
	test_args(kwargs)
	sql = '\n'.join([
		"INSERT INTO army_details",
		" (section_id, cr, xp, creature_type, alignment, size, descriptor, hp,"
		" acr, dv, om, special, speed, consumption, tactics, resources, note)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_army_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM army_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_army_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM army_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

