#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Principal Component Analysis (PCA)
@author: Mathew Yang
"""

#Libraries needed to run the tool
import numpy as np
np.set_printoptions(suppress=True, precision=5, linewidth=150) #to control what is printed: 'suppress=True' prevents exponential prints of numbers, 'precision=5' allows a max of 5 decimals, 'linewidth'=150 allows 150 characters to be shown in one line (thus not cutting matrices)
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

file_name = 'ind_node_c111.csv'
#data = pd.DataFrame(pd.read_csv(file_name, header=0, index_col=0,delim_whitespace=True))
data = pd.DataFrame(pd.read_csv(file_name, header=0, index_col=None,delim_whitespace=True,
                                usecols=[1,2,3,4,5,6,7,8,9,10,11]))

#normalize data to have range between 0 and 1
#norm_data = preprocessing.normalize(data)
#data.loc[:,:] = norm_data

#Defining X1, X2, and all the data X
X0 = data["time.span"]
X1 = data.switching2
X2 = data.absence2
X3 = data.visiting2
X4 = data.homing2
X5 = data["avg.group.size"]
X6 = data["avg.comm.size"]
X7 = data["avg.stay2"]
X8 = data["max.stay2"]
#Adding classes. First 32 are gSAD, last 32 are healthy.
#Y = data['category']
X = np.column_stack((X0,X1,X2, X3, X4, X5, X6, X7, X8))

"""
#Calculate and show covariance matrix
print("Covariance matrix")
print(np.cov(X, rowvar=0).round(5)) #rowvar=0 means that each column is a variable. Anything else suggest each row is a variable.
print("Here 1") #print to know where you are or to check if a bug exists
a = np.linalg.eigvals(np.cov(X, rowvar=0))
print(a/a.sum()) #To show that percentage variance explained by components is the eigenvalues
print("Here 2")

#Calculate and show correlation coefficients between datasets
print("Correlation Coefficients")
print(np.corrcoef(X, rowvar=0).round(5))
print("")
"""

#Define the PCA algorithm
ncompo = 2
pca = PCA(n_components=ncompo)

#Find the PCA
pcafit = pca.fit(X) #Use all data points since we are trying to figure out which variables are relevant

print("Mean")
print(pcafit.mean_)
print("")
print("Principal Components Results")
print(pcafit.components_)
print("")
print("Percentage variance explained by components")
print(pcafit.explained_variance_ratio_)
print("")
'''
#Plot percentage variance explained by components 
perc = pcafit.explained_variance_ratio_
perc_x = range(1, len(perc)+1)
plt.plot(perc_x, perc, '-.ro')
plt.xlabel('Components')
plt.ylabel('Percentage of Variance Explained')
plt.title('PCA Results')
plt.show()
'''
#In general a good idea is to scale the data
scaler = StandardScaler()
scaler.fit(data)
x=scaler.transform(data)    

pca = PCA()
x_new = pca.fit_transform(x)


def myplot(score,coeff,labels=None):
    xs = score[:,0]
    ys = score[:,1]
    n = coeff.shape[0]
    scalex = 1.0/(xs.max() - xs.min())
    scaley = 1.0/(ys.max() - ys.min())
    gSAD_labels = np.array(['r']*32)
    HC_labels = np.array(['b']*32)
    colors = np.append(gSAD_labels, HC_labels)
    plt.scatter(xs * scalex,ys * scaley, c = colors)
    for i in range(n):
        plt.arrow(0, 0, coeff[i,0], coeff[i,1],color = 'r',alpha = 0.5)
        if labels is None:
            plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, "Var"+str(i+1), color = 'b', ha = 'center', va = 'center')
        else:
            plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, labels[i], color = 'b', ha = 'center', va = 'center')
    plt.tight_layout()
    plt.title('PC1 and PC2')
    plt.legend(labels = ['gSAD','HC'])
    plt.grid('on')

plt.xlim(-1,1)
plt.ylim(-1,1)
plt.xlabel("PC{}".format(1))
plt.ylabel("PC{}".format(2))

#Call the function. Use only the 2 PCs.
mylabels = ["Individual", "observed", "time.span", "switching2", "absence2",
          "visiting2", "homing2", "avg.group.size", "avg.comm.size",
          "avg.stay2", "max.stay2",'category']
myplot(x_new[:,0:2],np.transpose(pca.components_[0:2, :]), mylabels)
plt.savefig("ind_node_PCA_c111.png", dpi=300)
