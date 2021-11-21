#!/usr/local/bin/python3

import sys
sys.path.insert(1, '../lib')

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

# Here we can validate the accuracy etc.

# Save the model
import pickle
with open('data/model.dat','wb') as file:
    pickle.dump(knn,file)

