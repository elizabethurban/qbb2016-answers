#!/usr/bin/env python

#number 5-calculates average MAPQ score:
import sys
f = open(sys.argv[1])

total = 0
count = 0
for line in f.readlines():
    fields = line.rstrip("\r\n").split("\t")
    if line.startswith("@"):
        continue
    elif fields[2] == "*":
        continue
    elif fields[4] == "255":
        continue
    else:
        for value in fields[4]:
            count +=1
            total += float(fields[4])
        
average = float(total) / count
print average

f.close()
       
        