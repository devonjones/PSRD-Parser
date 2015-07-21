
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
		reduce_misc(delta)
		output.append(delta)
	return output

def merge_misc(delta, misc):
	delta_misc = delta.setdefault('misc', [])
	for value in misc:
		if not value in delta_misc:
			delta_misc.append(value)

def reduce_misc(item):
	misc_list = item.get('misc', [])
	rewrite = {}
	for misc in misc_list:
		if misc.has_key('subsection'):
			subsection = rewrite.setdefault(misc['subsection'], {})
		else:
			subsection = rewrite.setdefault('default', {})
		subsection[misc['field']] = misc['value']
	if len(rewrite) == 1:
		return
	if rewrite.has_key('default') and len(rewrite) < 3:
		return
	move = []
	for key in rewrite.keys():
		if key != 'default':
			for field in rewrite[key].keys():
				if in_all(rewrite, field, rewrite[key][field]):
					move.append((field, rewrite[key][field]))
			break
	if len(move) == 0:
		return
	for (field, value) in move:
		default = rewrite.setdefault('default', {})
		default[field] = value
		for key in rewrite.keys():
			if key != 'default':
				del rewrite[key][field]
	rebuild = []
	default = rewrite.get('default', {})
	add_fields(rebuild, default)
	keys = rewrite.keys()
	keys.sort()
	for key in keys:
		if key != 'default':
			fields = rewrite[key]
			add_fields(rebuild, fields, key)
	item['misc'] = rebuild

def add_fields(rebuild, fields, subsection=None):
	keys = fields.keys()
	keys.sort()
	for key in keys:
		if subsection:
			rebuild.append({
				"field": key,
				"subsection": subsection,
				"value": fields[key]})
		else:
			rebuild.append({
				"field": key,
				"value": fields[key]})

def in_all(rewrite, field, value):
	for key in rewrite:
		if key != 'default':
			if rewrite[key].has_key(field):
				if rewrite[key][field] != value:
					return False
			else:
				return False
	return True
