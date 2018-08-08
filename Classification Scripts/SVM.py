#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Support Vector Machine
@author: Mathew Yang
"""

#Libraries needed to run the tool
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score #New element this week!K-cross validation
import matplotlib.pyplot as plt
from sklearn import preprocessing

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

X = np.column_stack((X2, X3, X4, X5, X6, X7, X8))

#Adding classes. First 32 are gSAD, last 32 are healthy.
gSAD_labels = np.array(['gSAD']*5440)
HC_labels = np.array(['HC']*5440)
Y = np.append(gSAD_labels, HC_labels)


#Using Built in train test split function in sklearn
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3)

total_scores=list()
total_Y_predict = list()

#Setting up SVM and fitting the model with training data
ker = ['linear', 'poly', 'rbf', 'sigmoid']
SVM_result = list()
for i in range(len(ker)):
    vector = svm.SVC(kernel=ker[i], degree=2) #degree is only relevant for the 'poly' kernel

    #Cross Validation (CV) process
    scores = cross_val_score(vector, X_train, Y_train, cv=5)
    print(ker[i].upper(), "Accuracy: {0} (+/- {1})".format(scores.mean().round(2), (scores.std() * 2).round(2)))
    print("")
    total_scores.append(scores)
    
    #Fit final SVC
    vector.fit(X_train, Y_train)
    
    if vector.kernel == 'linear':
        c = vector.coef_
        print("Coefficients:")
        print(c)
        print("This means the linear equation is: y = -" + str(c[0][0].round(2)) + "/" + str(c[0][1].round(2)) + "*x + " + str(vector.intercept_[0].round(2)) + "/" + str(c[0][1].round(2)))
        print("")
    
    #Run the model on the test (remaining) data and show accuracy
    Y_predict = vector.predict(X_test)
    total_Y_predict.append(Y_predict)
'''

#Adapted from http://ogrisel.github.io/scikit-learn.org/sklearn-tutorial/auto_examples/tutorial/plot_knn_iris.html
# Plot the decision boundary. For that, we will asign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
x_min, x_max = X[:,0].min() - .5, X[:,0].max() + .5 #Defines min and max on the x-axis
y_min, y_max = X[:,1].min() - .5, X[:,1].max() + .5 #Defines min and max on the y-axis
h = (x_max - x_min)/300 # step size in the mesh to plot entire areas
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h)) #Defines meshgrid
Z = vector.predict(np.c_[xx.ravel(), yy.ravel()]) #Uses the calibrated model knn and running on "fake" data in meshgrid

# Put the result into a color plot
Z = Z.reshape(xx.shape) #Reshape for matplotlib
plt.figure(1) #create one figure
plt.set_cmap(plt.cm.Paired) #Picks color for 
plt.pcolormesh(xx, yy, Z) #Plot for the data

# Plot also the training points
colormap = np.array(['white', 'black']) #BGive two colors based on values of 0 and 1 from HW6_Data
plt.scatter(X[:,0], X[:,1],c=colormap[Y]) #Plot the data as a scatter plot, note that the color changes with Y.

plt.xlabel("X1") #Adding axis labels
plt.ylabel("X2")
plt.xlim(xx.min(), xx.max()) #Setting limits of axes
plt.ylim(yy.min(), yy.max())
plt.xticks(()) #Removing tick marks
plt.yticks(())
plt.savefig(file_name + '_plot.png') #Saving the plot

plt.show() #Showing the plot
'''