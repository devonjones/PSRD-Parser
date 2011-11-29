#!/usr/bin/env python
import sys
import os
import re
import json
import sqlite3
from psrd.options import load_option_parser, exec_load_main
from psrd.loader import load_rule_structure_documents

def main():
	usage = "usage: %prog [options] [filenames]\nImports rules into psrd db from feat json files using a specified structure."
	parser = load_option_parser(usage)
	exec_load_main(parser, load_rule_structure_documents)

if __name__ == "__main__":
	sys.exit(main())

