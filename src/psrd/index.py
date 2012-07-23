import json
import sys
import os
from psrd.sql import get_db_connection
from psrd.sql import find_section, fetch_top, append_child_section, fetch_section, update_section
from psrd.sql.section_index import fetch_indexable_sections, count_sections_with_name, fetch_index, insert_index, strip_unindexed_urls

def save_index(curs, section_id, search_name):
	fetch_index(curs, section_id, search_name)
	if not curs.fetchone():
		insert_index(curs, section_id, search_name)

def index_section(curs, section):
	if section['name'] == section['parent_name']:
		if section['type'] == 'section':
			# if a section has the same name as it's parent and it is not
			# a more interesting type then 'section', don't index it
			return
	if section['type'] != 'section':
		save_index(curs, section['section_id'], section['name'])
	elif section['subtype'] != None:
		save_index(curs, section['section_id'], section['name'])
	else:
		count_sections_with_name(curs, section['name'])
		rec = curs.fetchone()
		if rec['cnt'] <= 5:
			save_index(curs, section['section_id'], section['name'])

def build_default_index(db, conn):
	curs = conn.cursor()
	try:
		fetch_indexable_sections(curs)
		section = curs.fetchone()
		while section:
			index_section(conn.cursor(), section)
			section = curs.fetchone()
		conn.commit()
	finally:
		curs.close()

def load_additional_index_entries(db, conn, filename, struct):
	curs = conn.cursor()
	try:
		find_section(curs, name=struct['name'])
		parent = curs.fetchone()
		if struct.has_key('file'):
			print struct['file']
		for child in struct['children']:
			pass
			#process_structure_node(curs, filename, parent, child) 
		conn.commit()
	finally:
		curs.close()

def strip_urls(conn):
	curs = conn.cursor()
	try:
		strip_unindexed_urls(curs)
		conn.commit()
	finally:
		curs.close()

def load_section_index(db, args, parent):
	conn = get_db_connection(db)
	build_default_index(db, conn)
	# Used for file loading additional indices
	for arg in args:
		fp = open(arg, 'r')
		struct = json.load(fp)
		fp.close()
		load_additional_index_entries(db, conn, arg, struct)
	strip_urls(conn)
