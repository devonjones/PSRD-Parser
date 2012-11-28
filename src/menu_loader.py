#!/usr/bin/env python
import sys
import os
import re
import json
import sqlite3
from psrd.options import load_option_parser, exec_load_main
from psrd.menu import load_menu

def main():
	usage = "usage: %prog [options] [filenames]\nImports the menu into the index db."
	parser = load_option_parser(usage)
	exec_load_main(parser, load_menu)

if __name__ == "__main__":
	sys.exit(main())

