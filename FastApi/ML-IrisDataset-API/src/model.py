from sklearn.datasets import load_iris
import pandas as pd    
import numpy as np 
from sklearn.linear_model import LinearRegression
import pickle

data = load_iris()


X = data
y = data.target

lr = LinearRegression(X, y)


