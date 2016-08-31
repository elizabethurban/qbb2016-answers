#!/usr/bin/env python

#part 1 mapping and parsing flydata to make flybas_id and uniprot_id
import sys
f = open(sys.argv[1]) #input flydata.txt 

mapping = {}
#filter out all lines lacking "DROME" and if the the length of fields is not 4
for line in f.readlines():
    fields = line.rstrip("\r\n").split()
    if "DROME" not in line:
        continue
    
    if len(fields) != 4:
        continue
    else:
        print fields[3], "\t", fields[1] #print day2-homework2.out
        
        
        
        
    