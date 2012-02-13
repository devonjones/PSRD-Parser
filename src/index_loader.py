#!/usr/bin/env python
import sys
import os
import re
import json
import sqlite3
from psrd.options import load_option_parser, exec_load_main
from psrd.index import load_section_index

def main():
	usage = "usage: %prog [options] [filenames]\nCreates an index based on the section names in the db already."
	parser = load_option_parser(usage)
	exec_load_main(parser, load_section_index)

if __name__ == "__main__":
	sys.exit(main())

