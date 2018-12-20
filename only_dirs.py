#!/usr/bin/env python

#command line version
#python -c 'import os,sys;dirs=[ r for r,s,f in os.walk(".") if r != "."];[os.makedirs(os.path.join(sys.argv[1],i)) for i in dirs]' ~/new_destination

scanned_directory="/media/raphael/Mystery"
destination="/home/raphael/illus_bio/mystery"

import os,sys
os.chdir(scanned_directory)
dirs=[ r for r,s,f in os.walk(".") if r != "."]
print dirs
os.chdir(destination)
for i in dirs:

	#newdir=os.path.join(destination,i)
	newdir=i
	print
	print newdir
	print
	if not os.path.isdir(newdir):
		os.makedirs(newdir) 
