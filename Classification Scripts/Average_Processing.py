# -*- coding: utf-8 -*-
"""
@author: Mathew Yang
"""

'''This python script takes all the text files that are returned from running the
CommDy algorithm and the Rstatistics script and converts it into an easier format
for data analysis.

INPUT = 64 patients, 160 rows each.
OUTPUT = 320 lines of averaged data
'''

import pandas as pd
import numpy as np
import glob
import csv
import fnmatch

#Start by writing the headers to data
headers = ["Individual", "observed", "time.span", "switching2", "absence2",
          "visiting2", "homing2", "avg.group.size", "avg.comm.size",
          "avg.stay2", "max.stay2"]

with open('avg_c111.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter = ' ')
    spamwriter.writerow(headers)
    
#start writing to data
for file in glob.glob("*c111.txt"):
    temp = pd.read_csv(file, header = 0, index_col=0, sep = ' ')

    data = temp.mean() # we write the mean of 32 columns to the .csv file
        
    with open('avg_c111.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter = ' ')
            spamwriter.writerow(data)
            
            """
    if fnmatch.fnmatch(file, 'theta_PSAD*'): #add gSAD label to those with PSAD in filename
        labels = pd.DataFrame(np.array(['gsad']*(len(temp)+1)))
        temp = temp.join(labels)
    else: #otherwise label as healthy
        labels = pd.DataFrame(np.array(['hc']*(len(temp)+1)))
        temp = temp.join(labels)
        """