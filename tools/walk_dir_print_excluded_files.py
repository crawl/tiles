#!/usr/bin/python
"""
walk_dir_print_excluded_files.py

Purpose:

Walk the given directory, and find files to exclude based on
a simple input file that lists files to exclude.

Optional Flags:

    FLAGS              EXAMPLE VALUES

    -f,  --file        /path/to/TILES.txt
    -d,  --dir         /path/to/crawl/crawl-ref/source/rltiles

Usage:

This script can be run from the commandline with no optional parameters, by
simply modifying the config variables at the top of the script:

    python walk_dir_print_excluded_files.py

Or you can run this script from the commandline with the two flags to set
the exclusion file and directory to walk:

    python walk_dir_print_excluded_files.py -f TILES2.txt
    python walk_dir_print_excluded_files.py -d /path/to/rtiles
    python walk_dir_print_excluded_files.py --file TILES2.txt -d rtiles
    python walk_dir_print_excluded_files.py -f TILES2.txt --dir source/rtiles

"""
from os import walk
from sys import argv

# CONFIG (DEFAULT) VARIABLES
EXCLUDE_FILE = "TILES2.TXT"
TILES_DIR = "/Users/donblas/Programming/crawl/crawl-ref/source/rltiles"


def main():
    # default (or manually-configure) inputs
    exclude_file = EXCLUDE_FILE
    tiles_dir = TILES_DIR

    # commandline parsing
    a = 1
    while a < len(argv):
        if argv[a] in ('-f', '--file'):
            a += 1
            exclude_file = argv[a]
        elif argv in ('-d', '--dir'):
            a += 1
            tiles_dir = argv[a]
        else:
            usage()
        a += 1

    # walk the directory and print your exclusion files
    walk_dir_print_excluded_files(exclude_file, tiles_dir)


def walk_dir_print_excluded_files(exclude_file, tiles_dir):
    """ walk the given directory, and find files to exclude based on
    a simple input file that lists files to exclude

    Args:
        exclude_file (str): a simple file, with one file name on each line
        tiles_dir (str): a directory containing files of interest
    Returns: None
    """
    bad_names = set()

    # read the file with names of other files to exclude
    with open(exclude_file) as f:
        for line in f:
            if len(line.strip()) > 0:
                bad_names.add(line.strip())

    # walk the given directory, and find files to exclude
    bad_count = 0
    good_count = 0
    path = tiles_dir
    for root, dirs, files in walk(path):
        path = root.split('/')
        for file in files:
            if file in bad_names:
            	# print any file that needs to be excluded
                print(str(root) + "/" + file)
                bad_count += 1
            else:
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
