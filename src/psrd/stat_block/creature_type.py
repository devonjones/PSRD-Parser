from psrd.stat_block.utils import colon_filter, default_closure
from psrd.universal import filter_name

def is_creature_type(sb, book):
	fields = dict(sb.keys)
	if len(fields.keys()) == 2:
		if fields.has_key('Traits') and fields.has_key('descriptor'):
			return True
	return False

def parse_creature_type(sb, book):
	section = {'type': 'section', 'subtype': 'creature_type', 'source': book, 'name': filter_name(sb.name.strip())}
	desc_text = ""
	trait_text = ""
	for key, value in sb.keys:
		if key == 'Traits':
			trait_text = trait_text + value
		else:
			desc_text = desc_text + value
	fields = dict(sb.keys)
	section['text'] = _list_text(desc_text)
	traits =  {'type': 'section', 'source': book, 'name': 'Traits'}
	traits['text'] = _list_text(trait_text)
	section['sections'] = [traits]
	return section

def _list_text(text):
	num = text.find(u'\u2022')
	newtext = text[0:num] + "<ul><li>" + text[num + 1:]
	newtext = newtext.replace(u'\u2022', "</li><li>") + "</li></ul>"
	return newtext
