#!/usr/bin/env python
from __future__ import division
import sys
import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import leaves_list as leaf
import numpy as np
import itertools
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
from scipy import stats
from scipy.stats import ttest_ind as ttest #ttest_ind_from_stats
import pydendroheatmap as pdh
from scipy.cluster.vq import kmeans2 as kmeans
import matplotlib.pyplot as plt
plt.style.use('ggplot')


df = open(sys.argv[1])
df2 = open(sys.argv[2])

early_stages = []
late_stages = []
cfu = []
mys = []
poly = []
unk = []
gene_names = []
gene_names_position = []
genes = {}

for i, line in enumerate(df):
    fields = line.split("\t")
    #print fields[0] + "\t" + fields[1] + "\t" + fields[5] + "\t" + fields[2] + "\t" + fields[3]
    if i == 0:
        continue
    else:
        cfu.append(fields[1])
        mys.append(fields[5])
        poly.append(fields[2])
        unk.append(fields[3])
        gene_names.append(fields[0])
        gene_names_position.append(i)

genes = dict(itertools.izip(gene_names_position, gene_names))
#genes = {genes}

#print genes


cfu_array = np.array(cfu, dtype = np.float)
mys_array = np.array(mys, dtype = np.float)
average_early = (cfu_array + mys_array)/2
early_stages.append(average_early)

poly_array = np.array(poly, dtype = np.float)
unk_array = np.array(unk, dtype = np.float)
average_late = (poly_array + unk_array)/2
late_stages.append(average_late)

early_stages_array = np.array(early_stages, dtype = np.float)
late_stages_array = np.array(late_stages, dtype = np.float)

#print average_early


#
intensity_ratio = []
# intesity_ratio_list = []
ratio = (early_stages_array/ late_stages_array)
intensity_ratio.append(ratio)
#intensity_ratio = np.array(intensity_ratio).tolist()
drats = []
rat = np.array(intensity_ratio).tolist()
drats.append(rat)


#print len(drats)

# # print intensity_ratio_list
# for i, value in enumerate(drats):
#     if value == 0.0296002034945:
#         print i
#     else:
#         continue

upregulated_genes = []
upregulated_genes_position = []
downregulated_genes = []
downregulated_genes_position = []
leftover_genes = []
leftover_genes_position = []
for position, value in enumerate(np.nditer(intensity_ratio)):
    if value >= 2.0:
        upregulated_genes.append(value)
        upregulated_genes_position.append(position)
    elif value <= 0.5:
        downregulated_genes.append(value)
        downregulated_genes_position.append(position)
    else:
        leftover_genes.append(value)
        leftover_genes_position.append(position)
upregulated_genes_array = np.array(upregulated_genes, dtype = np.float)
downregulated_genes_array = np.array(downregulated_genes, dtype = np.float)

#print downregulated_genes_array
# #
#print upregulated_genes
#print upregulated_genes_position
upregulated_genes_names = []
downregulated_genes_names = []
leftover_genes_names = []


for position, gene in genes.items():
    if position in upregulated_genes_position:
        upregulated_genes_names.append(gene)
    elif position in downregulated_genes_position:
        downregulated_genes_names.append(gene)
    else:
        leftover_genes_names.append(gene)

# early = np.array(average_early).tolist()
# late = np.array(average_late).tolist()

early_vals = []
late_vals = []
gene_titles = []
for i, line in enumerate(df2):
    fields = line.split("\t")
    if i == 0:
        continue
    else:
        early = (fields[1], fields[2])
        late = (fields[3], fields[4])
        gene_titles.append(fields[0])
        early_vals.append(early)
        late_vals.append(late)
  
#print sorted(late_vals)

t = ttest(early_vals, late_vals)
print t
