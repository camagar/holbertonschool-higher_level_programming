#!/usr/bin/python3
"""create"""
import sys
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


if __name__ == '__main__':
    """create object"""
    filename = "add_item.json"
    adding_list = sys.argv[1:]
    old_list = []

    if (os.path.exists(filename)):
        old_list = load_from_json_file(filename)
    new_list = old_list + (adding_list)
    save_to_json_file(new_list, filename)
