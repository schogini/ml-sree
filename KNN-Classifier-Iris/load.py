#!/usr/local/bin/python3

import sys
sys.path.insert(1, '../lib')

import pickle

with open('data/model.dat','rb') as file:
    model = pickle.load(file)

params = sys.argv[1]
params = params.split(',')

X=list(map(int, params))

print(model.predict([X]))
