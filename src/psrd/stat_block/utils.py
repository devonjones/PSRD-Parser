from psrd.universal import title_collapse_pass, section_pass, Heading

def colon_filter(value):
	if value.startswith(":"):
		value = value[1:]
	return value.strip()

def comma_filter(value):
	if value.endswith(","):
		value = value[:-1]
	return value.strip()

def default_closure(field):
	def fxn(sb, value):
		value = colon_filter(value)
		value = comma_filter(value)
		value = value.replace('&ndash;', '-')
		value = value.replace('&mdash;', '-')
		sb[field] = value
	return fxn

def noop(creature, value):
	print value

class StatBlockFunctions():
	def __init__(self):
		self.functions = []
		self.default = None

	def __call__(self):
		return self

	def add_function(self, test, function):
		self.functions.append((test, function))

	def add_default(self, function):
		self.default = function

StatBlockFunctions = StatBlockFunctions()

def parse_stat_block(sb, book, no_sb=False):
	if no_sb:
		return StatBlockFunctions.default(sb, book, no_sb=no_sb)
	for test, function in StatBlockFunctions().functions:
		if test(sb, book):
			return function(sb, book)
	return sb

def collapse_text(item, lines):
	textbuf = []
	sectionbuf = []
	text = True
	for line in lines:
		if not isinstance(line, str) and not isinstance(line, unicode):
			text = False
		if text:
			textbuf.append(line)
		else:
			if isinstance(line, str) or isinstance(line, unicode):
				sectionbuf.append({'type': 'section', 'source': item['source'], 'text': line})
			else:
				sectionbuf.append(line)
	item['text'] = ''.join(textbuf)
	if len(sectionbuf) > 0:
		sections = item.setdefault('sections', [])
		sections.extend(sectionbuf)
		level = has_heading(sections)
		while level:
			sections = title_collapse_pass(sections, level)
			level = level - 1
		if level == 0:
			sections = sections_pass(sections, item['source'])
		item['sections'] = sections

def sections_pass(sections, book):
	retsects = []
	for section in sections:
		if isinstance(section, Heading):
			retsects.append(section_pass(section, book))
		else:
			retsects.append(section)
	return retsects

def has_heading(sections):
	level = None
	for section in sections:
		if isinstance(section, Heading):
			if not level or level < section.level:
				level = section.level
	return level
