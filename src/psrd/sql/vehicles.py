from psrd.sql.utils import test_args

def create_vehicle_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE vehicle_details (",
		"  vehicle_details_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  size TEXT,",
		"  vehicle_type TEXT,",
		"  squares TEXT,",
		"  cost TEXT,",
		"  ac TEXT,",
		"  hardness TEXT,",
		"  hp TEXT,",
		"  base_save TEXT,",
		"  maximum_speed TEXT,",
		"  acceleration TEXT,",
		"  cmb TEXT,",
		"  cmd TEXT,",
		"  ramming_damage TEXT,",
		"  propulsion TEXT,",
		"  driving_check TEXT,",
		"  forward_facing TEXT,",
		"  driving_device TEXT,",
		"  driving_space TEXT,",
		"  decks TEXT,",
		"  deck TEXT,",
		"  weapons TEXT,",
		"  crew TEXT,",
		"  passengers TEXT",
		")"])
	curs.execute(sql)

def create_vehicle_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX vehicle_details_section_id",
		" ON vehicle_details (section_id)"])
	curs.execute(sql)

def insert_vehicle_detail(curs, section_id, size=None, vehicle_type=None, squares=None, cost=None, ac=None,
		hardness=None, hp=None, base_save=None, maximum_speed=None, acceleration=None, cmb=None, cmd=None,
		ramming_damage=None, propulsion=None, driving_check=None, forward_facing=None, driving_device=None,
		driving_space=None, decks=None, weapons=None, crew=None, passengers=None, **kwargs):
	values = [section_id, size, vehicle_type, squares, cost, ac, hardness, hp, base_save, maximum_speed, acceleration, cmb, cmd, ramming_damage, propulsion, driving_check, forward_facing, driving_device, driving_space, decks, weapons, crew, passengers]
	test_args(kwargs)
	sql = '\n'.join([
		"INSERT INTO vehicle_details",
		" (section_id, size, vehicle_type, squares, cost, ac, hardness, hp, base_save, maximum_speed,",
		"  acceleration, cmb, cmd, ramming_damage, propulsion, driving_check, forward_facing,",
		"  driving_device, driving_space, decks, weapons, crew, passengers)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,",
		"  ?, ?, ?, ?, ?, ?, ?,",
		"  ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_vehicle_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM vehicle_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_vehicle_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM vehicle_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

