import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statsmodels as sm
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

nhanes1314 = pd.read_csv('Nhanes_2013_2014.csv')
nhanes1112 = pd.read_csv('Nhanes_2011_2012.csv')
nhanes0910 = pd.read_csv('Nhanes_2009_2010.csv')
nhanes0708 = pd.read_csv('Nhanes_2007_2008.csv')
nhanes0506 = pd.read_csv('Nhanes_2005_2006.csv')
