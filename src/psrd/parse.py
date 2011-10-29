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
	if len(line) == 0:
		return None
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
	if len(line) == 0:
		return None
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

def has_name(tag, name):
	if hasattr(tag, 'name') and tag.name == name:
		return True
	return False

def has_first_child(tag, name):
	if has_name(tag, name):
		return True
	elif hasattr(tag, 'name') and len(tag.contents) > 0:
		if has_name(tag.contents[0], name):
			return True
	return False

def get_first_child_text(tag, name):
	if has_name(tag, name):
		return ''.join(tag.findAll(text=True))
	elif hasattr(tag, 'name') and len(tag.contents) > 0:
		if has_name(tag.contents[0], name):
			return ''.join(tag.contents[0].findAll(text=True))

def href_filter(soup):
	hrefs = soup.findAll('a')
	for href in hrefs:
		href.replaceWith(href.renderContents())

