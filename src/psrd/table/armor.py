#import pprint
from BeautifulSoup import BeautifulSoup
from psrd.table.general import add_additional_fields, set_subtype, clear_nbsp


def process_armor(table_data, armor_list):
	remap = {"Cost": "price", "Weight": "weight", "Name": "name"}
	for armor in armor_list:
		item = {"type": "item"}
		fields = armor.keys()
		fields.sort()
		for key in fields:
			if key in remap.keys():
				item[remap[key]] = armor[key]
			else:
				misc = item.setdefault('misc', [])
				value = armor[key]
				if key == u'Armor/Shield Bonus':
					if armor['Armor Type'] == u'Shields':
						key = 'Shield Bonus'
					else:
						key = 'Armor Bonus'
				misc.append({
					"field": key,
					"subsection": "Armor",
					"value": value})
		armor['item'] = item
		set_subtype(table_data, "Armor Type", armor)
	#pp = pprint.PrettyPrinter(indent=4)
	#pp.pprint(armor_list)
	return armor_list

def parse_armor_table(table, table_data):
	soup = BeautifulSoup(table['body'])
	fields = parse_armor_header(soup.table.thead.tr)
	armor_list = []
	armor_type = ""
	for line in soup.table.contents:
		if line.name == 'thead':
			armor_type = line.tr.contents[0].getText().strip()
		elif line.name == 'tr':
			if len(line.contents) == 1:
				armor_type = line.getText().strip()
			else:
				armor = {'Armor Type': armor_type}
				for i in range(len(line.contents)):
					armor[fields[i]] = clear_nbsp(line.contents[i].getText())
				add_additional_fields(table_data, armor)
				armor_list.append(armor)
	return process_armor(table_data, armor_list)

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

