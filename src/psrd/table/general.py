import re

def clear_nbsp(field):
	while field.startswith('&nbsp;'):
		field = field[6:]
	return field

def fix_cost(item):
	if item.has_key('Name'):
		matches = re.search(r' \((.*)\)', item['Name'])
		if matches:
			if item.has_key('Cost'):
				if not matches.group(1) in ("combat trained",  "empty"):
					item['Cost'] = "%s/%s" %(
							item['Cost'], matches.group(1))
			if not matches.group(1) in ("combat trained"):
				parts = item['Name'].split('(')
				item['Name'] = parts[0].strip()
				if parts[1].find(",") > -1:
					item['Name'] = "%s,%s" % (
							item["Name"], parts[1].split(",")[1])

def add_additional_fields(table_data, item):
	fields = table_data.get('additional_fields', {})
	if item['Name'] in fields.keys():
		item.update(fields[item['Name']])

def set_subtype(table_data, title, item):
	if table_data.has_key('default_subtype'):
		item['item']['subtype'] = table_data['default_subtype']
		title_alternates = table_data.get('title_alternate_subtypes', {})
		if item[title] in title_alternates:
			item['item']['subtype'] = title_alternates[item[title]]
		alternates = table_data.setdefault('alternate_subtypes', {})
		if item['Name'] in alternates:
			item['item']['subtype'] = alternates[item['Name']]

