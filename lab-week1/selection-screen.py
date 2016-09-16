#!/usr/bin/env python

import sys
import fastaP
from itertools import cycle
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.style.use('ggplot')



my_sequence = fastaP.FASTAReader(open(sys.argv[1])) #backtonucleocorrect
#my_proteins = fastaP.FASTAReader(open(sys.argv[2])) #mtffacorrect   
queryfile = fastaP.FASTAReader(open(sys.argv[2]))

codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

mutations = {}
synonomous = {}
nonsynonomous = {}
alignment_seq_codons = []
#l2 = []

for identifier, sequence in my_sequence:
    alignment_seq_codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]


query_sequence_codons = []
for identifier2, sequence2 in queryfile:
    query_sequence_codons = [sequence2[i:i+3] for i in range(0, len(sequence2),3)]

for index, i in enumerate(query_sequence_codons):
    synonomous[index] = 0
    nonsynonomous[index] = 0
index = 0
#zip through each alignment match, and compare it to the query codons by cycling through the query for each alignment. 
for (a,b) in zip(alignment_seq_codons, cycle(query_sequence_codons)):
    if a not in codontable:
        continue
    elif b not in codontable:
        continue
    elif a == b:
        continue
    elif codontable[a] == codontable[b]:
        synonomous[index] += 1
    else:
        nonsynonomous[index] += 1
    if index <= 3427:
        index += 3
    else:
        index = 0
        
#print synonomous  
#print nonsynonomous      

syn_list = []
nonsyn_list = []
positions = []

for index in synonomous:
    syn_list.append(synonomous[index])
    
for index in nonsynonomous:
    nonsyn_list.append(nonsynonomous[index])
for index in synonomous:
    positions.append(index)

#now i have two lists - one of all the synonomous mutations and another with nonsynonomous mutations.
syn_nonsyn_list = []
for index in synonomous and nonsynonomous:
    syn_nonsyn_list.append((synonomous[index], nonsynonomous[index]))
    
d = []
for value in syn_nonsyn_list:
    d.append(value[1]-value[0])
    
array_of_d = np.array(d)
z_score = stats.zscore(array_of_d)
    
#print syn_nonsyn_list
#colors = ('darkblue', 'red')
plt.figure()
plt.title("Z-scores by position for synonomous and nonsynonomous mutations")
plt.scatter(positions, z_score)
plt.xlabel("position")
plt.ylabel("z-score")
plt.savefig("z-score by position.png")





#My many attempts to determine the answer to this question!
# mutations = {}
# pos = 0
# pos2 = 0
# location = 1
#
# for alignment in alignment_seq:
#     alignment = alignment_seq[pos]
#     pos += 1
#     for pos in range(0, len(alignment_seq)-3, 3):
#         sequence_codon = alignment[pos: pos + 3]
#         #print sequence_codon
#         query_codon = query[pos: pos + 3]
#         #print query_codon
#                 #print query_codon
#         if codontable[sequence_codon] == codontable[query_codon]:
#             if sequence_codon == query_codon:
#                 if location not in mutations:
#                     mutations[location] = [("match")]
#                 else:
#                     mutations[location].append("match")
#                     location += 1
#             else:
#                 if location not in mutations:
#                     mutations[location] = [("dS")]
#                 else:
#                     mutations[location].append("dN")
#                     location += 1
# for key in mutations.keys():
#     for mutation in mutations[key]:
#         synonomous = mutations[key].count("dS")
#         non_synonomous = mutations [key].count("dN")
#     print synonomous
#
#
#
# # # for seq in my_sequences:
# # # for stuff in my_proteins:
# # #     l2.append(stuff)
# # #
# # # for n in range(0,len(alignment_seq)-3,3):
# # # for pos in alignment_seq:
# # #     pos= 0
# # #     alignment_codon = alignment_seq[pos: pos +3]
# # #     query_codon = query[pos: pos + 3]
# # #     #amino_acid_alignment_codon = codontable.get(alignment_codon)
# # #     #amino_acid_query_codon = codontable.get(query_codon)
# # # #for alignment in itertools.izip(my_sequence, my_proteins):
# # #     #for alignment in alignment_seq:
# # #     #nuc_seq = alignment[0][1]
# # #     #prot_seq = alignment[1][1]
# # #     #new_seq = []
# # #     dN = 0
# # #     dS = 0
# # #     dN_list = []
# # #     dS_list = []
# # #         #codon = nuc_seq[n:n+3]
# # #
# # #     if alignment_codon == query_codon:
# # #         n +=3
# # #         continue
# # #         #elif alignment_seq[n: n + 3] != query[n: n +3]:
# # #
# # #     elif codontable[alignment_codon] == codontable[query_codon]:
# # #         n += 3
# # #         dS += 1
# # #         dS_list.append(n)
# # #     else:
# # #         n += 3
# # #         dN += 1
# # #         dN_list.append(n, dN)
# # #
# # # print dS
# # # print dN
# # #
# # #
# # #
# # #
# # # #key = codon, value= protein
# # #
