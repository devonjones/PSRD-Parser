#!/usr/bin/env python
import sys
import json
from optparse import OptionParser
from psrd.sql import get_db_connection, find_section, update_section
from psrd.sql.items import update_item_detail, fetch_item_misc, delete_item_misc, insert_item_misc
from psrd.extensions.loader import filter_section_fields, filter_item_details_fields

def process_item(conn, curs, section, update):
	fields = filter_item_details_fields(update)
	if len(fields) > 0:
		update_item_detail(curs, section['section_id'], **fields)

def process_section(conn, curs, section, update):
	fields = filter_section_fields(update)
	if len(fields) > 0:
		update_section(curs, section['section_id'], **fields)
	if update.has_key('misc'):
		for misc in update['misc']:
			fetch_item_misc(curs, section['section_id'],
					field=misc.get('field', None),
					subsection=misc.get('subsection'))
			existing = curs.fetchone()
			if existing:
				delete_item_misc(curs, existing['item_misc_id'])
			insert_item_misc(curs, section['section_id'], **misc)

def process_update(conn, curs, update):
	find_section(curs, **{"url": update['url']})
	section = curs.fetchone()
	if not section:
		raise Exception("Can't find section with name: %s" % update['url'])
	process_section(conn, curs, section, update)
	if section['type'] == 'item' or update.get('type') == 'item':
		process_item(conn, curs, section, update)

def load_extension(conn, extension):
	curs = conn.cursor()
	try:
		with open(extension) as jsonfile:
			data = json.load(jsonfile)
			for update in data:
				process_update(conn, curs, update)
		conn.commit()
	finally:
		conn.rollback()
		curs.close()

def load_extensions(db, extensions):
	conn = get_db_connection(db)
	for extension in extensions:
		load_extension(conn, extension)

def option_parser(usage):
	parser = OptionParser(usage=usage)
	parser.add_option(
		"-d", "--db", dest="db", help="Sqlite DB to load into (required)")
	return parser

def main():
	usage = "usage: %prog [options] [files]\nLoads extension information into db.."
	parser = option_parser(usage)
	(options, args) = parser.parse_args()
	if not options.db:
		sys.stderr.write("-d/--db required\n")
		sys.exit(1)
	load_extensions(options.db, args)

if __name__ == "__main__":
	sys.exit(main())

