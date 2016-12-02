#!/usr/bin/env python

import sys
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import leaves_list as leaf
import numpy as np
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
import pydendroheatmap as pdh
from scipy.cluster.vq import kmeans2 as kmeans
import matplotlib.pyplot as plt
plt.style.use('ggplot')
# try: import cPickle as pickle
# except: import pickle

cell_type = []
number_array_list = []
gene_names = []

df = open(sys.argv[1])
for i, line in enumerate(df):
    fields = line.split("\t")
    gene_names.append(fields[0])
    if i == 0:
        cell_type = fields[1:]
    else:
        number_array_list.append([float(x) for x in fields[1:]])
        


value_array = np.array(number_array_list)
    
        
#print value_array
#print cell_type
#print gene_names


Z = linkage(value_array)
leaves = leaf(Z)
#print leaves

transposed_linkage_matrix = np.transpose(value_array)
K = linkage(transposed_linkage_matrix)
leaves_flip = leaf(K)
#print leaves_flip
#print K
#print cell_type

#print transposed_linkage_matrix

# calculate full dendrogram
plt.figure()
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('cell type')
plt.ylabel('distance')
#tick_names = ["CFU", "poly", "unk", "mys", "int", "mid_n"]

dendrogram(K, labels=cell_type)
#plt.xticks(range(len(tick_names)), tick_names)
plt.tight_layout()
plt.savefig("cell_type_clustering")
plt.close()

plt.figure()
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Gene name')
plt.ylabel('distance')
#tick_names = ["CFU", "poly", "unk", "mys", "int", "mid_n"]

dendrogram(Z, labels=gene_names)
#plt.xticks(range(len(tick_names)), tick_names)
plt.tight_layout()
plt.savefig("gene_clustering")
plt.close()


value_array = value_array[leaves, : ]
value_array = value_array[ :, leaves_flip]



heatmap = pdh.DendroHeatMap(heat_map_data = value_array, left_dendrogram= Z, top_dendrogram= K)
heatmap.title = 'gene expression by cell type'
#heatmap.column_labels = ['CFU', 'poly', 'unk', 'mys', 'int', 'mid']
heatmap.export('heatmap of gene expression.png')
plt.close()

centers, kmeans_cluster = kmeans(value_array[:,[0,2]], 8, iter = 10, thresh = 1e-05, minit = 'random')
# print kmeans_cluster

color_vals = []

for label in kmeans_cluster:
    if label == 0:
        colors = 'blue'
    elif label == 1:
        colors = 'red'
    elif label == 2:
        colors = 'purple'
    elif label == 3:
        colors = 'green'
    elif label == 4:
        colors = 'yellow'
    elif label == 5:
        colors = 'black'
    elif label == 6:
        colors = "orange"
    else:
        colors = "cyan" 
    color_vals.append(colors)
    
plt.figure()                          # Create a new blank canvas
plt.title("kmeans clustering of CFU and poly")   # Add a title to the top, spanning two lines
plt.scatter(value_array[:, 2], value_array[:, 0], c=color_vals) 
                   # ...Create a scatter plot
		# x[Y==i],                      # ... ... of x
#         y[Y==i],                      # ... ... vs y
#         c=colors[i],                  # ... ... set the color of these points
#         marker=ms[i],                 # ... ... and pick the marker style
#         label=species[i]              # ... ... finally, label the points of this set with the species name
#         )
#plt.legend(loc='upper left')          # Add a legend to the top left
plt.xlabel('poly')                 # label the x-axis
plt.ylabel('CFU')                 # label the y-axis
#plt.show()
plt.savefig("kmeans_cluster.png")      # Save the figure
plt.close()                           # Close the canvas

#df = pd.read_table(sys.argv[1])
# early_stages = []
# late_stages = []
# for i, line in enumerate(df):
#     fields = line.split("\t")
#     early_stages.append(fields[0,4])
#     late_stages.append(fields[1,2])
# print early_stages
    
