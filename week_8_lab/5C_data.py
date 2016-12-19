#!/usr/bin/env python

from __future__ import division 
import sys
import numpy as np
import h5py

"""note I was not able to complete this assignment but I got as far as I could on my own
I have submitted the code up until the point it no longer works. I was able to
get the strongest partner coordinates but cannot identify which CTCF containing fragment 
they correspond to"""

file = h5py.File("Out_enrichment_bin0.heat")
#file.keys()
#[u'0.counts', u'0.expected', u'0.positions', u'regions']
#want to pull the matrix out of 0.counts first 



counts = file['0.counts'][...]
expected = file['0.expected'][...]

# c = np.nonzero(counts)
# e = np.nonzero(expected)

where = np.where(counts > 0)

results = np.empty(counts.shape)
results[where]= np.log(counts[where]/expected[where])

#print results
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

#print heat_map_positions
value_in_heat_maps = []
for position in ctcf_positions:
    if int(position) < 98831147:
        continue
    elif int(position) > 103425148:
        continue
    else:
        value_in_heat_maps.append(position)
        
print value_in_heat_maps

for position in value_in_heat_maps:
    

# for i, position in enumerate(value_in_heat_maps):
#     if position in results:
#         print position
#     else:
#         continue
#
# print position
#
        
        
        
    


