#import pprint
from BeautifulSoup import BeautifulSoup
from psrd.table.general import add_additional_fields, fix_cost, set_subtype, clear_nbsp

def set_damage(weapon):
	damage = {
		"see text": ('see text', 'see text'),
		"special": ('special', 'special'),
		"Special": ('Special', 'Special'),
		"1d2": ('&mdash;', '1d3'),
		"1d3": ('1', '1d4'),
		"1d4": ('1d2', '1d6'),
		"1d6": ('1d3', '1d8'),
		"1d8": ('1d4', '2d6'),
		"1d10": ('1d6', '2d8'),
		"1d12": ('1d10', '3d6'),

		"2d4": ('1d6', '2d6'),
		"2d6": ('1d8', '3d6'),
		"2d8": ('1d6', '3d8'),
		"2d10": ('2d8', '4d8'),
		"2d12": ('2d10', '6d6'),

		"3d6": ('2d6', '4d6'),
		"3d8": ('2d8', '4d8'),

		"4d6": ('3d6', '6d6'),
		"4d8": ('3d8', '6d8'),

		"6d6": ('4d6', '8d6'),
		"6d8": ('4d8', '8d8'),

		"8d6": ('6d6', '12d6'),
		"8d8": ('6d8', '12d8'),
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
				subsection = "Weapon"
				value = weapon[key]
				if weapon['Name'] in table_data.get('distinct_section', {}):
					subsection = table_data['distinct_section'][weapon['Name']]
				misc.append({
					"field": key,
					"subsection": subsection,
					"value": value})
		weapon['item'] = item
		set_subtype(table_data, "Weapon Class", weapon)
	#pp = pprint.PrettyPrinter(indent=4)
	#pp.pprint(weapons)
	return weapons

def parse_weapon_table(table, table_data):
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
						weapon[fields[i]] = clear_nbsp(
							line.contents[i].getText())
					elif fields[i] in ('Cost', 'Weight'):
						weapon[fields[i]] = line.contents[i].getText()
				add_additional_fields(table_data, weapon)
				weapons.append(weapon)
	return process_weapons(table_data, weapons)

def parse_weapon_header(line):
	for sup in line.findAll('sup'):
		sup.extract()
	fields = [td.getText() for td in line.contents]
	fields.pop(0)
	fields.insert(0, 'Name')
	return fields

