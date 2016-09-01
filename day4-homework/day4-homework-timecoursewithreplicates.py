#!/usr/bin/env python


import sys
import pandas as pd
import matplotlib.pyplot as plt

df_meta = pd.read_csv(sys.argv[1]) #samples.csv
df_replicates = pd.read_csv(sys.argv[2]) #replicates.csv
ctab_dir = sys.argv[3] #/users...results/stringtie/

#make female plot from paper
#[1, 0, 2, 10, 50, 100]

female_Sxl = []
male_Sxl = []
male_Sxl_replicates = []
male_Sxl_replicates_stages = [4, 5, 6, 7]
df_roi = df_meta["sex"] == "male"
df2_roi = df_replicates["sex"] == "male"
df3_roi = df_meta["sex"] == "female"


for sample in df_meta[df_roi]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename ) #reading in the proper data and creating new file
    #then appending the info from the new file to a list to sift through the fpkm values of just the females 
    df_roi2 = df["t_name"] == "FBtr0331261"
    male_Sxl.append(df[df_roi2]["FPKM"].values) #.values comes from np through pandas-it is taking a pandas series structure and converting it to a np structure so matpotlib can understand it-returns just the value without any of the extra names with it. 
for sample in df_meta[df3_roi]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df3 = pd.read_table( filename ) 
    
    df_roi2 = df["t_name"] == "FBtr0331261"
    female_Sxl.append(df3[df_roi2]["FPKM"].values)     

for sample in df_replicates[df2_roi]["sample"]:
    filename2 = ctab_dir + "/" + sample + "/t_data.ctab"
    df2 = pd.read_table(filename2)
    
    df2_roi2 = df2["t_name"] == "FBtr0331261"
    male_Sxl_replicates.append(df2[df2_roi2]["FPKM"].values)
    #male_Sxl_replicates_stages.append(df_replicates["stage"])
    
    #print male_Sxl_replicates
    #print male_Sxl_replicates_stages
    xticks = ("10", "11", "12", "13", "14A", "14B", "14C", "14D")

plt.figure()
plt.title("Sxl male")
#plt.xscale(10,2)
plt.plot(male_Sxl)
plt.plot(female_Sxl)
plt.xticks(range(8), xticks, rotation="vertical")
plt.ylim((0, 150))
plt.scatter(male_Sxl_replicates_stages, male_Sxl_replicates)
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (FPKM)")
plt.savefig("timecourse_replicates2.png")
plt.close()
