#!/usr/bin/env python

import sys
import fastaP
import itertools

my_sequence = fastaP.FASTAReader(open(sys.argv[1]))
my_proteins = fastaP.FASTAReader(open(sys.argv[2]))

#sys.argv[2] = mafftalignmentscorrect.fa
#sys.argv[1] = alignmentssortedcorrect.fa
#itertools.izip(list1, list2)

l1 = []
l2 = []

for stuff in my_sequence:
    l1.append(stuff)
    
for stuff in my_proteins:
    l2.append(stuff)

#for alignment in itertools.izip(my_sequence, my_proteins):
for alignment in itertools.izip(l1,l2):
    nuc_seq = alignment[0][1]
    prot_seq = alignment[1][1]
    new_seq = []
    n = 0 
    for aa in prot_seq:
        if aa == "-":
            new_seq.append("---")
        else:
            codon = nuc_seq[n:n+3]
            n += 3
            new_seq.append(codon)
    print ">"+alignment[0][0]
    print "".join(new_seq)
#print new_seq