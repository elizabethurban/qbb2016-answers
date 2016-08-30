#!/usr/bin/env python

#number 2-counts number of perfect alignments:
import sys
f = open(sys.argv[1])

count = 0
for line in f.readlines():
    fields = line.rstrip("\r\n").split("\t")
    if line.startswith("@"):
        continue
    elif "NM:i:0" in line:
        count += 1
    else:
        continue
        
print count
    
f.close()

    