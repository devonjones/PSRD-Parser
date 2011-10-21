import os
import json
from psrd.files import char_replace
from psrd.warnings import WarningReporting
from psrd.parse import get_subtitle

class Tables():
	def __init__(self):
		self.tables = []

	def __call__(self):
		return self

	def reset(self):
		self.tables = []

	def append(self, table):
		for t in self.tables:
			if t['name'] == table['name']:
				self.rename_table(table)
		self.tables.append(table)

	def rename_table(self, table):
		i = 0
		done = False
		while not done:
			i += 1
			clear = True
			for t in self.tables:
				if t['name'] == table['name'] + " (%s)" % i:
					clear = False
			if clear:
				done = True
		table['name'] = table['name'] + " (%s)" % i


Tables = Tables()

def print_tables():
	for table in Tables().tables:
		print table['title']

def get_full_context(tag, context):
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
		caption = caption.replace('Table: ', '').strip()
		final = []
		captions = caption.split(' ')
		for caption in captions:
			if caption not in context:
				if caption + "s" not in context:
					final.append(caption)
		if len(final) > 0:
			c = list(context)
			c.append(' '.join(final))
			return c
	c = list(context)
	if head != '':
		c.append(head)
	return c

def create_title(context):
	opctxt = []
	opctxt.extend(context)
	title = []
	if len(context) == 1:
		return "Table: %s" % (context[0])
	if len(context) == 2:
		return "Table: (%s) %s" % (context[0], context[1])
	if len(context) == 3:
		return "Table: (%s) %s: %s" % (context[0], context[1], context[2])
	if len(context) == 4:
		return "Table: (%s) %s [%s]: %s" % (context[0], context[1], context[2], context[3])
	if len(context) > 4:
		retstr = "Table: (%s) %s [%s]" % (context[0], context[1], context[2])
		end = ": %s" % context[-1]
		for c in context[3:-1]:
			retstr = retstr + " [%s]" % c
		return retstr + end

def parse_table(tag, context):
	ncontext = [cxt for cxt in context if cxt]
	if hasattr(tag, 'name') and tag.name == 'table':
		table_context = get_full_context(tag, ncontext)
		title = create_title(table_context)
		tb = {'name': title, 'context': table_context, 'text': unicode(tag), 'type': 'table'}
		Tables().append(tb)
		return tb

def parse_tables(tags, context):
	tables = []
	for tag in tags:
		if hasattr(tag, 'name') and tag.name == 'table':
			tables.append(parse_table(tag, context))
		else:
			if hasattr(tag, 'name'):
				alltables = tag.findAll('table')
				for table in alltables:
					tables.append(parse_table(table, context))
	return tables

def create_table_filename(output, book, table):
	title = char_replace(book) + "/tables/" + char_replace(table['name'])
	return os.path.abspath(output + "/" + title + ".json")

def write_tables(output, book):
	for table in Tables().tables:
		table['source'] = book
		filename = create_table_filename(output, book, table)
		fp = open(filename, 'w')
		json.dump(table, fp, indent=4)
		fp.close()
	Tables().reset()

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
	
