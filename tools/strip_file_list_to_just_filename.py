#!/usr/bin/python

import os

with open("TILES.TXT") as f:
    for line in f:
    	print os.path.basename (line).rstrip ()
