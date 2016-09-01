#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#read in the two datasets and filter for sxl genes and fpkm >0 
df =pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])

df_roi = (df["gene_name"] == "Sxl") & (df["FPKM"] > 0)
df_sxl_expres = df[df_roi]

df2_roi = (df2["gene_name"] == "Sxl") & (df["FPKM"] > 0)
df2_sxl_expres = df2[df2_roi]

#calculate the log of the fpkm values 
fpkm_log = np.log(df_sxl_expres["FPKM"])
fpkm_log2 = np.log(df2_sxl_expres["FPKM"])

# #check that fpkm log works
# # print fpkm_log
# # print fpkm_log2

#generate the bokplot using plt
plt.figure()
plt.title("FPKM of Sxl gene for SRR072893 and SRR072915")
plt.boxplot([fpkm_log, fpkm_log2], labels=["SRR072893", "SRR072915"])
plt.xlabel("Fly source")
plt.ylabel("FPKM")
plt.savefig("day4_lunch_boxplot.png")
plt.close()




# Bad code - took way too long
# fpkm_median = np.median(fpkm_log)
# fpkm_median2 = np.median(fpkm_log2)
# #check that median values are calculated
# # print fpkm_median
# # print fpkm_median2
#
# fpkm_upper_quartile = np.percentile(fpkm_log, 75)
# fpkm_upper_quartile2 = np.percentile(fpkm_log2, 75)
#
# fpkm_lower_quartile = np.percentile(fpkm_log, 25)
# fpkm_lower_quartile2 = np.percentile(fpkm_log2, 25)
#
# iqr = fpkm_upper_quartile - fpkm_lower_quartile
# iqr2 = fpkm_upper_quartile2 - fpkm_lower_quartile2
#
# upper_wisker = fpkm_log[fpkm_log<=fpkm_upper_quartile + 1.5 * iqr].max()
# upper_wisker2 = fpkm_log2[fpkm_log2<=fpkm_upper_quartile2 + 1.5 * iqr2].max()
#
# lower_wisker = fpkm_log[fpkm_log>=fpkm_lower_quartile - 1.5 * iqr].min()
# lower_wisker2 = fpkm_log2[fpkm_log2>=fpkm_lower_quartile2 - 1.5 * iqr2].min()

# print fpkm_upper_quartile
# print fpkm_lower_quartile
# print upper_wisker
# print lower_wisker



#print df_sxl_expres["FPKM"]
#print df2_sxl_expres["FPKM"]

#we have only the sxl genes with fpkm>0
#next extract the FPKM value along with its identity and determine the log(fpkm)

# plot1 = df_sxl_expres.boxplot(by = "FPKM", return_type = "both")
# print plot1
# plot2 = df2_sxl_expres.boxplot(by = "FPKM", return_type = "both")
# print plot2
