#!/usr/local/bin/python3
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../lib')


import pandas as pd
import numpy as np
from sklearn import linear_model

import warnings
warnings.simplefilter("ignore")

import matplotlib.pyplot as plt

df = pd.read_csv('data/homeprices.csv')
print(df);


#%matplotlib inline
plt.xlabel('area')
plt.ylabel('price')
plt.scatter(df.area,df.price,color='red',marker='+')
plt.show()


new_df = df.drop('price',axis='columns')
new_df

price = df.price
price

reg = linear_model.LinearRegression()
reg.fit(new_df,price)

print(reg.predict([[3300]]));

import pickle
with open('data/model.dat','wb') as file:
    pickle.dump(reg,file)

