from sklearn.datasets import load_iris
import pandas as pd    
import numpy as np 
from sklearn.tree import DecisionTreeClassifier
import pickle

iris = load_iris()


X = iris.data
y = iris.target


dt = DecisionTreeClassifier().fit(X, y)

with open('ML-IrisDataset-API/src/model.pkl', 'wb') as file:
    pickle.dump(dt, file)