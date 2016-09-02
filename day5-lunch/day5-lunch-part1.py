#!/usr/bin/env python
"""Determine the approximation of the promoter region for each of the trascripts in SRR072893"""

import sys
import numpy as np
import pandas as pd

#find promoter- convert start site to range plus and minus 500 basepairs. if strant + then go around start position, if strand is - then go around the end position. Filter c-tab file to remove anything that is not chrom 2l 2r 3l 3r 4 or x
base = sys.argv[1]
df = pd.read_table(sys.argv[1])


col_names = ["chr", "start", "end", "t_name"]
promoter_region = []

for row in df.itertuples():
    #print row[3]
    strand = row[3]
    chrom = row[2]
    if chrom in ["2L", "2R", "3L", "3R", "4", "X"]:

        if strand == "+":
            table =      [row[2], row[4] - 500, row[4] + 500, row[6]]   
            promoter_region.append(table)
        elif strand == "-":
            table2 =    [row[2], row[5] + 500, row[5] - 500, row[6]]   
            #print table2
            promoter_region.append(table2)
        else:
            print "SOMETHING WACKY"
#create dataframe
new_df_promoter = pd.DataFrame(promoter_region)
new_df_promoter.to_csv("promoters.bed", sep="\t", header=False, index=False)

#for i in new_df_promoter.itertuples(): print i



# for _, chr, strand, start, end, t_name in df.itertuples():
#     d[chr + start + end + t_name] = pd.read_table(base + "/")




