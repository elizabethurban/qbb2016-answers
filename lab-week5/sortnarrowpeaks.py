#!/usr/bin/env python

import sys

df = open(sys.argv[1])

for i, line in enumerate(df):
    fields = line.rstrip("\n\r").split("\t")
    print fields[0] + "\t" + fields[1] + "\t" + fields[2] + "\t" + fields[3] + "\t" + fields[4] + "\t" + fields[5]
    
    