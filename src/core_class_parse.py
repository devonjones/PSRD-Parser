#!/usr/bin/env python
import sys
import os
import re
import json
from BeautifulSoup import BeautifulSoup
from psrd.classes import parse_core_classes
from psrd.warnings import WarningReporting
from psrd.options import exec_main, option_parser

def main():
	usage = "usage: %prog [options] [filenames]\nParses core classes from psrd html to json and writes them to the specified directory"
	parser = option_parser(usage)
	exec_main(parser, parse_core_classes, "core_classes")

if __name__ == "__main__":
	sys.exit(main())
