import json
import sys
import os
from psrd.sql import get_db_connection
from psrd.sql.sections import fetch_section_by_url
from psrd.sql.url_ref import insert_url_reference

def load_url_reference(conn, struct):
	curs = conn.cursor()
	try:
		for item in struct:
			fetch_section_by_url(curs, item['new'])
			section = curs.fetchone()
			if not section:
				raise Exception("'%s'" % item['new'])
			section_id = section['section_id']
			insert_url_reference(curs, section_id, item['old'])
		conn.commit()
	finally:
		curs.close()

def load_url_references(db, args, parent):
	conn = get_db_connection(db)
	# Used for file loading additional indices
	for arg in args:
		print arg
		fp = open(arg, 'r')
		struct = json.load(fp)
		fp.close()
		load_url_reference(conn, struct)
