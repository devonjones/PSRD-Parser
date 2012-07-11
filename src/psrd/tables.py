def get_title(tag):
	captions = tag.findAll('caption')
	caption = ""
	if len(captions) > 0:
		texts = captions[0].findAll(text=True)
		caption = texts.pop(0).strip()
	heads = tag.findAll('thead')
	head = ""
	if len(heads) > 0:
		texts = heads[0].findAll(text=True)
		head = texts.pop(0).strip()
	if caption.strip() != '':
		captions = caption.split(' ')
		final = filter(lambda x: x != '', captions)
		return ' '.join(final)
	return head

def parse_table(tag, book):
	if hasattr(tag, 'name') and tag.name == 'table':
		title = get_title(tag)
		tb = {'name': title, 'text': unicode(tag), 'type': 'table', 'source': book}
		return tb

def has_table(details):
	for detail in details:
		if hasattr(detail, 'name'):
			if is_table(detail):
				return True
	return False

def is_table(detail):
	if hasattr(detail, 'name'):
		if detail.name == 'table':
			return True
		elif detail.name == 'div' and detail.findAll(text=False)[0].name == 'table':
			return True
	return False
	
