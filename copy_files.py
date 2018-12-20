#!/usr/bin/env python
# -*- coding: utf-8 -*-
#



import shutil
source="/home/raphael/Music/18 - Juste quelqu'un de bien.mp3"
destination="/home/raphael/18 - Juste quelqu'un de bien.mp3"
shutil.copy2(source, destination)

import csv
#import codecs
newpath=""
with open("./list_missing.csv", "rb") as f:
	reader = csv.reader(f)
	j=0
	for row in reader:
		j+=1
		if j>1:
			print row[1]
			source=row[1]
			print
			x=row[1].split("/")
			i=0
			for part in x:
				i+=1
				#print part
				if i==4:#replace fourth part of the path
					part="Ananda"
				if i>1:
					newpath=newpath+"/"+part
			print newpath
			destination=newpath
			newpath=""
			shutil.copy2(source, destination)
			print
			print
		
				
	#print reader[2][2]

