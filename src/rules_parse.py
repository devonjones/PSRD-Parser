#!/usr/bin/env python
import sys
import os
import re
import json
from psrd.rules import parse_rules
from psrd.universal import parse_universal
from psrd.options import exec_main, option_parser

def main():
	usage = "usage: %prog [options] [filenames]\nParses files from psrd html to json and writes them to the specified directory"
	parser = option_parser(usage, title=True)
	exec_main(parser, parse_rules, "rules")

if __name__ == "__main__":
	sys.exit(main())
