from psrd.sql.utils import test_args

def create_settlement_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE settlement_details (",
		"  settlement_details_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  alignment TEXT,",
		"  settlement_type TEXT,",
		"  size TEXT,",
		"  corruption TEXT,",
		"  crime TEXT,",
		"  economy TEXT,",
		"  law TEXT,",
		"  lore TEXT,",
		"  society TEXT,",
		"  qualities TEXT,",
		"  danger TEXT,",
		"  disadvantages TEXT,",
		"  government TEXT,",
		"  population TEXT,",
		"  base_value TEXT,",
		"  purchase_limit TEXT,",
		"  spellcasting TEXT,",
		"  minor_items TEXT,",
		"  medium_items TEXT,",
		"  major_items TEXT",
		")"])
	curs.execute(sql)

def create_settlement_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX settlement_details_section_id",
		" ON settlement_details (section_id)"])
	curs.execute(sql)

def insert_settlement_detail(curs, section_id, alignment=None, settlement_type=None, size=None,
		corruption=None, crime=None, economy=None, law=None, lore=None, society=None, qualities=None,
		danger=None, disadvantages=None, government=None, population=None, base_value=None,
		purchase_limit=None, spellcasting=None, minor_items=None, medium_items=None,
		major_items=None, **kwargs):
	values = [section_id, alignment, settlement_type, size, corruption, crime, economy, law, lore,
		society, qualities, danger, disadvantages, government, population, base_value, purchase_limit,
		spellcasting, minor_items, medium_items, major_items]
	test_args(kwargs)
	sql = '\n'.join([
		"INSERT INTO settlement_details",
		" (section_id, alignment, settlement_type, size, corruption, crime, economy, law, lore, society,",
		"  qualities, danger, disadvantages, government, population, base_value, purchase_limit,",
		"  spellcasting, minor_items, medium_items, major_items)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_settlement_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM settlement_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_settlement_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM settlement_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

