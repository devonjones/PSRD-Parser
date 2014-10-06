#!/usr/bin/env python
import sys
from optparse import OptionParser
from psrd.sql import get_db_connection, find_section
from psrd.table.weapon import parse_weapon_table
from psrd.table.armor import parse_armor_table
from psrd.table.gear import parse_gear_table_closure
from psrd.table.gear import parse_gear_header, parse_gear_header2
from psrd.table.gear import siege_engine_modifier_clear
from psrd.table.io import load_extension_file, produce_output, write_output

def find_section_subtree(curs, parent_id, **kwargs):
	# There may be many rows in the result set.
	values = [parent_id]
	sqla = [
		"SELECT node.section_id, node.lft, node.rgt, node.parent_id,"
		+ " node.type, node.subtype, node.name, node.abbrev, node.source,"
		+ " node.description, node.body, node.image, node.alt, node.url,"
		+ " node.create_index",
		" FROM sections AS node, sections AS parent",
		" WHERE node.lft BETWEEN parent.lft AND parent.rgt",
		"  AND parent.section_id = ?"]
	for key in kwargs.keys():
		sqla.append("  AND " + key + " = ?")
		values.append(kwargs[key])
	sqla.append(" COLLATE NOCASE")
	sqla.append(" ORDER BY node.lft")
	sql = '\n'.join(sqla)
	curs.execute(sql, values)

def update_sections(curs, section_cache, table_data, table, item):
	section = get_section(curs, section_cache, table_data, table, item['Name'])
	if section:
		section['changes'].append(item)
	alternate_urls = table_data.get('alternate_urls', {})
	for url in alternate_urls.get(item['Name'], []):
		section = section_cache.get(url)
		if not section:
			find_section(curs, **{"url": url})
			alt = curs.fetchone()
			section_cache[alt['url']] = {"section": alt, "changes":[]}
			section = section_cache[alt['url']]
		if not section:
			sys.stderr.write("%s : not found\n" % url)
			return
		section['changes'].append(item)

def get_section(curs, section_cache, table_data, table, name):
	section = connect_section(curs, table, name)
	if not section:
		section = connect_section_remap(
				curs, table_data, table, name)
	if not section:
		sys.stderr.write("%s : not found\n" % name)
		return
	if not section['url'] in section_cache:
		section_cache[section['url']] = {"section": section, "changes":[]}
	return section_cache[section['url']]

def connect_section_remap(curs, extensions, table, weapon_name):
	renames = extensions.setdefault('alternate_names', {})
	if weapon_name in renames:
		return connect_section(curs, table, renames[weapon_name])

def connect_section(curs, table, weapon_name):
	find_section_subtree(
		curs, **{
			'parent_id': table['parent_id'],
			'node.name': weapon_name,
			'node.type': 'item'})
	results = curs.fetchall()
	if len(results) == 0:
		return
	if len(results) > 1:
		sys.stderr.write("%s : multiple results found\n" % weapon_name)
		return
	return results[0]

def get_parser(parser_name):
	parsers = {
		'weapons': parse_weapon_table,
		'armor': parse_armor_table,
		'gear': parse_gear_table_closure(parse_gear_header),
		'gear2': parse_gear_table_closure(parse_gear_header2),
		'siege': parse_gear_table_closure(
			parse_gear_header2, siege_engine_modifier_clear)
	}
	if parser_name in parsers:
		return parsers[parser_name]
	else:
		raise Exception("parser %s does not exist" % parser_name)

def dump_table(output_dir, db, book):
	extensions = load_extension_file(output_dir, book)
	conn = get_db_connection(db, source=book)
	curs = conn.cursor()
	section_cache = {}
	for table_data in extensions['tables']:
		url = table_data['url']
		find_section(curs, **{"url": url})
		table = curs.fetchone()
		parser = get_parser(table_data['parser'])
		items = parser(table, table_data)
		for item in items:
			update_sections(curs, section_cache, table_data, table, item)
	urls = section_cache.keys()
	urls.sort()
	output = produce_output([section_cache[url] for url in urls])
	write_output(output_dir, book, output)

def option_parser(usage):
	parser = OptionParser(usage=usage)
	parser.add_option(
		"-o", "--output", dest="output",
		help="Output data directory.  Should be top level directory of psrd data. (required)")
	parser.add_option(
		"-d", "--db", dest="db", help="Sqlite DB to load into (required)")
	parser.add_option(
		"-b", "--book", dest="book", help="Book items are from (required)")
	return parser

def main():
	usage = "usage: %prog [options] [pfsrd url]\nDumps weapon information from tables."
	parser = option_parser(usage)
	(options, _) = parser.parse_args()
	if not options.db:
		sys.stderr.write("-d/--db required\n")
		sys.exit(1)
	if not options.output:
		sys.stderr.write("-o/--output required\n")
		sys.exit(1)
	if not options.book:
		sys.stderr.write("-b/--book required")
		sys.exit(1)
	dump_table(options.output, options.db, options.book)

if __name__ == "__main__":
	sys.exit(main())

