#!/usr/local/bin/python3

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../lib')

from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(solver='liblinear')
logreg.fit(X, y)

p=logreg.predict([[3, 5, 4, 2]])
print(p);

X_new = [[3, 5, 4, 2], [5, 4, 3, 2]]

# predict the response for new observations
p=logreg.predict(X_new)
print(p);

import pickle
with open('data/model.dat','wb') as file:
    pickle.dump(logreg,file)

