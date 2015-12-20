#!/usr/bin/python

import os

bad_names = set()

with open("TILES2.TXT") as f:
    for line in f:
    	bad_names.add (line.rstrip ())

bad_count = 0
good_count = 0
path = "/Users/donblas/Programming/crawl/crawl-ref/source/rltiles"
for root, dirs, files in os.walk(path):
	path = root.split('/')
	for file in files:
		if file in bad_names:
			print str(root) + "/" + file
			bad_count += 1
		else:
			good_count += 1

print "Good: " + str(good_count)
print "Bad: " + str(bad_count)

