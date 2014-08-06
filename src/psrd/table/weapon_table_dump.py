#!/usr/bin/env python
import sys
import re
import os.path
import json
from optparse import OptionParser
from BeautifulSoup import BeautifulSoup
from psrd.sql import get_db_connection, find_section
from psrd.files import char_replace

def generate_extension_file_name(output_dir, book):
	return os.path.join(
			os.path.abspath(output_dir), char_replace(book), 'extension.json')

def generate_extension_output_file_name(output_dir, book):
	return os.path.join(
		os.path.abspath(output_dir),
		char_replace(book),
		'extensions',
		'items.json')

def load_extension_file(output_dir, book):
	filename = generate_extension_file_name(output_dir, book)
	with open(filename) as jsonfile:
		return json.load(jsonfile)

def write_output(output_dir, book, output):
	filename = generate_extension_output_file_name(output_dir, book)
	if not os.path.exists(os.path.dirname(filename)):
		os.makedirs(os.path.dirname(filename))
	with open(filename, 'w') as jsonfile:
		json.dump(output, jsonfile)

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

# Weapons

def set_damage(weapon):
	damage = {
		"1d2": ('&mdash;', '1d3'),
		"1d3": ('1', '1d4'),
		"1d4": ('1d2', '1d6'),
		"1d6": ('1d3', '1d8'),
		"1d8": ('1d4', '2d6'),
		"1d10": ('1d6', '2d8'),
		"1d12": ('1d8', '3d6'),
		"2d4": ('1d4', '2d6'),
		"2d6": ('1d8', '3d6'),
		"2d8": ('1d10', '3d8'),
		"2d10": ('2d6', '4d8')
	}
	if weapon.has_key(u"Dmg (M)"):
		medium = weapon[u"Dmg (M)"]
		parts = medium.split('/')
		tiny = []
		large = []
		for part in parts:
			dmg = damage[part]
			tiny.append(dmg[0])
			large.append(dmg[1])
		weapon["Dmg (T)"] = '/'.join(tiny)
		weapon["Dmg (L)"] = '/'.join(large)

def fix_cost(weapon):
	if weapon.has_key('Name'):
		matches = re.search(r' \((.*)\)', weapon['Name'])
		if matches:
			if weapon.has_key('Cost'):
				if not matches.group(1) in ("combat trained",  "empty"):
					weapon['Cost'] = "%s/%s" %(
							weapon['Cost'], matches.group(1))
			if not matches.group(1) in ("combat trained"):
				parts = weapon['Name'].split('(')
				weapon['Name'] = parts[0].strip()
				if parts[1].find(",") > -1:
					weapon['Name'] = "%s,%s" % (
							weapon["Name"], parts[1].split(",")[1])

def process_weapons(table_data, weapons):
	remap = {"Cost": "price", "Weight": "weight", "Name": "name"}
	for weapon in weapons:
		item = {"type": "item"}
		set_damage(weapon)
		fix_cost(weapon)
		fields = weapon.keys()
		fields.sort()
		for key in fields:
			if key in remap.keys():
				item[remap[key]] = weapon[key]
			else:
				misc = item.setdefault('misc', [])
				misc.append({
					"field": key,
					"subsection": "Weapon",
					"value": weapon[key]})
		weapon['item'] = item
		set_subtype(table_data, "Weapon Class", weapon)
	return weapons

def parse_weapon_table(table, table_data, url):
	soup = BeautifulSoup(table['body'])
	fields = parse_weapon_header(soup.table.thead.tr)
	category = None
	weapon_class = None
	weapons = []
	for line in soup.table.contents:
		if line.name == 'thead':
			category = line.tr.contents[0].getText()
		elif line.name == 'tr':
			if len(line.contents) == 1:
				weapon_class = line.getText()
			else:
				weapon = {'Proficiency':category, 'Weapon Class': weapon_class}
				for i in range(len(line.contents)):
					data = line.contents[i].getText()
					if data != '&mdash;':
						weapon[fields[i]] = line.contents[i].getText()
					elif fields[i] in ('Cost', 'Weight'):
						weapon[fields[i]] = line.contents[i].getText()
				weapons.append(weapon)
	return process_weapons(table_data, weapons)

def parse_weapon_header(line):
	for sup in line.findAll('sup'):
		sup.extract()
	fields = [td.getText() for td in line.contents]
	fields.pop(0)
	fields.insert(0, 'Name')
	return fields

# Armor

def process_armor(table_data, armor):
	remap = {"Cost": "price", "Weight": "weight", "Name": "name"}
	for a in armor:
		item = {"type": "item"}
		fields = a.keys()
		fields.sort()
		for key in fields:
			if key in remap.keys():
				item[remap[key]] = a[key]
			else:
				misc = item.setdefault('misc', [])
				value = a[key]
				if key == u'Armor/Shield Bonus':
					if a['Armor Type'] == u'Shields':
						key = 'Shield Bonus'
					else:
						key = 'Armor Bonus'
				misc.append({
					"field": key,
					"subsection": "Armor",
					"value": value})
		a['item'] = item
		set_subtype(table_data, "Armor Type", a)
	return armor

