#!/usr/bin/env python
import sys
import os
from optparse import OptionParser
from psrd.sql.index import get_db_connection
from psrd.sql.index.central_index import find_central_index
from psrd.sql.index.spell_component_index import fetch_spell_component_index
from psrd.sql.index.spell_subschool_index import fetch_spell_subschool_index
from psrd.sql.index.spell_list_index import fetch_spell_list_index
from psrd.sql.index.spell_descriptor_index import fetch_spell_descriptor_index
from psrd.parse.creds import register
import parse_rest.datatypes
from parse_rest.connection import ParseBatcher

class Spell(parse_rest.datatypes.Object):
	pass

def get_parse_spell(url):
	register()
	all_spells = Spell.Query.all().filter(url=url)
	for spell in all_spells:
		return spell

def load_spell_data(db):
	conn = get_db_connection(db)
	curs = conn.cursor()
	find_central_index(curs, **{"type": "spell"})
	index_lines = curs.fetchall()
	batch = []
	batcher = ParseBatcher()
	count = 0
	for line in index_lines:
		spell = get_parse_spell(line['url'])
		if spell:
			batch.append(make_spell(conn, line, spell))
		else:
			batch.append(make_spell(conn, line))
		if len(batch) >= 50:
			batcher.batch_save(batch)
			batch = []
			count += 50
			print "Saving through %s" % count

def make_spell(conn, line, spell=None):
	if not spell:
		spell = Spell()
	spell.source = line["source"]
	spell.subtype = line["subtype"]
	spell.name = line["name"]
	spell.url = line["url"]
	spell.school = line["spell_school"]
	spell.components = line["spell_component_text"]
	add_subschool(conn, spell, line["index_id"])
	add_descriptor(conn, spell, line["index_id"])
	add_levels(conn, spell, line["index_id"])
	return spell

def add_subschool(conn, spell, index_id):
	curs = conn.cursor()
	try:
		fetch_spell_subschool_index(curs, index_id)
		subschools = curs.fetchall()
		slist = []
		for subschool in subschools:
			slist.append(subschool["subschool"])
		if len(slist) > 0:
			spell.subschools = slist
	finally:
		curs.close()

def add_levels(conn, spell, index_id):
	curs = conn.cursor()
	try:
		fetch_spell_list_index(curs, index_id)
		levels = curs.fetchall()
		llist = []
		for level in levels:
			llist.append({"level": level["level"], "class": level["class"]})
		if len(llist) > 0:
			spell.levels = llist
	finally:
		curs.close()

def add_descriptor(conn, spell, index_id):
	curs = conn.cursor()
	try:
		fetch_spell_descriptor_index(curs, index_id)
		descriptors = curs.fetchall()
		dlist = []
		for descriptor in descriptors:
			dlist.append(descriptor["descriptor"])
		if len(dlist) > 0:
			spell.descriptors = dlist
	finally:
		curs.close()

def option_parser(usage, title=False):
	parser = OptionParser(usage=usage)
	parser.add_option("-d", "--db", dest="db", help="Sqlite DB to load into (required)")
	return parser

def main():
	usage = "usage: %prog [options]\nLoads spell data into parse."
	parser = option_parser(usage)
	(options, args) = parser.parse_args()
	if not options.db:
		sys.stderr.write("-d/--db required\n")
		sys.exit(1)
	load_spell_data(options.db)

if __name__ == "__main__":
	sys.exit(main())

