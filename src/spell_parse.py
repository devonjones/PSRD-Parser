#!/usr/bin/env python
import sys
import os
import re
import json
from psrd.options import exec_main, option_parser
from psrd.spells import parse_spell

def main():
	usage = "usage: %prog [options] [filenames]\nParses spells from psrd html to json and writes them to the specified directory"
	parser = option_parser(usage)
	exec_main(parser, parse_spell, "spells")

def optionParser():
	parser = OptionParser(usage=usage)
	parser.add_option("-b", "--book", dest="book", help="Book spells are from (required)")
	parser.add_option("-o", "--output", dest="output", help="Output data directory.  Should be top level directory of psrd data. (required)")
	return parser

if __name__ == "__main__":
	sys.exit(main())
