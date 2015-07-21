from BeautifulSoup import BeautifulSoup
from psrd.extensions.table.general import add_additional_fields, fix_cost, set_subtype, clear_nbsp

def process_gear(table_data, gear_list):
	remap = {
			"Cost": "price",
			"Weight": "weight",
			"Name": "name",
			"Aura": "aura"}
	for gear in gear_list:
		item = {"type": "item"}
		fix_cost(gear)
		fields = gear.keys()
		fields.sort()
		for key in fields:
			misc = item.setdefault('misc', [])
			if gear['Name'] in table_data.get('distinct_section', {}):
				value = gear[key]
				subsection = table_data['distinct_section'][gear['Name']]
				if key == "Cost":
					key = "Price"
				if not key == "Name":
					misc.append({
						"field": key,
						"subsection": subsection,
						"value": value})
			else:
				if key in remap.keys():
					item[remap[key]] = gear[key]
				else:
					value = gear[key]
					misc.append({
						"field": key,
						"value": value})
		gear['item'] = item
		set_subtype(table_data, 'Gear Type', gear)
	return gear_list

def default_modifier_clear(modifier, line):
	if modifier and not line.td.has_key('class'):
		return True
	return False

def siege_engine_modifier_clear(modifier, line):
	return False

def parse_gear_table_closure(header_function, modifier_clear_function=default_modifier_clear):
	def parse_gear_table(table, table_data):
		soup = BeautifulSoup(table['body'])
		gear = []
		gear_type = ""
		modifier = None
		for line in soup.table.contents:
			if line.name == 'thead':
				gear_type, fields = header_function(line)
			elif line.name == 'tr':
				if len(line.contents) == 1:
					modifier = line.getText().strip()
				else:
					item = {'Gear Type': gear_type}
					if modifier_clear_function(modifier, line):
						modifier = None
					for i in range(len(line.contents)):
						item[fields[i]] = clear_nbsp(line.contents[i].getText())
					if modifier and not item['Name'].startswith(modifier):
						item['Name'] = "%s, %s" % (modifier, item['Name'])
					add_additional_fields(table_data, item)
					gear.append(item)
		return process_gear(table_data, gear)
	return parse_gear_table

def parse_gear_header(line):
	for sup in line.findAll('sup'):
		sup.extract()
	gear_type = line.contents[0].getText()
	fields = [td.getText() for td in line.contents[1]]
	fields.pop(0)
	fields.insert(0, 'Name')
	return gear_type, fields

def parse_gear_header2(line):
	for sup in line.findAll('sup'):
		sup.extract()
	fields = [td.getText() for td in line.contents[0]]
	gear_type = fields.pop(0)
	fields.insert(0, 'Name')
	return gear_type, fields

