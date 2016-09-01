#!/usr/bin/env python


import sys
import pandas as pd
import matplotlib.pyplot as plt



#plot fpkm over chromosome 
#how does expression of transcripts track along chromosome

df = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])

#look at only 1 chromosome-3 so select only rows where 3l

#def rolling_mean("chrom"):
    
chromosome_list = ["2L", "2R", "3L", "3R", "4", "X"]
 
for chrom in chromosome_list:
    n = int(sys.argv[3])
    df_roi = df["chr"] == chrom
    df_chrom = df[df_roi] 

    df2_roi= df2["chr"] == chrom
    df2_chrom = df2[df2_roi]
        
    plot = df_chrom["FPKM"].rolling(n).mean() 
    plot2 = df2_chrom["FPKM"].rolling(n).mean()
# make immage for 2L 2R 3L 3R 4 and X - loop to print each? 
    plt.figure()
    plt.title("Chromosome %s, FPKM rolling mean (size = n)" % chrom)
    plt.plot(plot)
    
    plt.plot(plot2)
    plt.xlabel("Position")
    plt.ylabel("FPKM")
    plt.savefig(chrom + ".png")
    plt.close()
    
    
    
    
    