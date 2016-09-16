#!/usr/bin/env python

import sys
import fastaP
import itertools
import numpy as np

contigs = fastaP.FASTAReader(open(sys.argv[1]))

#count contigs
contigs_list = []
contigs_list_sorted = []
count = 0
for identifier, sequence in contigs:
        count += 1
        length_contig = len(sequence)
        contigs_list.append(length_contig)
        contigs_list.sort()
        total_length_contigs = sum(contigs_list)
        half_length_contigs = (total_length_contigs/ 2)

print count, "number of contigs"
#print contigs_list
print max(contigs_list), "max contigs length"
print min(contigs_list), "min contigs length"
print np.mean(contigs_list), "mean contig length"
#print total_length_contigs
#print half_length_contigs
length_so_far = 0
for length in contigs_list:
    length_so_far += length
    #if length_so_far < half_length_contigs:
        #length_so_far += length
    if length_so_far >= half_length_contigs:
        n50 = length 
        break
    else:
        continue
print n50, "n50"     
    
