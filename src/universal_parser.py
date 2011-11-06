#!/usr/bin/env python
import sys
import os
import re
import json
from psrd.options import option_parser
from psrd.universal import parse_universal

def exec_main(parser):
	(options, args) = parser.parse_args()
	title = False
	if hasattr(options, 'title'):
		title = True

	if not options.output:
		sys.stderr.write("-o/--output required")
		sys.exit(1)
	if not os.path.exists(options.output):
		sys.stderr.write("-o/--output points to a directory that does not exist")
		sys.exit(1)
	if not os.path.isdir(options.output):
		sys.stderr.write("-o/--output points to a file, it must point to a directory")
		sys.exit(1)
	if not options.book:
		sys.stderr.write("-b/--book required")
		sys.exit(1)
	for arg in args:
		if title:
			parse_universal(arg, options.output, options.book, options.title)
		else:
			parse_universal(arg, options.output, options.book)

def main():
	usage = "usage: %prog [options] [filenames]\nParses spells from psrd html to json and writes them to the specified directory"
	parser = option_parser(usage, title=True)
	exec_main(parser)

def optionParser():
	parser = OptionParser(usage=usage)
	parser.add_option("-b", "--book", dest="book", help="Book spells are from (required)")
	parser.add_option("-o", "--output", dest="output", help="Output data directory.  Should be top level directory of psrd data. (required)")
	return parser

if __name__ == "__main__":
	sys.exit(main())

