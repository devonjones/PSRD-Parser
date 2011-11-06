import os
import sqlite3
from psrd.sql.feats import create_feat_type_table

def check_db_version(curs):
	sql = ''.join([
		"SELECT MAX(version)",
		" FROM database_version"])
	curs.execute(sql)
	row = curs.fetchone()
	return row[0]

def set_version(curs, ver):
	sql = ''.join([
		"INSERT INTO database_version",
		" (version)",
		" VALUES (?)"])
	curs.execute(sql, (str(ver), ))

def create_db_v_1(conn, curs):
	sql = ''.join([
		"CREATE TABLE IF NOT EXISTS database_version(",
		"  id INTEGER PRIMARY KEY,",
		"  version INTEGER)"])
	curs.execute(sql)
	ver = check_db_version(curs)
	if not ver:
		ver = 1
		set_version(curs, ver)
	conn.commit()
	return ver

def create_db_v_2(conn, curs, ver):
	if ver >= 2:
		return ver
	ver = 2
	create_section_table(curs)
	create_feat_type_table(curs)
	section_insert_top(curs)
	set_version(curs, ver)
	conn.commit()
	return ver

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_db_connection(db):
	conn = sqlite3.connect(os.path.expanduser(db))
	curs = conn.cursor()
	try:
		ver = create_db_v_1(conn, curs)
		ver = create_db_v_2(conn, curs, ver)
	finally:
		curs.close()
	conn.row_factory = dict_factory
	return conn

def create_section_table(curs):
	sql = '\n'.join([
		"CREATE TABLE sections (",
		"  section_id INTEGER PRIMARY KEY,",
		"  type TEXT NOT NULL,",
		"  lft INTEGER NOT NULL,",
		"  rgt INTEGER NOT NULL,",
		"  name TEXT,",
		"  abbrev TEXT,",
		"  source TEXT NOT NULL,",
		"  description TEXT,",
		"  body TEXT"
		")"])
	curs.execute(sql)

def create_tags_table(curs):
	sql = '\n'.join([
		"CREATE TABLE tags (",
		"  tag_id  INTEGER PRIMARY KEY,",
		"  tag TEXT NOT NULL",
		")"])
	curs.execute(sql)

def section_insert_top(curs):
	sql = '\n'.join([
		"INSERT INTO sections",
		" (type, lft, rgt, name, source)",
		" VALUES",
		" ('section', 1, 2, 'PFSRD', 'PFSRD')"])
	curs.execute(sql)
	return curs.lastrowid

def _build_section_type(sqla, values, section_type):
	if section_type:
		if type(section_type) == list:
			sqla.append("  AND (" + ' OR '.join(["node.section_type = ?" for st in section_type])) + ")"
			values.extend(section_type)
		else:
			sqla.append("  AND node.section_type = ?")
			values.append(section_type)

def fetch_top(curs):
	sql = '\n'.join([
		"SELECT section_id, lft, rgt, type, name, abbrev, source, description, body",
		" FROM sections",
		" WHERE lft = 1"])
	curs.execute(sql)
	return curs.fetchone()

def fetch_section(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT section_id, lft, rgt, type, name, abbrev, source, description, body",
		" FROM sections",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def find_section(curs, name=None, section_type=None, source=None):
	values = []
	where = " WHERE"
	sqla = [
		"SELECT section_id, lft, rgt, type, name, abbrev, source, description, body",
		" FROM sections"]
	if name:
		sqla.append(where + " name = ?")
		where = "  AND"
		values.append(name)
	if section_type:
		sqla.append(where + " type = ?")
		where = "  AND"
		values.append(section_type)
	if source:
		sqla.append(where + " source = ?")
		values.append(source)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_section_subtree(curs, parent_id, section_type=None):
	values = [parent_id]
	sqla = [
		"SELECT node.section_id, node.lft, node.rgt, node.type, node.name, node.abbrev, node.source, node.description, node.body",
		" FROM sections AS node, sections AS parent",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"  AND parent.section_id = ?"]
	_build_section_type(sqla, values, section_type)
	sqla.append(" ORDER BY node.lft")
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_section_leaves(curs, parent_id):
	sql = '\n'.join([
		"SELECT node.section_id, node.lft, node.rgt, node.type, node.name, node.abbrev, node.source, node.description, node.body",
		" FROM sections AS node, sections AS parent",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"  AND parent.section_id = ?",
		"  AND node.rgt = node.lft + 1",
		" ORDER BY node.lft"])
	curs.execute(sql, (parent_id))

def fetch_section_path(curs, section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT parent.section_id, parent.lft, parent.rgt, parent.type, parent.name, parent.abbrev, parent.source, parent.description, parent.body",
		" FROM sections AS node, sections AS parent",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"  AND node.section_id = ?",
		" ORDER BY node.lft"])
	curs.execute(sql, values)

