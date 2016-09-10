#!/usr/bin/env python

import sys



openfile = open(sys.argv[1])


# seq_id = []
# sequence = []

for line in openfile:
    fields = line.rstrip("\r\n").split()
    seq_id = fields[0]
    sequence = fields[3]
    if int(fields[2]) - int(fields[1]) < 10292:
        continue
    elif "-" in line:
        newline = line.replace("-", "")
    else:
        print ">" + seq_id
        print sequence 

