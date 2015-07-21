
def filter_fields(fields, section):
	retdict = {}
	for f in fields:
		if f in section.keys():
			retdict[f] = section[f]
	return retdict

def filter_section_fields(section):
	fields = [
		"type",
		"subtype",
		"name",
		"abbrev",
		"source",
		"description",
		"body",
		"image",
		"alt",
		"create_index"
	]
	return filter_fields(fields, section)

def filter_item_details_fields(section):
	fields = [
		"aura",
		"slot",
		"cl",
		"price",
		"weight"
	]
	return filter_fields(fields, section)


