#!/usr/bin/env python

#number 4-prints chromosome that allignment aligns to for the first 10 alignments:
import sys
f = open(sys.argv[1])

actual_alignments = []

for line in f.readlines():
    fields = line.rstrip("\r\n").split("\t")
    if line.startswith("@"):
        continue
    else:
        actual_alignments.append(line)
        
count = 0
for entry in actual_alignments:
    fields = entry.rstrip("\r\n").split("\t")
    if fields[2] == "*":
        continue
    else:
        if count <= 9:
            print fields[2]
            count += 1
        else:
            continue  
    
f.close()