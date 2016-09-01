#!/usr/bin/env python



import sys
import fasta
#command line arguments
k = int(sys.argv[3])


full_length_sequence_match = []

for ident, sequence in fasta.FASTAReader(open(sys.argv[1])):

    sequence = sequence.upper()
    kmer_position = {}
    t_seq = {}
    for i in range(0, len(sequence)-k):
        kmer = sequence[i: i + k]
        position = (sequence[i])
        
         
        if kmer not in kmer_position:
            kmer_position[kmer] = []
        kmer_position[kmer].append(i)
        

    for ident2, sequence2 in fasta.FASTAReader(open(sys.argv[2])):      
        sequence2 = sequence2.upper()  
        file_one_output = []
        for i, nuc in enumerate(range(0, len(sequence2)-k)):
            query_kmer = sequence2[nuc: nuc + k]
            
            
            if query_kmer in kmer_position:
                #print ident,
                #print kmer_position[query_kmer],
                #print nuc,
                #print query_kmer
                file_one_output.append([ident, kmer_position[query_kmer], nuc, query_kmer])
            else:
                continue
#print file_one_output
#for item in file_one_output:
    #print item[3] prints the query_kmer           
   # going backwards         

    for query_kmer in kmer_position:
        target = sequence
        for j in kmer_position[query_kmer]:
            n = k
            n2 = 1
            #find end of matchingness
            while 1:
                if nuc + n == len(sequence2) or j + n == len(target):
                    break 

                if sequence2[nuc + n] == target[j + n]:
                    n += 1
                else:
                    break
           #find start of matchingness
            while 1:
                if nuc - n2 == 0 or j - n2 == 0:
                    break
            
                if sequence2[nuc - n2] == target[j - n2]:
                    n2 += 1
                else:
                    break
                
            length_match = sequence2[nuc - n2 + 1: nuc + n]

            full_length_sequence_match.append(length_match)

for seq in sorted(full_length_sequence_match, key=len, reverse=True)[:1000]:
    print seq
                








               
           
                   
                    
                
                
                
              
           
        