#!/usr/bin/env python

import sys
import fasta
#command line arguments
k = int(sys.argv[3])

#create target dictionary key=kmer, value = list of positions of kmer
for ident, sequence in fasta.FASTAReader(open(sys.argv[1])):
    sequence = sequence.upper()
    kmer_position = {}
    for i in range(0, len(sequence)-k):
        kmer = sequence[i: i + k]
        position = (sequence[i])
        
         
        if kmer not in kmer_position:
            kmer_position[kmer] = []
        kmer_position[kmer].append(i)
        
# assign a position to each nucleotide in query sequence and find matches
    for ident2, sequence2 in fasta.FASTAReader(open(sys.argv[2])):      
        sequence2 = sequence2.upper()  
        for i, nuc in enumerate(range(0, len(sequence2)-k)):
            query_kmer = sequence2[nuc: nuc + k]

            if query_kmer in kmer_position:
                print ident,
                print kmer_position[query_kmer],
                print nuc,
                print query_kmer
            else:
                continue
           
        
     
     
     #print "---", ident, "---"
    #print kmer_position
    
    #print "---", ident, "---"
    
    #for i, kmer in enumerate(kmer_position):
        #print kmer, kmer_position[kmer]
    
    #for ident, sequence in fasta.FASTAReader(open(sys.argv[3])):
        #sequence = sequence.upper()
    
                      
    #print kmer, kmer_position[kmer]
            
            #print "---", ident, "---" #seperates each sequence with identifier
    
     
    #print kmer, position
    
 
        #for i, kmer in enumerate((kmer_position)):
            #if i > 10:
                #break
            #print kmer, kmer_position[kmer]
        
    
#kmer_matcher(sys.argv[1],sys.argv[2],sys.argv[3])
