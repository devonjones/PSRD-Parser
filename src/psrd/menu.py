import json
import sys
import os
import psrd.sql.index.section_sort
from psrd.sql.index import get_db_connection
from psrd.sql.index.menu import insert_menu
from psrd.sql.index.central_index import select_section_types

def load_menu_structure(curs, struct, menu_id=None):
	for item in struct:
		children = []
		if item.has_key('children'):
			children = item['children']
			del item['children']
		if menu_id:
			item['parent_menu_id'] = menu_id
		new_menu_id = insert_menu(curs, **item)
		load_menu_structure(curs, children, new_menu_id)

def create_sort(conn):
	curs = conn.cursor()
	try:
		select_section_types(curs)
		types = curs.fetchall()
		psrd.sql.index.section_sort.create_sorts(curs, types)
		conn.commit()
	finally:
		curs.close()

def load_menu(db, args, parent):
	conn = get_db_connection(db)
	# Used for file loading additional indices
	for arg in args:
		print arg
		fp = open(arg, 'r')
		struct = json.load(fp)
		fp.close()
		curs = conn.cursor()
		try:
			load_menu_structure(curs, struct)
			create_sort(conn)
			conn.commit()
		finally:
			curs.close()
