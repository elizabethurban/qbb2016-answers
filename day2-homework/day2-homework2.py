#!/usr/bin/env python

#part 2 identifyer mapping

#terminal inputs, f=day2-homework2.out, c=t_data.ctab, o=option
import sys
f = open(sys.argv[1])
c = open(sys.argv[2])
o = int(sys.argv[3]) #input 1 or 2 for special character or to ignore 

#define dictionary using f
dic = {}

for line in f:
    fields = line.rstrip("\r\n").split()
    fly_id = fields[0]
    uni_id = fields[1]
    dic[fly_id]= uni_id

#print dic
 
# determine if t_dat matches dictionary and define print options for match or no match    
for line in c:
    #print line
    # line=line.strip()
    fields = line.rstrip("\r\n").split()
    ctab_gene_id = fields[8]
    #print ctab_gene_id
# #print outputs for matches, or the options if match does not exist
    if o == 1:
        if ctab_gene_id in dic:
            #print "yes" + ctab_gene_id
            print dic[ctab_gene_id], "\t", line
        elif ctab_gene_id not in dic:
            print "* * * " 
    elif o == 2:
        if ctab_gene_id in dic:
            #print "yes" + ctab_gene_id
            print dic[ctab_gene_id], "\t", line
        elif ctab_gene_id not in dic:
            continue
    
  #   elif o == 1:
  #       print dic[fly_id], "\t", "."
  #   elif o == 2:
  #       continue
