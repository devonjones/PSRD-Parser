from psrd.sql.utils import test_args

def create_resource_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE resource_details (",
		"  resource_detail_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  benefit TEXT,",
		"  resource_create TEXT,",
		"  earnings TEXT,",
		"  rooms TEXT,",
		"  size TEXT,",
		"  skills TEXT,",
		"  teams TEXT,",
		"  time TEXT,",
		"  upgrade_from TEXT,",
		"  upgrade_to TEXT,",
		"  wage TEXT",
		")"])
	curs.execute(sql)

def create_resource_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX resource_details_section_id",
		" ON resource_details (section_id)"])
	curs.execute(sql)

def insert_resource_detail(curs, section_id, benefit=None, create=None,
		earnings=None, rooms=None, size=None, skills=None, teams=None,
		time=None, upgrade_from=None, upgrade_to=None, wage=None, **kwargs):
	values = [section_id, benefit, create, earnings, rooms, size, skills,
		teams, time, upgrade_from, upgrade_to, wage]
	test_args(kwargs)
	sql = '\n'.join([
		"INSERT INTO resource_details",
		" (section_id, benefit, resource_create, earnings, rooms, size, skills,"
		" teams, time, upgrade_from, upgrade_to, wage)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_resource_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM resource_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_resource_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM resource_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

