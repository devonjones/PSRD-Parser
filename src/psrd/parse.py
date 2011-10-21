def store_section(parent, name, details):
	if not name:
		name = 'description'
	if name == 'description':
		parent[name] = construct_stripped_line(details)
	else:
		name = construct_stripped_line(name)
		sections = parent.setdefault('sections', [])
		section = {'name': name, 'text': construct_line(details)}
		sections.append(section)

def construct_stripped_line(contents, strip_start_colon=True, strip_end_colon=True):
	if len(contents) == 0:
		return None
	output = []
	for content in contents:
		if hasattr(content, 'name'):
			output.extend(content.findAll(text=True))
		else:
			output.append(content)
	line = ''.join(output).strip()
	if line[0] == ':' and strip_start_colon:
		line = line[1:]
	if line.endswith(':') and strip_end_colon:
		line = line[:-1]
	return line.strip()

def construct_line(contents, strip_start_colon=True, strip_end_colon=True):
	if len(contents) == 0:
		return None
	output = []
	for content in contents:
		output.append(unicode(content))
	line = ''.join(output).strip()
	if line[0] == ':' and strip_start_colon:
		line = line[1:]
	if line.endswith(':') and strip_end_colon:
		line = line[:-1]
	return line.strip()

def get_subtitle(tag):
	if hasattr(tag, 'contents') and len(tag.contents) > 1:
		for content in tag.contents:
			if content.string and len(content.string.strip()) > 0:
				return content.string.strip()
	elif tag.string:
		return tag.string.strip()
	elif len(tag.contents) == 0:
		return None
	else:
		return get_subtitle(tag.contents[0]).strip()

