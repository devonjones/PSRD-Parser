def create_feat_types_table(curs):
	sql = '\n'.join([
		"CREATE TABLE feat_types (",
		"  feat_type_id INTEGER PRIMARY KEY,",
		"  section_id INTEGER NOT NULL,",
		"  feat_type TEXT"
		")"])
	curs.execute(sql)

def create_feat_types_index(curs):
	sql = '\n'.join([
		"CREATE INDEX feat_types_section_id",
		" ON feat_types (section_id)"])
	curs.execute(sql)

def insert_feat_type(curs, section_id, feat_type):
	values = [section_id, feat_type]
	sql = '\n'.join([
		"INSERT INTO feat_types",
		" (section_id, feat_type)",
		" VALUES",
		" (?, ?)"])
	curs.execute(sql, values)

def delete_feat_type(curs, section_id, feat_type=None):
	values = [section_id]
	sqla = [
		"DELETE FROM feat_types",
		" WHERE section_id = ?"]
	if feat_type:
		sqla.append("  AND feat_type = ?")
		values.append(feat_type)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_feat_types(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM feat_types",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def fetch_feats_by_type(curs, feat_type):
	values = [feat_type]
	sql = '\n'.join([
		"SELECT s.*",
		" FROM sections s, feat_types ft",
		" WHERE s.section_id = ft.section_id",
		"  AND ft.feat_type = ?"])
	curs.execute(sql, values)
