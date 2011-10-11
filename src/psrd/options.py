import sys
import os
from optparse import OptionParser
from psrd.files import makedirs

def exec_main(parser, function, localdir):
	(options, args) = parser.parse_args()

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
	makedirs(options.output, options.book, localdir)
	for arg in args:
		function(arg, options.output, options.book)

def option_parser(usage):
	parser = OptionParser(usage=usage)
	parser.add_option("-b", "--book", dest="book", help="Book races are from (required)")
	parser.add_option("-o", "--output", dest="output", help="Output data directory.  Should be top level directory of psrd data. (required)")
	return parser
