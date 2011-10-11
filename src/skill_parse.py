#!/usr/bin/env python
import sys
import os
import re
import json
from psrd.skills import parse_skills
from psrd.options import exec_main, option_parser

def main():
	usage = "usage: %prog [options] [filenames]\nParses skills from psrd html to json and writes them to the specified directory"
	parser = option_parser(usage)
	exec_main(parser, parse_skills, "skills")

if __name__ == "__main__":
	sys.exit(main())
