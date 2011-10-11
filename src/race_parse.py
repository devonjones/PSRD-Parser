#!/usr/bin/env python
import sys
import os
import re
import json
from BeautifulSoup import BeautifulSoup
from psrd.races import parse_races
from psrd.warnings import WarningReporting
from psrd.options import exec_main, option_parser

def main():
	usage = "usage: %prog [options] [filenames]\nParses races from psrd html to json and writes them to the specified directory"
	parser = option_parser(usage)
	exec_main(parser, parse_races, "races")

if __name__ == "__main__":
	sys.exit(main())
