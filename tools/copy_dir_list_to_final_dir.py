#!/usr/bin/python
"""
copy_dir_list_to_final_dir.py

Purpose:

Walk the given directory, and find files to move to the release directory,
ignoring any files listed in a special exclusion file

Optional Flags:

    FLAGS           EXAMPLE VALUES

    -f,  --file     /path/to/TILES.txt
    -d,  --dir      /path/to/crawl/crawl-ref/source/rltiles
    -o,  --out      /path/to/releases/Nov-2015

Usage:

This script can be run from the commandline with no optional parameters, by
simply modifying the config variables at the top of the script:

    python copy_dir_list_to_final_dir.py

Or you can run this script from the commandline with the two flags to set
the exclusion file and directory to walk:

    python copy_dir_list_to_final_dir.py -f TILES2.txt
    python copy_dir_list_to_final_dir.py -d /path/to/rtiles
    python copy_dir_list_to_final_dir.py --out /path/to/releases/Nov-2015
    python copy_dir_list_to_final_dir.py --file TILES2.txt -d rtiles
    python copy_dir_list_to_final_dir.py -f TILES2.txt --dir source/rtiles

"""
import os
from shutil import copyfile

# CONFIG (DEFAULT) VARIABLES
EXCLUDE_FILE = "TILES2.TXT"
TILES_DIR = "/Users/donblas/Programming/crawl/crawl-ref/source/rltiles"
OUTPUT_DIR = "/Users/donblas/Programming/tiles/releases/Nov-2015"


def main():
    # default (or manually-configure) inputs
    exclude_file = EXCLUDE_FILE
    tiles_dir = TILES_DIR
    output_dir = OUTPUT_DIR

    # commandline parsing
    a = 1
    while a < len(argv):
        if argv[a] in ('-f', '--file'):
            a += 1
            exclude_file = argv[a]
        elif argv in ('-d', '--dir'):
            a += 1
            tiles_dir = argv[a]
        elif argv in ('-o', '--out'):
            a += 1
            output_dir = argv[a]
        else:
            usage()
        a += 1

    # walk the directory and print your exclusion files
    copy_dir_list_to_final_dir(exclude_file, tiles_dir, output_dir)


def copy_dir_list_to_final_dir(exclude_file, tiles_dir, output_dir):
    """ walk the given directory, and find files to move to the release directory,
    ignoring any files listed in a special exclusion file

    Args:
        exclude_file (str): a simple file, with one file name on each line
        tiles_dir (str): a directory containing files of interest
        output_dir (str): an output directory to copy your files to
    Returns: None
    """
    bad_names = set()

    # read the file with names of other files to exclude
    with open(exclude_file) as f:
        for line in f:
            if len(line.strip()) > 0:
                bad_names.add(line.strip())

    # walk the given directory, and find files to move to the release directory
    bad_count = 0
    good_count = 0
    path = tiles_dir
    for root, dirs, files in os.walk(path):
        mRoot = root.replace(path, "")
        for file in files:
            if not file.endswith(".png"):
                continue

            if file in bad_names:
                bad_count += 1
            else:
                try:
                    os.makedirs(output_dir + "/" + mRoot)
                except OSError:
                    pass
                shutil.copyfile(root + "/" + file, output_dir + "/" + mRoot + "/" + file)
                good_count += 1

    # print some helpful counts of good/bad files
    print("Good: " + str(good_count))
    print("Bad: " + str(bad_count))


def usage():
    """ Print a help menu to the screen. """
    print(__doc__)
    exit()


if __name__ == '__main__':
    main()
