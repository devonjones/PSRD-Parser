import os.path
import json
from psrd.files import char_replace

def generate_extension_file_name(output_dir, book):
	return os.path.join(
			os.path.abspath(output_dir), char_replace(book), 'extension.json')

def generate_extension_output_file_name(output_dir, book, fn):
	return os.path.join(
		os.path.abspath(output_dir),
		char_replace(book),
		'extensions',
		fn)

def load_extension_file(output_dir, book):
	filename = generate_extension_file_name(output_dir, book)
	with open(filename) as jsonfile:
		return json.load(jsonfile)

def write_output(output_dir, book, output, fn):
	filename = generate_extension_output_file_name(output_dir, book, fn)
	if not os.path.exists(os.path.dirname(filename)):
		os.makedirs(os.path.dirname(filename))
	with open(filename, 'w') as jsonfile:
		json.dump(output, jsonfile, indent=2)