def parse_armor_table(table, table_data, url):
	soup = BeautifulSoup(table['body'])
	fields = parse_armor_header(soup.table.thead.tr)
	armor = []
	armor_type = ""
	for line in soup.table.contents:
		if line.name == 'thead':
			armor_type = line.tr.contents[0].getText().strip()
		elif line.name == 'tr':
			if len(line.contents) == 1:
				armor_type = line.getText().strip()
			else:
				a = {'Armor Type': armor_type}
				for i in range(len(line.contents)):
					data = line.contents[i].getText()
					a[fields[i]] = line.contents[i].getText()
				armor.append(a)
	return process_armor(table_data, armor)

def parse_armor_header(line):
	for sup in line.findAll('sup'):
		sup.extract()
	fields = [td.getText() for td in line.contents]
	fields.pop(0)
	fields.insert(0, 'Name')
	weight = fields.pop()
	fields.pop()
	fields.append("Speed (30 ft.)")
	fields.append("Speed (20 ft.)")
	fields.append(weight)
	return fields

# Gear

def add_additional_fields(table_data, item):
	fields = table_data.get('additional_fields', {})
	if item['Name'] in fields.keys():
		item.update(fields[item['Name']])

def process_gear(table_data, gear):
	remap = {"Cost": "price", "Weight": "weight", "Name": "name", "Aura": "aura"}
	for a in gear:
		item = {"type": "item"}
		fix_cost(a)
		fields = a.keys()
		fields.sort()
		for key in fields:
			misc = item.setdefault('misc', [])
			if a['Name'] in table_data.get('distinct_section', {}):
				value = a[key]
				subsection = table_data['distinct_section'][a['Name']]
				if key == "Cost":
					key = "Price"
				if not key == "Name":
					misc.append({
						"field": key,
						"subsection": subsection,
						"value": value})
			else:
				if key in remap.keys():
					item[remap[key]] = a[key]
				else:
					value = a[key]
					misc.append({
						"field": key,
						"value": value})
		a['item'] = item
		set_subtype(table_data, 'Gear Type', a)
	return gear

def parse_gear_table(table, table_data, url):
	soup = BeautifulSoup(table['body'])
	gear = []
	gear_type = ""
	modifier = None
	for line in soup.table.contents:
		if line.name == 'thead':
			gear_type, fields = parse_gear_header(line)
		elif line.name == 'tr':
			if len(line.contents) == 1:
				modifier = line.getText().strip()
			else:
				item = {'Gear Type': gear_type}
				if modifier and not line.td.has_key('class'):
					modifier = None
				for i in range(len(line.contents)):
					data = line.contents[i].getText()
					item[fields[i]] = line.contents[i].getText()
				if modifier and not item['Name'].startswith(modifier):
					item['Name'] = "%s, %s" % (modifier, item['Name'])
				add_additional_fields(table_data, item)
				gear.append(item)
	return process_gear(table_data, gear)

def parse_gear_header(line):
	for sup in line.findAll('sup'):
		sup.extract()
	gear_type = line.contents[0].getText()
	fields = [td.getText() for td in line.contents[1]]
	fields.pop(0)
	fields.insert(0, 'Name')
	return gear_type, fields

# General

def set_subtype(table_data, title, item):
	if table_data.has_key('default_subtype'):
		item['item']['subtype'] = table_data['default_subtype']
		title_alternates = table_data.get('title_alternate_subtypes', {})
		if item[title] in title_alternates:
			item['item']['subtype'] = title_alternates[item[title]]
		alternates = table_data.setdefault('alternate_subtypes', {})
		if item['Name'] in alternates:
			item['item']['subtype'] = alternates[item['Name']]

def get_parser(parser_name):
	parsers = {
		'weapons': parse_weapon_table,
		'armor': parse_armor_table,
		'gear': parse_gear_table,
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
		items = parser(table, table_data, url)
		finished = []
		for item in items:
			update_sections(curs, section_cache, table_data, table, item)
	urls = section_cache.keys()
	urls.sort()
	output = produce_output([section_cache[url] for url in urls])
	write_output(output_dir, book, output)

def produce_output(sections):
	output = []
	for section in sections:
		print section['section']['url']
		delta = {'url': section['section']['url']}
		changes = section['changes']
		for change in changes:
			item = change['item']
			if item.has_key('price'):
				delta['price'] = item['price']
			if item.has_key('weight'):
				delta['weight'] = item['weight']
			if item.has_key('misc'):
				misc = item['misc']
				merge_misc(delta, misc)
		output.append(delta)
	return output

def merge_misc(delta, misc):
	delta_misc = delta.setdefault('misc', [])
	for value in misc:
		if not value in delta_misc:
			delta_misc.append(value)

def option_parser(usage, title=False):
	parser = OptionParser(usage=usage)
	parser.add_option(
			"-o", "--output", dest="output",
			help="Output data directory.  Should be top level directory of psrd data. (required)")
	parser.add_option(
			"-d", "--db", dest="db", help="Sqlite DB to load into (required)")
	parser.add_option(
			"-b", "--book", dest="book", help="Book races are from (required)")
	return parser

def main():
	usage = "usage: %prog [options] [pfsrd url]\nDumps weapon information from tables."
	parser = option_parser(usage)
	(options, args) = parser.parse_args()
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

