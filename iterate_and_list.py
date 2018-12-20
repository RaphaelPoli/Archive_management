

#Creates a csv list of all files in the subtree

import os
import csv
print csv.list_dialects()
rootdir = '/media/raphael/Jnana/00_Raphael_Poli_Oeuvre_Complete/'
results=[]
#list of list creates a csv table
#first list is first row
#second list is second row

for subdir,dirs, files in os.walk(rootdir):
	for file in files:
		#print os.path.join(subdir, file)
		results.append([file,subdir])

with open("/home/raphael/illus_bio/list_files_Jnana.csv",'wb') as resultFile:
	wr = csv.writer(resultFile, dialect='excel')
	#results=[["test1","test1",],["test2","test2"]]
	for line in results:
		wr.writerow(line)
