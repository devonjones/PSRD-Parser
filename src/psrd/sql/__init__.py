import os
import sqlite3
from psrd.sql.abilities import create_ability_types_table, create_ability_types_index
from psrd.sql.afflictions import create_affliction_details_table, create_affliction_details_index
from psrd.sql.classes import create_class_details_table, create_class_details_index
from psrd.sql.creatures import create_creature_details_table, create_creature_details_index, create_creature_spells_table, create_creature_spells_index
from psrd.sql.animal_companions import create_animal_companion_details_table, create_animal_companion_details_index
from psrd.sql.settlements import create_settlement_details_table, create_settlement_details_index
from psrd.sql.vehicles import create_vehicle_details_table, create_vehicle_details_index
from psrd.sql.traps import create_trap_details_table, create_trap_details_index
from psrd.sql.haunts import create_haunt_details_table, create_haunt_details_index
from psrd.sql.items import create_item_details_table, create_item_details_index, create_item_misc_table, create_item_misc_index
from psrd.sql.feats import create_feat_types_table, create_feat_types_index, create_feat_type_descriptions_table, create_feat_type_descriptions_index
from psrd.sql.links import create_link_details_table, create_link_details_index
from psrd.sql.section_index import create_section_index_table, create_section_index_index
from psrd.sql.skills import create_skill_attributes_table, create_skill_attributes_index
from psrd.sql.spells import create_spell_details_table, create_spell_details_index, create_spell_lists_table, create_spell_lists_index, create_spell_descriptors_table, create_spell_descriptors_index, create_spell_components_table, create_spell_components_index, create_spell_effects_table, create_spell_effects_index
from psrd.sql.url_ref import create_url_references_table
from psrd.sql.url_ref import create_url_references_index

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

def create_db_v_2(conn, curs, ver, source=None):
	if ver >= 2:
		return ver
	ver = 2
	create_sections_table(curs)
	create_sections_index(curs)
	create_class_details_table(curs)
	create_class_details_index(curs)
	create_feat_types_table(curs)
	create_feat_types_index(curs)
	create_feat_type_descriptions_table(curs)
	create_feat_type_descriptions_index(curs)
	create_skill_attributes_table(curs)
	create_skill_attributes_index(curs)
	create_ability_types_table(curs)
	create_ability_types_index(curs)
	create_affliction_details_table(curs)
	create_affliction_details_index(curs)
	create_animal_companion_details_table(curs)
	create_animal_companion_details_index(curs)
	create_vehicle_details_table(curs)
	create_vehicle_details_index(curs)
	create_settlement_details_table(curs)
	create_settlement_details_index(curs)
	create_creature_details_table(curs)
	create_creature_details_index(curs)
	create_creature_spells_table(curs)
	create_creature_spells_index(curs)
	create_trap_details_table(curs)
	create_trap_details_index(curs)
	create_haunt_details_table(curs)
	create_haunt_details_index(curs)
	create_item_details_table(curs)
	create_item_details_index(curs)
	create_item_misc_table(curs)
	create_item_misc_index(curs)
	create_link_details_table(curs)
	create_link_details_index(curs)
	create_section_index_table(curs)
	create_section_index_index(curs)
	create_spell_details_table(curs)
	create_spell_details_index(curs)
	create_spell_lists_table(curs)
	create_spell_lists_index(curs)
	create_spell_descriptors_table(curs)
	create_spell_descriptors_index(curs)
	create_spell_components_table(curs)
	create_spell_components_index(curs)
	create_spell_effects_table(curs)
	create_spell_effects_index(curs)
	create_url_references_table(curs)
	create_url_references_index(curs)
	if source:
		section_insert_top(curs, source)
	set_version(curs, ver)
	conn.commit()
	return ver

def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

def get_db_connection(db, source=None):
	conn = sqlite3.connect(os.path.expanduser(db))
	curs = conn.cursor()
	try:
		ver = create_db_v_1(conn, curs)
		ver = create_db_v_2(conn, curs, ver, source)
	finally:
		curs.close()
	conn.row_factory = dict_factory
	return conn

def create_sections_table(curs):
	sql = '\n'.join([
		"CREATE TABLE sections (",
		"  section_id INTEGER PRIMARY KEY,",
		"  type TEXT NOT NULL,",
		"  subtype TEXT,",
		"  lft INTEGER NOT NULL,",
		"  rgt INTEGER NOT NULL,",
		"  parent_id INTEGER,",
		"  name TEXT,",
		"  abbrev TEXT,",
		"  source TEXT NOT NULL,",
		"  description TEXT,",
		"  body TEXT,",
		"  image TEXT,",
		"  alt TEXT,",
		"  url TEXT,",
		"  create_index BOOLEAN",
		")"])
	curs.execute(sql)

