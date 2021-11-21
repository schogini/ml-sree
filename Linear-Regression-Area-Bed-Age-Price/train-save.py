#!/usr/local/bin/python3

# https://github.com/codebasics/py/blob/master/ML/2_linear_reg_multivariate/2_linear_regression_multivariate.ipynb

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../lib')


import pandas as pd
import numpy as np
from sklearn import linear_model

import warnings
warnings.simplefilter("ignore")

import matplotlib.pyplot as plt

df = pd.read_csv('data/homeprices2.csv')
print(df);

df.bedrooms = df.bedrooms.fillna(df.bedrooms.median())

reg = linear_model.LinearRegression()
reg.fit(df.drop('price',axis='columns'),df.price)

print(reg.predict([[3000, 3, 40]]))


import pickle
with open('data/model.dat','wb') as file:
    pickle.dump(reg,file)

