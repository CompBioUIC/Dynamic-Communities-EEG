# -*- coding: utf-8 -*-
"""
@author: Mathew Yang
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

file_name = 'avg_c111.csv'
data = pd.DataFrame(pd.read_csv(file_name, header=0, index_col=None, 
                                delim_whitespace=True, 
                                usecols=[4,5,6,7,8,9,10]))

"""Healthy vs gSAD comparisons"""
'''Only normalize last 4 columns: avg.group.size, avg.comm.size, avg.stay2, max.stay2'''
norm_data = preprocessing.normalize(data)
norm = pd.DataFrame(norm_data)
#data.loc[:,:] = norm_data

data['avg.group.size'] = norm[3]
data['avg.comm.size'] = norm[4]
data['avg.stay2'] = norm[5]
data['max.stay2'] = norm[6]

#Split dataframe into two based on conditions
HC = data[:160].mean()
gSAD=data[160:].mean()

#Pairplot

#Barplot
#healthy_height = healthy[:,1].mean()
#gSAD_height = gSAD[:,1].mean()
plt.figure()
ax = HC.plot(kind='bar', color='b',width=0.2, position=0)
gSAD.plot(kind='bar', ax=ax, color='r',width=0.2, position=1)
plt.ylabel('Normalized Value')
plt.title('Average CommDy Statistics with Cost 111')
plt.legend(['HC','gSAD'])
plt.tight_layout()
plt.savefig('avg_c111_stats.png', dpi=300)
