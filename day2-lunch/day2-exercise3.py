#!/usr/bin/env python

#number 3-counts number of reads with 1 alignments:
import sys
f = open(sys.argv[1])

count = 0
for line in f.readlines():
    fields = line.rstrip("\r\n").split("\t")
    if line.startswith("@"):
        continue
    elif "NH:i:1" in line:
        count += 1
    else:
        continue
        
print count
    
f.close()