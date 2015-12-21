#!/usr/bin/python

import os
import shutil

bad_names = set()

with open("TILES2.TXT") as f:
    for line in f:
    	bad_names.add (line.rstrip ())

bad_count = 0
good_count = 0
path = "/Users/donblas/Programming/crawl/crawl-ref/source/rltiles"
final_path ="/Users/donblas/Programming/tiles/releases/Nov-2015"

for root, dirs, files in os.walk(path):
	mRoot = root.replace ("/Users/donblas/Programming/crawl/crawl-ref/source/rltiles", "")
	for file in files:
		if not file.endswith (".png"):
			continue
		if file in bad_names:
			bad_count += 1
		else:
			try:
				os.makedirs (final_path + "/" + mRoot)
			except OSError:
				pass
			shutil.copyfile (root + "/" + file, final_path + "/" + mRoot + "/" + file)
			good_count += 1

print "Good: " + str(good_count)
print "Bad: " + str(bad_count)

