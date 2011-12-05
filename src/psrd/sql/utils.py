
def test_args(args):
	for key in args.keys():
		if key not in ['sections', 'name', 'source', 'type', 'subtype']:
			raise Exception("Unknown key for insert: %s" % key)
