#!/usr/local/bin/python3

import sys
#insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../lib')

import warnings
warnings.simplefilter("ignore")

# from sklearn.linear_model import LogisticRegression
import pickle

with open('data/model.dat','rb') as file:
    mp = pickle.load(file)


p=mp.predict([[sys.argv[1]]])
print(p);
