#!/usr/bin/env python
import sys
import json
import os
import os.path
from optparse import OptionParser
from psrd.sql import get_db_connection, find_section
from psrd.files import makedirs, char_replace
from psrd.dump.types import fetch_subrecords

def find_types(curs):
	# There may be many rows in the result set.
	sql = sql = '\n'.join([
		"SELECT DISTINCT type",
		" FROM sections"])
	curs.execute(sql)

def find_rules(curs):
	# There may be many rows in the result set.
	sql = sql = '\n'.join([
		"SELECT s.*",
		" FROM sections s",
		"  INNER JOIN sections p",
		"   ON s.parent_id = p.section_id",
		" WHERE p.name = 'Rules'",
		"  AND p.type = 'list'"])
	curs.execute(sql)

def filter_types(types):
	types_to_filter = set([
		"ability",
		"embed",
		"section",
		"table",
		"list",
		"link"])
	return list(set(types) - types_to_filter)

def construct_type_path(output, book, section):
	typedir = os.path.abspath(
		output + "/" +
		char_replace(book) + "/" +
		char_replace(section['type']))
	if section.has_key('subtype'):
		typedir += "/" + section['subtype']
		if not os.path.exists(typedir):
			os.makedirs(typedir)
	typefile = typedir + "/" + char_replace(section['name']) + ".json"
	if os.path.exists(typefile):
		sys.stderr.write("File %s already exists\n" % typefile)
		#raise Exception("File %s already exists" % typefile)
	return typefile

def construct_rule_path(output, book, section, path):
	full = "/".join([char_replace(p) for p in path])
	typedir = os.path.abspath(
		output + "/" +
		char_replace(book) + "/" +
		full)
	if not os.path.exists(typedir):
		os.makedirs(typedir)
	typefile = typedir + "/" + char_replace(section['name']) + ".json"
	if os.path.exists(typefile):
		sys.stderr.write("File %s already exists\n" % typefile)
		#raise Exception("File %s already exists" % typefile)
	return typefile

def get_types(curs):
	find_types(curs)
	types = []
	for t in curs.fetchall():
		types.append(t['type'])
	return filter_types(types)

def get_rules(curs):
	find_rules(curs)
	return curs.fetchall()

def write_type_section(output, book, section):
	filename = construct_type_path(output, book, section)
	with open(filename, 'w') as fp:
		json.dump(section, fp, indent=4)

def write_rule_section(output, book, section, path):
	filename = construct_rule_path(output, book, section, path)
	with open(filename, 'w') as fp:
		json.dump(section, fp, indent=4)

def dump_section(conn, section):
	fetch_subrecords(conn, section)
	curs = conn.cursor()
	try:
		find_section(curs, parent_id=section['section_id'])
		sections = []
		for ss in curs.fetchall():
			ss = dump_section(conn, ss)
			sections.append(ss)
		if len(sections) > 0:
			section['sections'] = sections
		del section['lft']
		del section['rgt']
		del section['parent_id']
		del section['section_id']
		del section['create_index']
	finally:
		curs.close()
	return dict((k, v) for k, v in section.iteritems() if v)

def dump_type(output, conn, book, section_type):
	curs = conn.cursor()
	makedirs(output, book, section_type)
	try:
		if section_type == 'animal_companion':
			find_section(curs, type=section_type, subtype='base')
		else:
			find_section(curs, type=section_type)
		for section in curs.fetchall():
			section = dump_section(conn, section)
			write_type_section(output, book, section)
	finally:
		curs.close()

def dump_types(output, conn, book):
	curs = conn.cursor()
	try:
		types = get_types(curs)
		for t in types:
			dump_type(output, conn, book, t)
	finally:
		curs.close()

def dump_rule(output, conn, book, section, path):
	newpath = []
	newpath.extend(path)
	if section.has_key("url") and section.has_key("name"):
		write_rule_section(output, book, section, path)
		newpath.append(section['name'])
	else:
		newpath.append("_")
	for s in section.get('sections', []):
		dump_rule(output, conn, book, s, newpath)

def dump_rules(output, conn, book):
	curs = conn.cursor()
	try:
		rules = get_rules(curs)
		for rule in rules:
			section = dump_section(conn, rule)
			dump_rule(output, conn, book, section, path=["rules"])
	finally:
		curs.close()

def dump_db(output, db, book):
	conn = get_db_connection(db, source=book)
	curs = conn.cursor()
	# Create files for interesting subtypes
	dump_types(output, conn, book)
	# Create files for rules
	dump_rules(output, conn, book)

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
	usage = "usage: %prog [options] [pfsrd url]\nDumps data from db out to data folder in json format."
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
	dump_db(options.output, options.db, options.book)

if __name__ == "__main__":
	sys.exit(main())


