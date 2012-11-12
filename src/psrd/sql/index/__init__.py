import os
import sqlite3
from psrd.sql.index.central_index import create_central_index_table
from psrd.sql.index.central_index import create_central_index_indexes
from psrd.sql.index.feat_type_index import create_feat_type_index_table
from psrd.sql.index.feat_type_index import create_feat_type_index_indexes
from psrd.sql.index.spell_list_index import create_spell_list_index_table
from psrd.sql.index.spell_list_index import create_spell_list_index_indexes
from psrd.sql.index.section_sort import create_section_sort_table
from psrd.sql.index.section_sort import create_section_sort_index
from psrd.sql.index.url_ref import create_url_references_table
from psrd.sql.index.url_ref import create_url_references_index

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
	create_central_index_table(curs)
	create_central_index_indexes(curs)
	create_feat_type_index_table(curs)
	create_feat_type_index_indexes(curs)
	create_spell_list_index_table(curs)
	create_spell_list_index_indexes(curs)
	create_section_sort_table(curs)
	create_section_sort_index(curs)
	create_url_references_table(curs)
	create_url_references_index(curs)
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

