import json
import sys
import os
from psrd.sql.index import get_db_connection
from psrd.sql.index.central_index import fetch_index_by_url
from psrd.sql.index.url_ref import insert_url_reference

def load_url_reference(conn, struct):
	curs = conn.cursor()
	try:
		for item in struct:
			fetch_index_by_url(curs, item['new'])
			index = curs.fetchone()
			if not index:
				raise Exception("%s" % item['new'])
			index_id = index['index_id']
			insert_url_reference(curs, index_id, item['old'])
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
