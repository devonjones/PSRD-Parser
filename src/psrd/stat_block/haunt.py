from psrd.stat_block.utils import colon_filter, default_closure
from psrd.universal import filter_name

def is_haunt(sb, book):
	fields = dict(sb.keys)
	if fields.has_key('Destruction'):
		if fields.has_key('Notice'):
			return True
	return False

def parse_haunt(sb, book):
	section = {'type': 'haunt', 'source': book, 'name': filter_name(''.join(sb.html.pop(0).findAll(text=True)))}
	section['body'] = ''.join([unicode(elem) for elem in sb.html])
	return section

