
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

	def __call__(self):
		return self

	def add_function(self, test, function):
		self.functions.append((test, function))

StatBlockFunctions = StatBlockFunctions()

def parse_stat_block(sb, book):
	for test, function in StatBlockFunctions().functions:
		if test(sb, book):
			return function(sb, book)
	print sb
	print sb.html
	return sb
