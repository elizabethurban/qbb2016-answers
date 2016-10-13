#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
#from pandas import DataFrame
#from scipy.stats import uniform
#from scipy.stats import randint


df_name = sys.argv[1]
for df_name in sys.argv[1:]:
    df = open(df_name)

p_values_list = []
log_p_values_list = []    

for i, line in enumerate(df):
    if i == 0:
        continue
    else:
        fields = line.rstrip("\n\r").split()
        p_value = fields[8]
        p_values_list.append(p_value)
        #print p_value
        log_p_value = -np.log10(float(p_value))
        log_p_values_list.append(log_p_value)
        
y = np.array(log_p_values_list)
x = np.array(range(len(log_p_values_list)))
threshold = -np.log10(10** -5)
loy= y[y < threshold]
hiy= y[y >= threshold]
lox = x[y < threshold]
hix = x[y >= threshold]

treatment = df_name.split(".")[1]            
            
plt.figure()
plt.title("manhattan plot of " + treatment) 
plt.axhline(5)
plt.scatter(lox, loy, color= 'r', edgecolor= "none")
plt.scatter(hix, hiy, color= 'b', edgecolor= "none")
plt.xlabel("snp")
plt.ylabel("-log10 p-value")
#plt.show()
plt.savefig(treatment + ".png")
        
    

            #print log_p_value
    


#make the -log_ten(pvalue)