#!/usr/bin/python3
""" import sys to access system function"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Create a list of arguments
args = sys.argv[1:]

# Load the existing list from the file, or create a new one if the file does not exist
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []

# Add the arguments to the list
my_list.extend(args)

# Save the list to the file as a JSON representation
save_to_json_file(my_list, "add_item.json")
