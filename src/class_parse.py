#!/usr/bin/env python
import sys
import os
import re
import json
from BeautifulSoup import BeautifulSoup
from psrd.classes import parse_core_classes, parse_npc_classes, parse_base_classes, parse_prestige_classes
from psrd.warnings import WarningReporting
from psrd.options import exec_main, option_parser

def main():
	usage = "usage: %prog [options] [filenames]\nParses core classes from psrd html to json and writes them to the specified directory"
	parser = option_parser(usage)
	parser.add_option("-c", "--class_type", dest="class_type", help="Type of class (core, base, prestige, npc (default core)")
	(options, args) = parser.parse_args()
	fxn = parse_core_classes
	if options.class_type == 'base':
		fxn = parse_base_classes
	elif options.class_type == 'prestige':
		fxn = parse_prestige_classes
	elif options.class_type == 'npc':
		fxn = parse_npc_classes
	elif options.class_type == 'core' or options.class_type == None:
		fxn = parse_core_classes
	else:
		sys.stderr.write("class type of %s is invalid" % options.class_type)
	exec_main(parser, fxn, "classes")

if __name__ == "__main__":
	sys.exit(main())
