#!/usr/bin/env python
import sys
import os
import re
import json
from BeautifulSoup import BeautifulSoup
from psrd.creatures import parse_creature
from psrd.warnings import WarningReporting
from psrd.options import exec_main, option_parser

def main():
	usage = "usage: %prog [options] [filenames]\nParses creatures from psrd html to json and writes them to the specified directory"
	parser = option_parser(usage)
	exec_main(parser, parse_creature, "creatures")

if __name__ == "__main__":
	sys.exit(main())

