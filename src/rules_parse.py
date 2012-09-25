#!/usr/bin/env python
import sys
import os
import re
import json
from psrd.rules import parse_rules, parse_rules_no_sb
from psrd.universal import parse_universal
from psrd.options import exec_main, option_parser

def main():
	usage = "usage: %prog [options] [filenames]\nParses files from psrd html to json and writes them to the specified directory"
	parser = option_parser(usage, title=True)
	parser.add_option("-n", "--no-statblocks", dest="no_statblocks", default=False, action="store_true", help="Don't parse statblocks")
	(options, args) = parser.parse_args()
	fxn = parse_rules
	if options.no_statblocks:
		fxn = parse_rules_no_sb
	exec_main(parser, fxn, "rules")

if __name__ == "__main__":
	sys.exit(main())
