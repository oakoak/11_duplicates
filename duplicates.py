import os
import argparse


def search_for_duplicate_files(path):
    name_files = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            size_file = os.path.getsize(root+"\\"+file)
            if (file, size_file) in name_files:
                name_files[(file, size_file)].append(root)
            else:
                name_files[(file, size_file)] = [root]
    duplicate_files = [
        [path+"\\"+duplicates[0] for path in name_files[duplicates]]
        for duplicates in name_files if len(name_files[duplicates]) > 1
    ]
    return duplicate_files


def pprint_duplicate_files(duplicates_files):
    for duplicates in duplicates_files:
        for file in duplicates:
            print(file)
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


if __name__ == '__main__':
    arguments = get_parser_args()

    if os.path.isdir(arguments.path):
        duplicates = search_for_duplicate_files(arguments.path)
        pprint_duplicate_files(duplicates)
    else:
        print("Error: This is a file or directory not found!")
