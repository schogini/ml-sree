#!/usr/local/bin/python3

import sys
#insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../lib')

import warnings
# from sklearn.exceptions import DataConversionWarning
# warnings.filterwarnings(action='ignore', category=DataConversionWarning)

import pickle

with open('data/model.dat','rb') as file:
    mp = pickle.load(file)

# with warnings.catch_warnings():
#     warnings.simplefilter("ignore")
#     print(mp.predict([[3300]]));

warnings.simplefilter("ignore")
print(mp.predict([[3300]]));

print(mp.predict([[sys.argv[1]]]));
