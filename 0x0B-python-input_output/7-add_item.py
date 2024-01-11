#!/usr/bin/python3

import json

def save_to_json_file(data, filename="add_item.json"):
  """Saves a Python data structure to a JSON file.

  Args:
    data: The Python data to be saved.
    filename: The name of the JSON file to save to.
  """

  with open(filename, "w") as file:
    json.dump(data, file)

def load_from_json_file(filename="add_item.json"):
  """Loads a Python data structure from a JSON file.

  Args:
    filename: The name of the JSON file to load from.

  Returns:
    The loaded Python data structure.
  """

  with open(filename, "r") as file:
    return json.load(file)

# Collect arguments from the command line
args = list(sys.argv[1:])  # Exclude the script name itself

# Load existing items from the JSON file, if it exists
existing_items = load_from_json_file()

# Combine existing items with new arguments
all_items = existing_items + args

# Save the combined list to the JSON file
save_to_json_file(all_items)

print(f"Items saved to add_item.json: {all_items}")
