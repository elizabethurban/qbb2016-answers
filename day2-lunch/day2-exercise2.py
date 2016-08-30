#!/usr/bin/env python

#number 1-counts number of alignments:
import sys
f = open(sys.argv[1])

count = 0
for line in f.readlines():
    fields = line.rstrip("\r\n").split("\t")
    if line.startswith("@"):
        continue
    elif fields[2] == "*":
        continue
    else:
        count += 1
        
print count
    
f.close()

    