def create_sections_index(curs):
	sql = '\n'.join([
		"CREATE INDEX sections_type",
		" ON sections (type)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX sections_subtype",
		" ON sections (subtype)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX sections_lft",
		" ON sections (lft)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX sections_rgt",
		" ON sections (rgt)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX sections_parents",
		" ON sections (parent_id)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX sections_name",
		" ON sections (name)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX sections_source",
		" ON sections (source)"])
	curs.execute(sql)
	sql = '\n'.join([
		"CREATE INDEX sections_url",
		" ON sections (url)"])
	curs.execute(sql)

def create_tags_table(curs):
	sql = '\n'.join([
		"CREATE TABLE tags (",
		"  tag_id  INTEGER PRIMARY KEY,",
		"  tag TEXT NOT NULL",
		")"])
	curs.execute(sql)

def section_insert_top(curs, source):
	url = source.replace(':', '')
	url = url.replace('&', 'and')
	url = url.replace('?', '')
	url = url.replace("'", '')
	url = 'pfsrd://' + url
	sql = '\n'.join([
		"INSERT INTO sections",
		" (type, lft, rgt, name, source, url)",
		" VALUES",
		" ('section', 1, 2, ?, ?, ?)"])
	curs.execute(sql, (source, source, url))

def _build_section_type(sqla, values, section_type):
	if section_type:
		if type(section_type) == list:
			sqla.append("  AND (" + ' OR '.join(["node.type = ?" for _ in section_type]) + ")")
			values.extend(section_type)
		else:
			sqla.append("  AND node.type = ?")
			values.append(section_type)

def fetch_top(curs):
	# There will only be one row in the result set.
	sql = '\n'.join([
		"SELECT section_id, lft, rgt, type, subtype, name, abbrev, source, description, body, image, alt, url, create_index",
		" FROM sections",
		" WHERE lft = 1"])
	curs.execute(sql)

def fetch_section(curs, section_id):
	# There will only be one row in the result set.
	values = [section_id]
	sql = '\n'.join([
		"SELECT section_id, lft, rgt, parent_id, type, subtype, name, abbrev, source, description, body, image, alt, url, create_index",
		" FROM sections",
		" WHERE section_id = ?"])
	curs.execute(sql, values)

def find_section(curs, **kwargs):
	# There may be many rows in the result set.
	values = []
	where = " WHERE "
	sqla = [
		"SELECT section_id, lft, rgt, parent_id, type, subtype, name, abbrev, source, description, body, image, alt, url, create_index",
		" FROM sections"]
	for key in kwargs.keys():
		sqla.append(where + key + " = ?")
		values.append(kwargs[key])
		where = "  AND "
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_section_subtree(curs, parent_id, section_type=None):
	# There may be many rows in the result set.
	values = [parent_id]
	sqla = [
		"SELECT node.section_id, node.lft, node.rgt, node.parent_id, node.type, node.subtype, node.name, node.abbrev, node.source, node.description, node.body, node.image, node.alt, node.url, node.create_index",
		" FROM sections AS node, sections AS parent",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"  AND parent.section_id = ?"]
	_build_section_type(sqla, values, section_type)
	sqla.append(" ORDER BY node.lft")
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_section_leaves(curs, parent_id):
	# There may be many rows in the result set.
	sql = '\n'.join([
		"SELECT node.section_id, node.lft, node.rgt, node.parent_id, node.type, node.subtype, node.name, node.abbrev, node.source, node.description, node.body, node.image, node.alt, node.url, node.create_index",
		" FROM sections AS node, sections AS parent",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"  AND parent.section_id = ?",
		"  AND node.rgt = node.lft + 1",
		" ORDER BY node.lft"])
	curs.execute(sql, (parent_id,))

def fetch_section_path(curs, section_id):
	# There may be many rows in the result set.
	values = [section_id]
	sql = '\n'.join([
		"SELECT parent.section_id, parent.lft, parent.rgt, parent.parent_id, parent.type, parent.subtype, parent.name, parent.abbrev, parent.source, parent.description, parent.body, parent.image, parent.alt, parent.url, parent.create_index",
		" FROM sections AS node, sections AS parent",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"  AND node.section_id = ?",
		" ORDER BY parent.lft"])
	curs.execute(sql, values)

