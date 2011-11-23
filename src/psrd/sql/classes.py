def create_class_details_table(curs):
	sql = '\n'.join([
		"CREATE TABLE class_details (",
		"  class_details_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  alignment TEXT,"
		"  hit_die TEXT"
		")"])
	curs.execute(sql)

def create_class_details_index(curs):
	sql = '\n'.join([
		"CREATE INDEX class_details_section_id",
		" ON class_details (section_id)"])
	curs.execute(sql)

def insert_class_detail(curs, section_id, alignment, hit_die):
	values = [section_id, alignment, hit_die]
	sql = '\n'.join([
		"INSERT INTO class_details",
		" (section_id, alignment, hit_die)",
		" VALUES",
		" (?, ?, ?)"])
	curs.execute(sql, values)

def delete_class_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"DELETE FROM class_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_class_detail(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM class_details",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

