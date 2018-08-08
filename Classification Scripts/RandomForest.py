#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Decision Tree Learning
@author: Mathew Yang
"""

#Libraries needed to run the tool
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn import preprocessing

file_name = 'avg_c111.csv'
'''
data = pd.DataFrame(pd.read_csv(file_name, header=0, index_col=None, 
                                delim_whitespace=True, 
                                usecols=[4,5,6,7,8,9,10]))
'''
data = pd.DataFrame(pd.read_csv(file_name, header=0, index_col=0, delim_whitespace=True))

#normalize data to have range between 0 and 1
#norm_data = preprocessing.normalize(data)
#data.loc[:,:] = norm_data

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
Y = data['category']

#Using Built in train test split function in sklearn
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

#Fit the Decision tree
crit_choice = ['gini', 'entropy']
crit = crit_choice[0]
cross_val_number = 10
decitree = tree.DecisionTreeClassifier(criterion=crit)
randfor = RandomForestClassifier(n_estimators = 10, criterion=crit)

#Cross Validation (CV) process
decitree_scores = cross_val_score(decitree, X_train, Y_train, cv=cross_val_number)
randfor_scores = cross_val_score(randfor, X_train, Y_train, cv=cross_val_number)
print("Decision Tree Accuracy: {0} (+/- {1})".format(decitree_scores.mean().round(2), (decitree_scores.std() * 2).round(2)))
print("Random Forest Accuracy: {0} (+/- {1})".format(randfor_scores.mean().round(2), (randfor_scores.std() * 2).round(2)))
print("")

#Training final trees
decitree.fit(X_train, Y_train) #Decision Tree
randfor.fit(X_train, Y_train) #Random Forest

#Export tree properties in graph format
#if needed, install Graphviz from http://www.graphviz.org/
#alternatively, copy and paste the text from the .dot file to http://www.webgraphviz.com/
tree.export_graphviz(decitree, out_file= file_name + '.dot')

decitree_predict = decitree.predict(X_test)
decitree_score = metrics.accuracy_score(decitree_predict, Y_test)

randfor_predict = randfor.predict(X_test)
randfor_score = metrics.accuracy_score(randfor_predict, Y_test)

print("Decision Tree")
print(decitree_predict)
print(decitree_score)
print("")
print("Random Forest")
print(randfor_predict)
print(randfor_score)
print("")
