#!/usr/bin/env python
import sys
import os
import re
import json
import sqlite3
from psrd.options import load_option_parser, exec_load_main
from psrd.loader import load_spell_list_documents

def main():
	usage = "usage: %prog [options] [filenames]\nImports spell lists into psrd db from feat json files."
	parser = load_option_parser(usage)
	exec_load_main(parser, load_spell_list_documents)

if __name__ == "__main__":
	sys.exit(main())

