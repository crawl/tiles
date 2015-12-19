#!/usr/bin/python

import os

bad_names = set()

with open("TILES2.TXT") as f:
    for line in f:
    	bad_names.add (line.rstrip ())

path = "/Users/donblas/Programming/crawl/crawl-ref/source/rltiles"
for root, dirs, files in os.walk(path):
	path = root.split('/')
	for file in files:
		if file in bad_names:
			print str(root) + "/" + file
