#!/usr/local/bin/python3

import sys
#insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../lib')

from sklearn.linear_model import LogisticRegression
import pickle

with open('data/model.dat','rb') as file:
    mp = pickle.load(file)

X_new = [[3, 5, 4, 2], [5, 4, 3, 2]]
p=mp.predict(X_new)
print(p);
