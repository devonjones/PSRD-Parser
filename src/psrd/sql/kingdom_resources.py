from psrd.sql.utils import test_args

def create_kingdom_resource_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE kingdom_resource_details (",
		"  kingdom_resource_detail_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  cr TEXT,",
		"  bp TEXT,",
		"  lot TEXT,",
		"  kingdom TEXT,",
		"  discount TEXT,",
		"  magic_items TEXT,",
		"  settlement TEXT,",
		"  special TEXT,",
		"  resource_limit TEXT,",
		"  upgrade_from TEXT,",
		"  upgrade_to TEXT",
		")"])
	curs.execute(sql)

def create_kingdom_resource_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX kingdom_resource_details_section_id",
		" ON kingdom_resource_details (section_id)"])
	curs.execute(sql)

def insert_kingdom_resource_detail(curs, section_id, cr=None, bp=None, lot=None,
		kingdom=None, discount=None, magic_items=None, settlement=None,
		special=None, limit=None, upgrade_from=None, upgrade_to=None, **kwargs):
	values = [section_id, cr, bp, lot, kingdom, discount, magic_items,
		settlement, special, limit, upgrade_from, upgrade_to]
	test_args(kwargs)
	sql = '\n'.join([
		"INSERT INTO kingdom_resource_details",
		" (section_id, cr, bp, lot, kingdom, discount, magic_items, settlement,"
		" special, resource_limit, upgrade_from, upgrade_to)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_kingdom_resource_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM kingdom_resource_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_kingdom_resource_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM kingdom_resource_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

