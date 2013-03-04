def create_item_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE item_details (",
		"  item_details_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  aura TEXT,",
		"  slot TEXT,",
		"  cl TEXT,",
		"  price TEXT,",
		"  weight TEXT,",
		"  requirements TEXT,",
		"  skill TEXT,",
		"  cr_increase TEXT,",
		"  cost TEXT",
		")"])
	curs.execute(sql)

def create_item_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX item_details_section_id",
		" ON item_details (section_id)"])
	curs.execute(sql)

def insert_item_detail(curs, section_id, aura=None, slot=None, cl=None, price=None, weight=None, requirements=None, skill=None, cr_increase=None, cost=None, **kwargs):
	values = [section_id, aura, slot, cl, price, weight, requirements, skill, cr_increase, cost]
	keys = kwargs.keys()
	sql = '\n'.join([
		"INSERT INTO item_details",
		" (section_id, aura, slot, cl, price, weight, requirements, skill, cr_increase, cost)",
		" VALUES",
		" (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"])
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

def create_item_misc_table(curs):
	sql = '\n'.join([
		"CREATE TABLE item_misc (",
		"  item_misc_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  field TEXT,",
		"  subsection TEXT,",
		"  value TEXT",
		")"])
	curs.execute(sql)

def create_item_misc_index(curs):
	sql = '\n'.join([
		"CREATE INDEX item_misc_section_id",
		" ON item_misc (section_id)"])
	curs.execute(sql)

def insert_item_misc(curs, section_id, field=None, subsection=None, value=None, **kwargs):
	values = [section_id, field, subsection, value]
	sql = '\n'.join([
		"INSERT INTO item_misc",
		" (section_id, field, subsection, value)",
		" VALUES",
		" (?, ?, ?, ?)"])
	curs.execute(sql, values)

def delete_item_misc(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM item_misc",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_item_misc(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM item_misc",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