def fetch_section_full_tree_depth(curs, section_type=None):
	# There may be many rows in the result set.
	values = []
	sqla = [
		"SELECT node.section_id, node.lft, node.rgt, node.parent_id, node.type, node.subtype, node.name, node.abbrev, node.source, node.description, node.body, node.image, node.alt, node.url, node.create_index,",
		"  (COUNT(parent.name) - 1) AS depth",
		" FROM sections AS node, sections AS parent",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt"]
	_build_section_type(sqla, values, section_type)
	sqla.append(" GROUP BY node.section_id")
	sqla.append(" ORDER BY node.lft")
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_section_tree_depth_indented(curs, parent_id, section_type=None):
	# There may be many rows in the result set.
	# FIXME: This took 10 minutes to return 7 results for parent_id=10122.
	parent = fetch_section(curs, parent_id)
	values = [parent['lft'], parent['rgt']]
	sqla = [
		"SELECT node.section_id, node.lft, node.rgt, node.parent_id, node.type, node.subtype, SUBSTR('                              ', 0, COUNT(parent.name)) || node.name AS name,"
		"   node.abbrev, node.source, node.description, node.body, node.image, node.alt, node.url, node.create_index, (COUNT(parent.name) - 1) AS depth",
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
	# There may be many rows in the result set.
	values = [parent_id]
	sqla = [
		"SELECT node.section_id, node.lft, node.rgt, node.parent_id, node.type, node.subtype, node.name, node.abbrev, node.source, node.description, node.body, node.image, node.alt, node.url, node.create_index,",
		"  (COUNT(parent.section_id) - (sub_tree.sdepth + 1)) AS depth",
		" FROM sections AS node, sections AS parent, sections AS sub_parent, (",
		"   SELECT snode.section_id, (COUNT(sparent.section_id) - 1) AS sdepth",
		"    FROM sections AS snode, sections AS sparent",
		"    WHERE snode.lft BETWEEN sparent.lft AND sparent.rgt",
		"     AND snode.section_id = ?",
		"    GROUP BY snode.section_id",
		"    ORDER BY snode.lft",
		"   ) AS sub_tree",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"  AND node.lft BETWEEN sub_parent.lft AND sub_parent.rgt",
		"  AND sub_parent.section_id = sub_tree.section_id"]
	_build_section_type(sqla, values, section_type)
	sqla.append(" GROUP BY node.section_id")
	if depth:
		sqla.append(" HAVING depth <= ?")
		values.append(depth)
	sqla.append(" ORDER BY node.lft")
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def fetch_immediate_subordinantes(curs, parent_id, section_type=None):
	# There may be many rows in the result set.
	fetch_section_tree_depth(curs, parent_id, section_type, 1)

def insert_section_left(curs, section_id, section_type, subtype, name, abbrev, source, description, text, image, alt, url, create_index):
	fetch_section(curs, section_id)
	section = curs.fetchone()
	insert_child_section(curs, section['lft'] - 1, section['parent_id'], section_type, subtype, name, abbrev, source, description, text, image, alt, url, create_index)
	return curs.lastrowid

def insert_section_right(curs, section_id, section_type, subtype, name, abbrev, source, description, text, image, alt, url, create_index):
	fetch_section(curs, section_id)
	section = curs.fetchone()
	insert_child_section(curs, section['rgt'], section['parent_id'], section_type, subtype, name, abbrev, source, description, text, image, alt, url, create_index)
	return curs.lastrowid

def append_child_section(curs, parent_id, section_type, subtype, name, abbrev, source, description, text, image, alt, url, create_index):
	fetch_section(curs, parent_id)
	parent = curs.fetchone()
	insert_child_section(curs, parent['rgt'] - 1, parent_id, section_type, subtype, name, abbrev, source, description, text, image, alt, url, create_index)
	return curs.lastrowid

def prepend_child_section(curs, parent_id, section_type, subtype, name, abbrev, source, description, text, image, alt, url, create_index):
	fetch_section(curs, parent_id)
	parent = curs.fetchone()
	insert_child_section(curs, parent['lft'], parent_id, section_type, subtype, name, abbrev, source, description, text, image, alt, url, create_index)
	return curs.lastrowid

def insert_child_section(curs, update_above, parent_id, section_type, subtype, name, abbrev, source, description, text, image, alt, url, create_index):
	if text and text.find('\n') > -1:
		text = text.replace('\n', '')
	values = [update_above]
	sql = '\n'.join([
		"UPDATE sections",
		" SET rgt = rgt + 2",
		" WHERE rgt > ?"])
	curs.execute(sql, values)
	sql = '\n'.join([
		"UPDATE sections",
		" SET lft = lft + 2"
		" WHERE lft > ?"])
	curs.execute(sql, values)
	if name and name.strip() == '':
		name = None
	values = [update_above, update_above, parent_id, section_type, subtype, name, abbrev, source, description, text, image, alt, url, create_index]
	sql = '\n'.join([
		"INSERT INTO sections",
		" (lft, rgt, parent_id, type, subtype, name, abbrev, source, description, body, image, alt, url, create_index)",
		" VALUES",
		"(? + 1, ? + 2, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"])
	curs.execute(sql, values)

def update_section(curs, section_id, description=None):
	values = []
	sqla = ["UPDATE sections"]
	sep = " SET"
	if description:
		sqla.append(sep)
		sqla.append(" description = ?")
		sep = ", "
		values.append(description)
	sqla.append(" WHERE section_id = ?")
	values.append(section_id)
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def delete_node_with_children(curs, section_id):
	section = fetch_section(curs, section_id)
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
	section = fetch_section(curs, section_id)
	width = section['rgt'] - section['lft'] + 1 # FIXME: width is not used
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

def select_section_types(curs):
	sql = '\n'.join([
		"SELECT DISTINCT type",
		" FROM sections"])
	curs.execute(sql)
