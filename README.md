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

#Merged Dataset

# Find all unique columns across datasets
all_cols = set(nhanes1314.columns) | set(nhanes1112.columns) | set(nhanes0910.columns) | set(nhanes0708.columns) | set(nhanes0506.columns)

# Find common columns
common_cols = set(nhanes1314.columns) & set(nhanes1112.columns) & set(nhanes0910.columns) & set(nhanes0708.columns) & set(nhanes0506.columns)

# Find extra columns
extra_cols = all_cols - common_cols

# Convert common_cols to a list
common_cols_list = list(common_cols)

# Merge all datasets on common columns
merged_nhanes = pd.concat([nhanes1314[common_cols_list], nhanes1112[common_cols_list], nhanes0910[common_cols_list], nhanes0708[common_cols_list], nhanes0506[common_cols_list]], ignore_index=True)

len(merged_nhanes.columns)
# Remove all columns that start with 'DRD' except 'DRDINT'
columns_to_drop = [col for col in merged_nhanes.columns if col.startswith('DRD') and col != 'DRDINT']
columns_to_drop_1 = [col for col in merged_nhanes.columns if col.startswith('RHQ')]
columns_to_drop_2 = [col for col in merged_nhanes.columns if col.startswith('RHD')]

merged_nhanes.drop(columns=columns_to_drop, inplace=True)
merged_nhanes.drop(columns=columns_to_drop_1, inplace=True)
merged_nhanes.drop(columns=columns_to_drop_2, inplace=True)

len(merged_nhanes.columns)
