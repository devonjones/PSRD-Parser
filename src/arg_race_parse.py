#!/usr/bin/env python
import sys
import os
import re
import json
from BeautifulSoup import BeautifulSoup
from psrd.races import parse_arg_core_race, parse_arg_featured_race, parse_arg_uncommon_race
from psrd.warnings import WarningReporting
from psrd.options import exec_main, option_parser

def main():
	usage = "usage: %prog [options] [filenames]\nParses races from psrd html to json and writes them to the specified directory"
	parser = option_parser(usage)
	parser.add_option("-t", "--type", dest="type", help="Race type")
	(options, args) = parser.parse_args()
	fxn = parse_arg_core_race
	if options.type == 'core':
		fxn = parse_arg_core_race
	elif options.type == 'featured':
		fxn = parse_arg_featured_race
	elif options.type == 'uncommon':
		fxn = parse_arg_uncommon_race
	exec_main(parser, fxn, "races")

if __name__ == "__main__":
	sys.exit(main())
