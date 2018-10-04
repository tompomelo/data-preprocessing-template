# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 23:29:15 2018

@author: tomst
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values