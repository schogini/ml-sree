#!/usr/local/bin/python3

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../lib')

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris = load_iris()
# create X (features) and y (response)
X = iris.data
y = iris.target
# use train/test split with different random_state values
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)

# check classification accuracy of KNN with K=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

X_new = [[3, 5, 4, 2], [5, 4, 3, 2]]
p=knn.predict(X_new)
print(p)

import pickle
with open('data/model.dat','wb') as file:
    pickle.dump(knn,file)

