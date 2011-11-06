import sys
import re
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup, Tag, NavigableString
from psrd.parse import href_filter, br_filter, has_name
from psrd.tables2 import is_table, parse_table

class Heading():
	def __init__(self, level, name):
		self.level = level
		self.name = name
		self.details = []

	def __repr__(self):
		return "<Heading %s:%s>" % (self.level, self.name)

class StatBlockHeading(Heading):
	def __init__(self, name):
		self.name = name
		self.keys = []
		self.details = []

	def __repr__(self):
		return "<StatBlockHeading %s %s>" % (self.name, self.keys)

class StatBlockSection(StatBlockHeading):
	def __init__(self, name):
		self.name = name
		self.keys = []
		self.details = []

	def __repr__(self):
		return "<StatBlockSection %s %s>" % (self.name, self.keys)

def get_text(detail):
	return ''.join(detail.findAll(text=True))

def noop_pass(details):
	retdetails = []
	for detail in details:
		if not unicode(detail).strip() == "":
			retdetails.append(detail)
	return retdetails

def table_pass(details, book):
	retdetails = []
	for detail in details:
		if is_table(detail):
			retdetails.append(parse_table(detail, book))
		else:
			retdetails.append(detail)
	return retdetails

def title_pass(details):
	retdetails = []
	for detail in details:
		if has_name(detail, 'h1'):
			retdetails.append(Heading(1, get_text(detail)))
		elif has_name(detail, 'h2'):
			retdetails.append(Heading(2, get_text(detail)))
		else:
			retdetails.append(detail)
	return retdetails

def title_collapse_pass(details, level, add_statblocks=True):
	retdetails = []
	curr = None
	for detail in details:
		if detail.__class__ == Heading and detail.level <= level:
			curr = None
			retdetails.append(detail)
		else:
			if curr:
				if add_statblocks:
					curr.details.append(detail)
				else:
					if issubclass(detail.__class__, StatBlockHeading):
						retdetails.append(detail)
					else:
						curr.details.append(detail)
			else:
				retdetails.append(detail)
		if detail.__class__ == Heading and detail.level == level:
			curr = detail
	return retdetails

def subtitle_pass(details):
	retdetails = []
	for detail in details:
		if hasattr(detail, 'name'):
			if issubclass(detail.__class__, Heading):
				detail.details = subtitle_pass(detail.details)
				retdetails.append(detail)
			elif has_name(detail, 'h3'):
				retdetails.append(Heading(3, get_text(detail)))
			elif len(detail.contents) > 0:
				subdetail = detail.contents[0]
				if has_name(subdetail, 'b'):
					if not detail.get('align', '') == 'center':
						retdetails.append(Heading(4, get_text(subdetail)))
						subdetail.replaceWith('')
				elif has_name(subdetail, 'i'):
					retdetails.append(Heading(5, get_text(subdetail)))
					subdetail.replaceWith('')
				retdetails.append(detail)
			else:
				retdetails.append(detail)
		else:
			retdetails.append(detail)
	return retdetails

def stat_block_pass(details):
	retdetails = []
	for detail in details:
		if has_name(detail, 'p') and detail.get('class', "").find('stat-block-title') > -1:
			retdetails.append(StatBlockHeading(get_text(detail)))
		elif has_name(detail, 'h3') and detail.get('id', "").find('companion') > -1:
			retdetails.append(StatBlockHeading(get_text(detail)))
		else:
			retdetails.append(detail)
	return retdetails

def stat_block_collapse_pass(details):
	retdetails = []
	curr = None
	for detail in details:
		if issubclass(detail.__class__, Heading):
			if curr:
				stat_block_preparse(curr)
			curr = None
			retdetails.append(detail)
		else:
			if curr:
				curr.details.append(detail)
			else:
				retdetails.append(detail)
		if issubclass(detail.__class__, StatBlockHeading):
			curr = detail
	if curr:
		stat_block_preparse(curr)
	return retdetails

def stat_block_internals_first_pass(details):
	retdetails = []
	for detail in details:
		if has_name(detail, 'p') and detail.get('class', "") == 'stat-block-breaker':
			retdetails.append(StatBlockSection(get_text(detail)))
		else:
			retdetails.append(detail)
	return retdetails

def stat_block_key_first_pass(sb):
	retdetails = []
	key = None
	text = []
	top = True
	started = False
	for detail in sb.details:
		if has_name(detail, 'p') and detail.get('class', "").find('stat-block-1') > -1 and top:
			started = True
			key, text = stat_block_key_inner_parse(sb, detail, key, text)
		else:
			if started:
				top = False
			retdetails.append(detail)
	sb.details = retdetails
	if started:
		store_key(sb, key, text)
	else:
		stat_block_key_second_pass(sb)
	return sb

def stat_block_key_second_pass(sb):
	retdetails = []
	key = None
	text = []
	top = True
	started = False
	for detail in sb.details:
		if has_name(detail, 'p') and has_name(detail.contents[0], 'b') and top:
			started = True
			key, text = stat_block_key_inner_parse(sb, detail, key, text)
		else:
			if started:
				top = False
			retdetails.append(detail)
	sb.details = retdetails
	if started:
		store_key(sb, key, text)
	return sb

