#!/usr/bin/env python
import sys
import os
import re
import json
import sqlite3
from psrd.options import load_option_parser, exec_load_main
from psrd.feats import load_feat

def main():
	usage = "usage: %prog [options] [filenames]\nImports feats into psrd db from feat json files."
	parser = load_option_parser(usage)
	exec_load_main(parser, load_feat)

if __name__ == "__main__":
	sys.exit(main())

