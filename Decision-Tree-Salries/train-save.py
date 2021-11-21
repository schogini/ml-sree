#!/usr/local/bin/python3

# https://github.com/codebasics/py/blob/master/ML/7_logistic_reg/7_logistic_regression.ipynb

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../lib')

import pandas as pd
from matplotlib import pyplot as plt
# %matplotlib inline
df = pd.read_csv("data/insurance_data.csv")
print(df.head());

plt.scatter(df.age,df.bought_insurance,marker='+',color='red')
plt.show();

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df[['age']],df.bought_insurance,train_size=0.8)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(X_train, y_train)

y_predicted = model.predict(X_test)

print(model.predict_proba(X_test))
print(model.score(X_test,y_test))
print(y_predicted)


import pickle
with open('data/model.dat','wb') as file:
    pickle.dump(model,file)

