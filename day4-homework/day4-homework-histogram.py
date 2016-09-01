#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np

df = pd.read_table(sys.argv[1])
df_roi = df["FPKM"] > 0
df_fpkm = df[df_roi]

fpkm_log = np.log(df_fpkm["FPKM"])


minimum = np.min(fpkm_log)
maximum = np.max(fpkm_log)



plt.figure()
plt.title("Histogram of SRR072893")

plt.hist(fpkm_log, bins= 30, range = [minimum, maximum], normed =True )
plt.legend(loc = "upper right")
plt.ylabel("Frequency")
plt.xlabel("log of FPKM")
plt.savefig("SRR072893 histogram.png")
plt.close()