def stat_block_key_inner_parse(sb, detail, key, text):
	for element in detail.contents:
		if has_name(element, 'b'):
			if key:
				store_key(sb, key, text)
				text = []
			elif len(text) > 0:
				raise Exception("value with no key")
			key = ''.join(element.findAll(text=True))
		else:
			if hasattr(element, 'name'):
				text.append(''.join(element.findAll(text=True)))
			else:
				text.append(element)
	return key, text

def colon_pass(details):
	for detail in details:
		if detail.__class__ == Tag:
			colon_starter = detail.find(text=re.compile("^: .*"))
			if colon_starter:
				colon_starter.replaceWith(re.sub('^: ', '', unicode(colon_starter)))
		elif issubclass(detail.__class__, Heading):
			colon_pass(detail.details)

def store_key(sb, key, text):
	ptext = ''.join(text).strip()
	if ptext.endswith(';'):
		ptext = ptext[:-1]
	sb.keys.append((key.strip(), ptext.strip()))

def stat_block_preparse(sb):
	sb.details = stat_block_internals_first_pass(sb.details)
	sb.details = stat_block_collapse_pass(sb.details)
	stat_block_key_first_pass(sb)

def create_title_section(book, title):
	top = {'source': book, 'sections': [], 'type': 'section'}
	if title:
		top['name'] = title
	return top

def section_pass(struct, book):
	proclist = []
	if struct.__class__ == dict:
		for s in struct.get('sections', []):
			proclist.append(section_pass(s, book))
		struct['sections'] = proclist
	elif struct.__class__ == Heading:
		for d in struct.details:
			proclist.append(section_pass(d, book))
		oldstruct = struct
		struct = {'name': oldstruct.name, 'type': 'section', 'source': book, }
		if len(proclist) > 0:
			struct['sections'] = proclist
	return struct

# Adds text to sections
def section_text_pass(struct, book):
	text = []
	done = False
	newsections = []
	for item in struct.get('sections', []):
		if item.__class__ == Tag or item.__class__ == NavigableString:
			# Item is text, append it to the text list for attaching to an object
			text.append(unicode(item))
		elif item.__class__ in (str, unicode):
			text.append(item)
		else:
			if not done:
				# Only apply text to the current struct if we havn't hit an element of any other type
				done = True
				if len(text) > 0:
					struct['text'] = ''.join(text)
				text = []
			else:
				# Otherwise, add it to a new child section
				if len(text) > 0:
					newsections.append(section_text_pass({'type': 'section', 'source': book, 'sections': text}, book))
				text = []
			if item.__class__ == dict:
				# append any existing sections
				newsections.append(section_text_pass(item, book))
			elif issubclass(item.__class__, Heading):
				# This should only be statblocks
				newsections.append(item)
			else:
				# catchall
				raise Exception("Object is of unrecognized class %s.  Don't know how to proceed" % item.__class__)
	if len(text) > 0:
		if struct.has_key('text'):
			newsections.append(section_text_pass({'type': 'section', 'source': book, 'sections': text}, book))
		else:
			struct['text'] = ''.join(text)
	if len(newsections) > 0:
		struct['sections'] = newsections
	else:
		del struct['sections']
	return struct

def parse_body(div, book, title=False):
	lines = noop_pass(div.contents)
	lines = title_pass(lines)
	lines = table_pass(lines, book)
	lines = stat_block_pass(lines)
	lines = stat_block_collapse_pass(lines)
	lines = subtitle_pass(lines)
	lines = title_collapse_pass(lines, 5, add_statblocks=False)
	lines = title_collapse_pass(lines, 4, add_statblocks=False)
	lines = title_collapse_pass(lines, 3, add_statblocks=False)
	lines = title_collapse_pass(lines, 2)
	lines = title_collapse_pass(lines, 1)
	colon_pass(lines)
	top = lines[0]
	if len(lines) > 1:
		top = create_title_section(book, title)
		top['sections'] = lines
	top = section_pass(top, book)
	top = section_text_pass(top, book)
	return top

def parse_universal(filename, output, book, title=False):
	fp = open(filename)
	try:
		soup = BeautifulSoup(fp)
		href_filter(soup)
		br_filter(soup)
		divs = soup.findAll('div')
		for div in divs:
			if div.has_key('id') and div['id'] == 'body':
				div = __derender_divs(div)
				return parse_body(div, book, title)
	finally:
		fp.close()

def __derender_divs(div):
	if __has_div(div):
		text = ""
		for tag in div.contents:
			if has_name(tag, 'div'):
				text += tag.renderContents()
			elif hasattr(tag, 'name'):
				text += str(tag)
		div = BeautifulSoup(text)
		div = __derender_divs(div)
	return div

def __has_div(div):
	for tag in div.contents:
		if has_name(tag, 'div'):
			return True
	return False

def print_struct(top, level=0):
	if not top:
		return
	sys.stderr.write(''.join(["-" for i in range(0, level)]))
	if top.__class__ == dict:
		if top.has_key('name'):
			print "# " + top['name']
		else:
			print "# <Anonymous>"
		if top.has_key('sections'):
			for s in top['sections']:
				print_struct(s, level + 2)
	elif issubclass(top.__class__, Heading):
		print "* " + top.name
		for detail in top.details:
			print_struct(detail, level + 2)
	else:
		print "<text>"

