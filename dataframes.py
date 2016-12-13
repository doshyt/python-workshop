# -*- coding: utf-8 -*-
"""
Getting to know Dataframes

More:
    http://pandas.pydata.org/pandas-docs/stable/dsintro.html
"""

import pandas as pd
import numpy as np

print("Create an empty dataframe")
df = pd.DataFrame()
df

print("Populate random matrix 10x5 and name columns")
df = pd.DataFrame(np.random.randn(10, 5),
                  columns=['a', 'b', 'c', 'd', 'e'])
df

print("Get all column content")
df['a']

print("Get all 1-st row content")
df.iloc[[0]]

print("Get all 10-th row content")
df.iloc[[9]]

print("Create a dataframe with indexes")
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
df.index
df.columns

print("Access a column or an indexed row")
df['one']
df.loc['c']
df.iloc[2]

print("Read dataframe from file")
animals_data = pd.read_csv("C:\dev\python-workshop\species.csv", 
                           index_col=0,
                           parse_dates=True,
                           dayfirst=True)
animals_data

print("Select only bears")
bears_data = animals_data[animals_data['species']=='bear']
bears_data

print("Count how many bears in total were seen")
sum(bears_data['count'])

print("TASK: Get all species seen on 11/01/15")

print("Group by a column")
animals_data.groupby(by='species')

animals_data.groupby(by='species').sum()
animals_data.groupby(by='field')['count'].sum()
animals_data.groupby(by='species')['count'].mean()

print("How many species of each type were seen on the field A")
animals_data[animals_data['field']=='A'].groupby(by='species')['count'].sum()

print("TASK: what about dates? Get total count of species for each particular day")

print("Visualize counts per day for bear")
bears_data.plot()
print("Fields are messing the plot")
bears_data_flatten = bears_data.groupby(by=bears_data.index)['count'].sum()    
bears_data_flatten

bears_data_flatten.plot()

print("Plot bears to wolves count on each day")
wolves_data = animals_data[animals_data['species']=='wolf']
wolves_data_flatten = wolves_data.groupby(by=wolves_data.index)['count'].sum()    

print("First, try to run them one by one, not as a block")
import matplotlib.pyplot as plt
plt.figure()
bears_data_flatten.plot()
wolves_data_flatten.plot()
