
def create_section_table():
	sql = '\n'.join([
		"CREATE TABLE sections (",
		"  section_id INTEGER PRIMARY KEY,",
		"  type TEXT NOT NULL",
		"  lft INTEGER NOT NULL,",
		"  rgt INTEGER NOT NULL,",
		"  name TEXT,",
		"  abbrev TEXT,",
		"  source TEXT NOT NULL,",
		"  description TEXT",
		"  body TEXT"
		")"])

def create_tags_table():
	sql = '\n'.join([
		"CREATE TABLE tags (",
		"  tag_id  INTEGER PRIMARY KEY,",
		"  tag TEXT NOT NULL",
		")"])

def section_insert_top():
	sql = '\n'.join([
		"INSERT INTO sections",
		" (type, lft, rgt, name, source)",
		" VALUES",
		" ('section', 1, 2, 'PFSRD', 'PFSRD')")]

def _build_section_type(sqla, values, section_type):
	if section_type:
		if type(section_type) == list:
			sqla.append("  AND " + ', '.join(["%s" for st in section_type]))
			values.extend(section_type)
		else:
			sqla.append("  AND node.section_type = %s")
			values.append(section_type)

def fetch_section(section_id):
	values = [section_id]
	sql = '\n'.join([
		"SELECT section_id, name, section_type, section_text",
		" FROM sections",
		" WHERE section_id = %s"])

def fetch_section_subtree(parent_id, section_type=None):
	values = [parent_id]
	sqla = [
		"SELECT node.section_id, node.name, node.section_type, node.section_text",
		" FROM sections AS node, sections AS parent",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"  AND parent.section_id = %s"]
	_build_section_type(sqla, values, section_type)
	sqla.append(" ORDER BY node.lft")
	sql = '\n'.join(sqla)

def fetch_section_leaves(parent_id):
	sql = '\n'.join([
		"SELECT node.section_id, node.name, node.section_type, node.section_text",
		" FROM sections AS node, sections AS parent",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"  AND parent.section_id = %s",
		"  AND node.rgt = node.lft + 1",
		" ORDER BY node.lft"])

def fetch_section_path(section_id):
	sql = '\n'.join([
		"SELECT parent.section_id, parent.name, parent.section_type, node.section_text",
		" FROM sections AS node, sections AS parent",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"  AND node.section_id = %s",
		" ORDER BY node.lft"])

def fetch_section_full_tree_depth(section_type=None):
	values = []
	sqla = [
		"SELECT node.section_id, node.name, node.section_type, node.section_text,",
		"  (COUNT(parent.name) - 1) AS depth",
		" FROM sections AS node, sections AS parent",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt"]
	_build_section_type(sqla, values, section_type)
	sqla.append(" GROUP BY node.section_id")
	sqla.append(" ORDER BY node.lft")
	sql = '\n'.join(sqla)

def fetch_section_tree_depth_indented(parent_id, section_type=None):
	parent = fetch_section(parent_id)
	values = [parent['lft'], parent['rgt']]
	sqla = [
		"SELECT node.section_id, SUBSTR('                              ', 0, COUNT(parent.name)) || node.name,"
		"  node.section_type, node.section_text, (COUNT(parent.name) - 1) AS depth",
		" FROM sections AS node, sections AS parent",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"  AND parent.lft >= %s",
		"  AND parent.rgt <= %s"]
	_build_section_type(sqla, values, section_type)
	sqla.append(" GROUP BY node.section_id")
	sqla.append(" ORDER BY node.lft")
	sql = '\n'.join(sqla)

def fetch_section_tree_depth(parent_id, section_type=None, depth=None):
	values = [parent_id]
	sqla = [
		"SELECT node.section_id, node.name, node.section_type, node.section_text,",
		"  (COUNT(parent.name) - (sub_tree.depth + 1)) AS depth",
		" FROM sections AS node, sections AS parent, sections AS sub_parent, (",
		"   SELECT node.name, (COUNT(parent.name) - 1) AS depth",
		"    FROM sections AS node, sections AS parent",
		"    WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"     AND node.section_id = %s",
		"    GROUP BY node.name",
		"    ORDER BY node.lft",
		"   ) AS sub_tree",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"  AND node.lft BETWEEN sub_parent.lft AND sub_parent.rgt",
		"  AND sub_parent.name = sub_tree.name"]
	_build_section_type(sqla, values, section_type)
	sqla.append(" GROUP BY node.section_id")
	if depth:
		sqla.append(" HAVING depth <= %s")
		values.append(depth)
	sqla.append(" ORDER BY node.lft")
	sql = '\n'.join(sqla)

def fetch_immediate_subordinantes(parent_id, section_type=None):
	return fetch_section_tree_depth(parent_id, section_type, 1)

def insert_section_left(section_id, name, section_type, section_text):
	section = fetch_section(section_id)
	insert_child_section(name, section_type, section_text, section['lft'] - 1)

def insert_section_right(section_id, name, section_type, section_text):
	section = fetch_section(section_id)
	insert_child_section(name, section_type, section_text, section['rgt'])

def append_child_section(parent_id, name, section_type, section_text):
	parent = fetch_section(parent_id)
	insert_child_section(name, section_type, section_text, parent['rgt'] - 1)

def prepend_child_section(parent_id, name, section_type, section_text):
	parent = fetch_section(parent_id)
	insert_child_section(name, section_type, section_text, parent['lft'])

def insert_child_section(name, section_type, section_text, update_above):
	values = [update_above]
	sql = '\n'.join([
		"UPDATE nested_category",
		" SET rgt = rgt + 2",
		" WHERE rgt > %s"])
	sql = '\n'.join([
		"UPDATE nested_category",
		" SET lft = lft + 2"
		" WHERE lft > %s"])
	values = [name, update_above, update_above, section_type, section_text]
	sql = '\n'.join([
		"INSERT INTO sections",
		" (name, lft, rgt, section_type, section_text)",
		" VALUES",
		"(%s, %s + 1, %s + 2, %s, %s)"])

def delete_node_with_children(section_id):
	section = fetch_section(section_id)
	width = section['rgt'] - section['lft'] + 1
	values = [section['lft'], section['rgt']]
	sql = '\n'.join([
		"DELETE FROM sections",
		" WHERE lft BETWEEN %s AND %s"])
	values = [width, section['rgt']]
	sql = '\n'.join([
		"UPDATE sections",
		" SET rgt = rgt - %s",
		" WHERE rgt > %s"])
	sql = '\n'.join([
		"UPDATE sections"
		" SET lft = lft - %s"
		" WHERE lft > %s"])

def delete_node_promote_children(section_id):
	section = fetch_section(section_id)
	width = section['rgt'] - section['lft'] + 1
	values = [section['lft']]
	sql = '\n'.join([
		"DELETE FROM sections",
		" WHERE lft = %s"])
	values = [section['lft'], section['rgt']]
	sql = '\n'.join([
		"UPDATE nested_category",
		" SET rgt = rgt - 1,",
		"  lft = lft - 1",
		" WHERE lft BETWEEN %s AND %s"])
	values = [section['rgt']]
	sql = '\n'.join([
		"UPDATE nested_category",
		" SET rgt = rgt - 2",
		" WHERE rgt > %s"])
	sql = '\n'.join([
		"UPDATE nested_category",
		" SET lft = lft - 2",
		" WHERE lft > %s"])

