#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde


df = pd.read_table(sys.argv[1])

fpkm = df["FPKM"]
density = gaussian_kde(fpkm)
xs = np.linspace(0,140, 1000)
density.covariance_factor = lambda : .25
density._compute_covariance()





plt.figure()
plt.title("FPKM density plot of SRR07893")
plt.plot(xs, density(xs))
plt.ylabel("Density")
plt.xlabel("FPKM")
#plt.hexbin(df["FPKM"] +1, df2["FPKM"]+1) #gives density of points as well
plt.savefig("densityplot.png")
plt.close()