def fetch_section_full_tree_depth(curs, section_type=None):
	values = []
	sqla = [
		"SELECT node.section_id, node.lft, node.rgt, node.type, node.name, node.abbrev, node.source, node.description, node.body,",
		"  (COUNT(parent.name) - 1) AS depth",
		" FROM sections AS node, sections AS parent",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt"]
	_build_section_type(sqla, values, section_type)
	sqla.append(" GROUP BY node.section_id")
	sqla.append(" ORDER BY node.lft")
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_section_tree_depth_indented(curs, parent_id, section_type=None):
	parent = fetch_section(parent_id)
	values = [parent['lft'], parent['rgt']]
	sqla = [
		"SELECT node.section_id, node.lft, node.rgt, node.type, SUBSTR('                              ', 0, COUNT(parent.name)) || node.name,"
		"   node.abbrev, node.source, node.description, node.body, (COUNT(parent.name) - 1) AS depth",
		" FROM sections AS node, sections AS parent",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"  AND parent.lft >= ?",
		"  AND parent.rgt <= ?"]
	_build_section_type(sqla, values, section_type)
	sqla.append(" GROUP BY node.section_id")
	sqla.append(" ORDER BY node.lft")
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_section_tree_depth(curs, parent_id, section_type=None, depth=None):
	values = [parent_id]
	sqla = [
		"SELECT node.section_id, node.lft, node.rgt, node.type, node.name, node.abbrev, node.source, node.description, node.body,",
		"  (COUNT(parent.name) - (sub_tree.depth + 1)) AS depth",
		" FROM sections AS node, sections AS parent, sections AS sub_parent, (",
		"   SELECT node.name, (COUNT(parent.name) - 1) AS depth",
		"    FROM sections AS node, sections AS parent",
		"    WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"     AND node.section_id = ?",
		"    GROUP BY node.name",
		"    ORDER BY node.lft",
		"   ) AS sub_tree",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"  AND node.lft BETWEEN sub_parent.lft AND sub_parent.rgt",
		"  AND sub_parent.name = sub_tree.name"]
	_build_section_type(sqla, values, section_type)
	sqla.append(" GROUP BY node.section_id")
	if depth:
		sqla.append(" HAVING depth <= ?")
		values.append(depth)
	sqla.append(" ORDER BY node.lft")
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_immediate_subordinantes(curs, parent_id, section_type=None):
	return fetch_section_tree_depth(curs, parent_id, section_type, 1)

def insert_section_left(curs, section_id, section_type, name, abbrev, source, description, text):
	fetch_section(curs, section_id)
	section = curs.fetchone()
	return insert_child_section(curs, section['lft'] - 1, section_type, name, abbrev, source, description, text)

def insert_section_right(curs, section_id, section_type, name, abbrev, source, description, text):
	fetch_section(curs, section_id)
	section = curs.fetchone()
	return insert_child_section(curs, section['rgt'], section_type, name, abbrev, source, description, text)

def append_child_section(curs, parent_id, section_type, name, abbrev, source, description, text):
	fetch_section(curs, parent_id)
	parent = curs.fetchone()
	return insert_child_section(curs, parent['rgt'] - 1, section_type, name, abbrev, source, description, text)

def prepend_child_section(curs, parent_id, section_type, name, abbrev, source, description, text):
	fetch_section(curs, parent_id)
	parent = curs.fetchone()
	return insert_child_section(curs, parent['lft'], section_type, name, abbrev, source, description, text)

def insert_child_section(curs, update_above, section_type, name, abbrev, source, description, text):
	values = [update_above]
	sql = '\n'.join([
		"UPDATE nested_category",
		" SET rgt = rgt + 2",
		" WHERE rgt > ?"])
	sql = '\n'.join([
		"UPDATE nested_category",
		" SET lft = lft + 2"
		" WHERE lft > ?"])
	values = [update_above, update_above, section_type, name, abbrev, source, description, text]
	sql = '\n'.join([
		"INSERT INTO sections",
		" (lft, rgt, type, name, abbrev, source, description, body)",
		" VALUES",
		"(? + 1, ? + 2, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)
	return curs.lastrowid

def delete_node_with_children(curs, section_id):
	section = fetch_section(section_id)
	width = section['rgt'] - section['lft'] + 1
	values = [section['lft'], section['rgt']]
	sql = '\n'.join([
		"DELETE FROM sections",
		" WHERE lft BETWEEN ? AND ?"])
	values = [width, section['rgt']]
	sql = '\n'.join([
		"UPDATE sections",
		" SET rgt = rgt - ?",
		" WHERE rgt > ?"])
	sql = '\n'.join([
		"UPDATE sections"
		" SET lft = lft - ?"
		" WHERE lft > ?"])
	curs.execute(sql, values)

def delete_node_promote_children(curs, section_id):
	section = fetch_section(section_id)
	width = section['rgt'] - section['lft'] + 1
	values = [section['lft']]
	sql = '\n'.join([
		"DELETE FROM sections",
		" WHERE lft = ?"])
	values = [section['lft'], section['rgt']]
	sql = '\n'.join([
		"UPDATE sections",
		" SET rgt = rgt - 1,",
		"  lft = lft - 1",
		" WHERE lft BETWEEN ? AND ?"])
	values = [section['rgt']]
	sql = '\n'.join([
		"UPDATE sections",
		" SET rgt = rgt - 2",
		" WHERE rgt > ?"])
	sql = '\n'.join([
		"UPDATE sections",
		" SET lft = lft - 2",
		" WHERE lft > ?"])
	curs.execute(sql, values)

