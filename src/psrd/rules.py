import os
import json
from BeautifulSoup import BeautifulSoup
from psrd.files import char_replace
from psrd.warnings import WarningReporting
from psrd.parse import construct_line, get_subtitle, href_filter, has_name
from psrd.sections import store_section, set_section_text, filter_sections, print_struct

def parse_simple_rules(book, details, name):
	retarr = []
	if len(details) == 0:
		return None
	section = {'name': name, 'type': 'section', 'source': book}
	set_section_text(section, [name], details)
	return section

def create_title_section(title, book):
	return {'name': title, 'source': book, 'sections': [], 'type': 'section'}

def parse_body(div, book, title):
	top = create_title_section(title, book)
	store_section(top, [title], div.contents)
	filter_sections(top)
	if len(top['sections']) == 1 and top['sections'][0].has_key('name') and top['name'] == top['sections'][0]['name']:
		return top['sections'][0]
	return top

def parse_rules(filename, output, book, title):
	WarningReporting().book = book
	fp = open(filename)
	try:
		soup = BeautifulSoup(fp)
		href_filter(soup)
		divs = soup.findAll('div')
		for div in divs:
			if div.has_key('id') and div['id'] == 'body':
				if len(div.findAll('div')) > 0:
					text = ""
					for tag in div.contents:
						if has_name(tag, 'div'):
							text += tag.renderContents()
						elif hasattr(tag, 'name'):
							text += str(tag)
					div = BeautifulSoup(text)
				rules = parse_body(div, book, title)
				print_struct(rules)
				write_rules(output, rules, book, char_replace(title))
	finally:
		fp.close()

def write_rules(output, rules, book, filename):
	filename = create_rules_filename(output, book, filename)
	fp = open(filename, 'w')
	json.dump(rules, fp, indent=4)
	fp.close()

def create_rules_filename(output, book, filename):
	title = char_replace(book) + "/rules/" + filename
	return os.path.abspath(output + "/" + title + ".json")
