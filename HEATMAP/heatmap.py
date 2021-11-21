#!/usr/local/bin/python3


import sys
sys.path.insert(1, '../lib')

import matplotlib.pyplot as mp
import pandas as pd
import seaborn as sb
  
#data = pd.read_csv('drive/MyDrive/Colab Notebooks/homeprices2.csv')
data = pd.read_csv('../data/homeprices2.csv')

# prints data that will be plotted
# columns shown here are selected by corr() since
# they are ideal for the plot
print(data.corr())
  
# plotting correlation heatmap
dataplot = sb.heatmap(data.corr(), cmap="YlGnBu", annot=True)
  
# displaying heatmap
mp.show()
