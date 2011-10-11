#!/usr/bin/env python
import sys
import os
import re
import json
from BeautifulSoup import BeautifulSoup
from psrd.spell_lists import parse_spell_lists
from psrd.options import exec_main, option_parser

def main():
	usage = "usage: %prog [options] [filenames]\nParses spell lists from psrd html to json and writes them to the specified directory"
	parser = option_parser(usage)
	exec_main(parser, parse_spell_lists, "spell_lists")

if __name__ == "__main__":
	sys.exit(main())
