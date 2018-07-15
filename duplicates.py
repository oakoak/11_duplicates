import os
import argparse
from collections import defaultdict


def search_for_duplicate_files(path):
    files_name_size_paths = defaultdict(list)
    for root, dirs, name_files in os.walk(path):
        for name_file in name_files:
            size_file = os.path.getsize(os.path.join(root, name_file))
            files_name_size_paths[(name_file, size_file)].append(root)
    duplicate_files = [
        [os.path.join(path, duplicates[0]) for path in files_name_size_paths [duplicates]]
        for duplicates in files_name_size_paths  if len(files_name_size_paths [duplicates]) > 1
    ]
    return duplicate_files


def pprint_duplicate_files(duplicates_files):
    for duplicates in duplicates_files:
        for name_file in duplicates:
            print(name_file)
        print("\n")


def get_parser_args():
    parser = argparse.ArgumentParser(
        description="Path to the check for duplication"
    )
    parser.add_argument(
        "path",
        help="input path to check"
    )
    return parser.parse_args()


if __name__ == "__main__":
    arguments = get_parser_args()

    if os.path.isdir(arguments.path):
        duplicates = search_for_duplicate_files(arguments.path)
        pprint_duplicate_files(duplicates)
    else:
        print("Error: This is a file or directory not found!")
