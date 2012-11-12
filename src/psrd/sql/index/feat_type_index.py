def create_feat_type_index_table(curs):
	sql = '\n'.join([
		"CREATE TABLE feat_type_index (",
		"  feat_type_id INTEGER PRIMARY KEY,",
		"  index_id INTEGER,",
		"  feat_type TEXT",
		")"])
	curs.execute(sql)

def create_feat_type_index_indexes(curs):
	sql = '\n'.join([
		"CREATE INDEX feat_type_index_feat_type",
		" ON feat_type_index (feat_type)"])
	curs.execute(sql)

def insert_feat_type_index(curs, index_id, feat_type):
	values = [index_id, feat_type]
	sql = '\n'.join([
		"INSERT INTO feat_type_index",
		" (index_id, feat_type)",
		" VALUES",
		" (?, ?)"])
	curs.execute(sql, values)
	return curs.lastrowid

def delete_feat_type_index(curs, index_id, feat_type=None):
	values = [index_id]
	sqla = [
		"DELETE FROM feat_type_index",
		" WHERE section_id = ?"]
	if feat_type:
		sqla.append("  AND feat_type = ?")
		values.append(feat_type)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_feat_type_index(curs, index_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT *",
		" FROM feat_type_index",
		" WHERE index_id = ?"])
	curs.execute(sql, values)

def fetch_feats_by_type(curs, feat_type):
	values = [feat_type]
	sql = '\n'.join([
		"SELECT ci.*",
		" FROM central_index ci, feat_type_index ft",
		" WHERE ci.index_id = ft.index_id",
		"  AND ft.feat_type = ?"])
	curs.execute(sql, values)

