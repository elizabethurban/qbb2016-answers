#!/usr/bin/env python
"""ordinary linear regression"""

import sys
import numpy as np
import pandas as pd
import statsmodels.api as sm

df = pd.read_table(sys.argv[1]) #t-data.ctab fpkm values
df2 = pd.read_table(sys.argv[2],header=None) #.tab files

fpkm_list = []
mean_list = []

for row in df.itertuples():
    fpkm = [row[-1]]
    chrom = row[2]
    if chrom in ["2L", "2R", "3L", "3R", "4", "X"]:
        fpkm_list.append(fpkm)
  

for row in df2.itertuples():
    mean = [row[5]]
    mean_list.append(mean)

#debugging difference in list length-error due to header     
#print len(fpkm_list)
#print len(mean_list)


model = sm.OLS(mean_list, fpkm_list)
res = model.fit()
print res.summary()