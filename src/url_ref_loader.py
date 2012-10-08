#!/usr/bin/env python
import sys
import os
import re
import json
import sqlite3
from psrd.options import load_option_parser, exec_load_main
from psrd.url_ref import load_url_references

def main():
	usage = "usage: %prog [options] [filenames]\nLoads URL sym links for URLs no longer in the system."
	parser = load_option_parser(usage)
	exec_load_main(parser, load_url_references)

if __name__ == "__main__":
	sys.exit(main())

