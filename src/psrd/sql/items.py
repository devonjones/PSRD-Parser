def create_item_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE item_details (",
		"  item_details_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  slot TEXT,",
		"  cl TEXT,",
		"  price TEXT,",
		"  weight TEXT,",
		"  requirements TEXT,",
		"  cost TEXT",
		")"])
	curs.execute(sql)

def create_item_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX item_details_section_id",
		" ON item_details (section_id)"])
	curs.execute(sql)

def insert_item_detail(curs, section_id, slot=None, cl=None, price=None, weight=None, requirements=None, cost=None, **kwargs):
	values = [section_id, slot, cl, price, weight, requirements, cost]
	sql = '\n'.join([
		"INSERT INTO item_details",
		" (section_id, slot, cl, price, weight, requirements, cost)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_item_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM item_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_item_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM item_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

