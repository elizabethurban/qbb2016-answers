#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn.decomposition import PCA

df = pd.read_table(sys.argv[1], sep=" ", header = None )
# print df
# for line in df:
#     fields = line.rstrip("\r\n").strip(" ")

#print df[2]

plt.figure()
plt.title("PCA") 
plt.scatter(df[2], df[3])
plt.xlabel("PCA1")
plt.ylabel("PCA2")
#plt.show()
plt.savefig("PCAyeast")
