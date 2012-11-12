#!/usr/bin/env python
import sys
import os
import re
import json
import sqlite3
from psrd.options import load_option_parser, exec_load_main
from psrd.central_index import load_central_index

def main():
	usage = "usage: %prog [options] [filenames]\nCreates a central index that crosses across books."
	parser = load_option_parser(usage)
	exec_load_main(parser, load_central_index)

if __name__ == "__main__":
	sys.exit(main())

