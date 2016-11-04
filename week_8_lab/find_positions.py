#!/usr/bin/env python

from __future__ import division 
import sys
import numpy as np
import h5py

file = h5py.File("Out_enrichment_bin0.heat")
#file.keys()
#[u'0.counts', u'0.expected', u'0.positions', u'regions']
#want to pull the matrix out of 0.counts first 
df = open(sys.argv[1])

ctcf_positions = []
for i, line in enumerate(df):
    fields = line.rstrip("\n\r").split("\t")
    if fields[0] == "chrX":
        ctcf_positions.append(fields[1])
    else:
        continue
    

#print ctcf_positions

heat_map_positions = file['0.positions'][...]

print heat_map_positions



