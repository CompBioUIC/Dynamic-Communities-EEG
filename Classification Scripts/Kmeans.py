#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clustering Analysis
@author: Mathew Yang
"""

#Libraries needed to run the tool
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
from scipy.cluster.hierarchy import dendrogram, linkage #for dendrogram specifically
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing

sns.set(style='darkgrid')

file_name = 'ind_node_c111.csv'
data = pd.DataFrame(pd.read_csv(file_name, header=0, index_col=None, 
                                delim_whitespace=True, 
                                usecols=[4,5,6,7,8,9,10]))

#normalize data to have range between 0 and 1
norm_data = preprocessing.normalize(data)
data.loc[:,:] = norm_data

#Defining X1, X2, and all the data X
#X0 = data["time.span"]
#X1 = data.switching2
X2 = data.absence2
X3 = data.visiting2
X4 = data.homing2
X5 = data["avg.group.size"]
X6 = data["avg.comm.size"]
X7 = data["avg.stay2"]
X8 = data["max.stay2"]

#Class to predict
gSAD_labels = np.array(['1']*5440)
HC_labels = np.array(['0']*5440)
Y = np.append(gSAD_labels, HC_labels)
X = np.column_stack((X2, X3, X4, X5, X6, X7, X8, Y))

#Standardize
pca = decomposition.PCA(n_components=2)
x_std = StandardScaler().fit_transform(X)
X=pca.fit_transform(x_std)


#Try out different types of hierarchical clustering 
fig, axes = plt.subplots(3,3, sharex= 'col', sharey= 'row')
k = [2,3,6]
for j in range(len(k)):
    for i in range(3):
        
        #Define which hierarchical clustering algorithm to use and fit it
        linkage_types = ['ward', 'average', 'complete']
        Y_hierarchy = AgglomerativeClustering(linkage=linkage_types[j], n_clusters=k[i])
        Y_hierarchy.fit(X)
        Y_hierarchy_labels = Y_hierarchy.labels_
        Y_hierarchy_silhouette = metrics.silhouette_score(X, Y_hierarchy_labels, metric='sqeuclidean')
        #print("Silhouette for Hierarchical Clustering: {0}".format(Y_hierarchy_silhouette))
        #print("Hierarchical Clustering: {0}".format(Y_hierarchy_labels))
        
        #Define figure
        colormap = np.array(['white','black', 'blue', 'red', 'orange', 'green', 'brown', 'yellow', 'magenta', 'cyan']) #Define colors to use in graph - could use c=Y but colors are too similar when only 2-3 clusters
        
        #Plot Hierarchical clustering results
        #plt.title("Hierarchical Clustering")
        axes[j,i].scatter(X[:, 0], X[:, 1], c=colormap[Y_hierarchy_labels])
        axes[j,i].annotate("s = " + str(Y_hierarchy_silhouette.round(2)), xy=(1, 0), xycoords='axes fraction', horizontalalignment='right', verticalalignment='bottom')
axes[0,0].set_title('Clusters: 2')
axes[0,1].set_title('Clusters: 3')
axes[0,2].set_title('Clusters: 6')
axes[0,0].set_ylabel('Ward')
axes[1,0].set_ylabel('Average')
axes[2,0].set_ylabel('Complete')

fig.set_figheight(10)
fig.set_figwidth(10)

#Save plots
fig.savefig('ind_node_Hierarchical_c111.png', dpi=300)

#Define which KMeans algorithm to use and fit it
Y_Kmeans = KMeans(n_clusters = 3)
Y_Kmeans.fit(X)
Y_Kmeans_labels = Y_Kmeans.labels_
Y_Kmeans_silhouette = metrics.silhouette_score(X, Y_Kmeans_labels, metric='sqeuclidean')
print("Silhouette for Kmeans: {0}".format(Y_Kmeans_silhouette))
print("Results for Kmeans: {0}".format(Y_Kmeans_labels))

#Plot KMeans results
fig1 = plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=colormap[Y_Kmeans_labels])
plt.title("KMeans")
plt.annotate("s = " + str(Y_Kmeans_silhouette.round(2)), xy=(1, 0), xycoords='axes fraction', horizontalalignment='right', verticalalignment='bottom')
       
#Save plots
fig1.savefig('ind_node_KMeans_c111.png', dpi=300)
'''
#Using Scipy to draw dendrograms - for more info, see: https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/
linkage_types = ['ward', 'average', 'complete']
Z = linkage(X, linkage_types[1])
dendro = plt.figure()
dendro.set_size_inches(12,8)
dendrogram(Z, labels=np.asarray(Y), leaf_rotation=90)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Index from Dataframe')
plt.ylabel('Distance')
plt.savefig('EEG_dendro.png', dpi=300)
plt.show()

dendro.savefig('Dendrogram.png', dpi=300)
'''