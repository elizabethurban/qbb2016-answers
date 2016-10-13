#!/usr/bin/env python

from __future__ import division
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')


allelefrequency = []

df = open(sys.argv[1])

for line in df:
    if line[0] == "#":
        continue
    else:
        fields = line.rstrip("\n\r").split("\t")[9:]
        row = [int(x) for x in fields]
        frequency = (sum(row)/len(row))
        allelefrequency.append(frequency)
        
#min = np.min(allelefrequency)
#max= np.max(allelefrequency)
    
#print allelefrequency
plt.figure()
plt.title("Allele Frequency")
plt.hist(allelefrequency, bins= 30)
plt.xlabel("Frequency")
plt.ylabel("number of snps")
plt.savefig("allelefrequency_of_yeast_data")