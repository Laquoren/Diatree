import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statsmodels as sm
import sklearn
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

# Remove all columns that start with 'DRD' except 'DRDINT'
columns_to_drop = [col for col in merged_nhanes.columns if col.startswith('DRD') and col != 'DRDINT']
columns_to_drop_1 = [col for col in merged_nhanes.columns if col.startswith('RHQ')]
columns_to_drop_2 = [col for col in merged_nhanes.columns if col.startswith('RHD')]

merged_nhanes.drop(columns=columns_to_drop, inplace=True)
merged_nhanes.drop(columns=columns_to_drop_1, inplace=True)
merged_nhanes.drop(columns=columns_to_drop_2, inplace=True)

len(merged_nhanes.columns)

# List of columns to be removed. both some extra cols and some common cols. 

columns_to_remove = ['DBQ095Z', 'DBD100', 'DRQSPREP', 'DR1STY', 'DR2STY', 'DR1SKY', 'DR2SKY', 'DRQSDIET', 
    'DRQSDT1', 'DRQSDT2', 'DRQSDT3', 'DRQSDT4', 'DRQSDT5', 'DRQSDT6', 'DRQSDT7', 'DRQSDT8', 
    'DRQSDT9', 'DRQSDT10', 'DRQSDT11', 'DRQSDT12', 'DRQSDT91', 'DR1_300', 'DR1_320Z', 'DR2_320Z', 
    'DR1_330Z', 'DR2_330Z', 'DR1BWATZ', 'DR2BWATZ', 'DR1TWS', 'DR2TWS', 'DRD340', 'DRD350A', 
    'DRD350B', 'DRD350C', 'DRD350D', 'DRD350E', 'DRD350F', 'DRD350G', 'DRD350H', 'DRD350I', 
    'DRD350J', 'DRD350K', 'DRD350AQ', 'DRD350BQ', 'DRD350CQ', 'DRD350DQ', 'DRD350EQ', 'DRD350FQ', 
    'DRD350GQ', 'DRD350HQ', 'DRD350IQ', 'DRD350JQ', 'DRD350KQ', 'DRD360', 'DRD370A', 'DRD370B', 
    'DRD370C', 'DRD370D', 'DRD370E', 'DRD370F', 'DRD370G', 'DRD370H', 'DRD370I', 'DRD370J', 
    'DRD370K', 'DRD370L', 'DRD370M', 'DRD370N', 'DRD370O', 'DRD370P', 'DRD370Q', 'DRD370R', 
    'DRD370S', 'DRD370T', 'DRD370U', 'DRD370V', 'DRD370AQ', 'DRD370BQ', 'DRD370CQ', 'DRD370DQ', 
    'DRD370EQ', 'DRD370FQ', 'DRD370GQ', 'DRD370HQ', 'DRD370IQ', 'DRD370JQ', 'DRD370KQ', 'DRD370LQ', 
    'DRD370MQ', 'DRD370NQ', 'DRD370OQ', 'DRD370PQ', 'DRD370QQ', 'DRD370RQ', 'DRD370SQ', 'DRD370TQ', 
    'DRD370UQ', 'DRD370VQ', 'SDDSRVYR', 'SDMVPSU', 'SDMVSTRA', 'WTINT2YR', 'WTMEC2YR', 'WTSAF2YR', 
    'DMQMILIZ', 'DMQADFC', 'DMDBORN4', 'DMDCITZN', 'DMDYRSUS', 'SIALANG', 'SIAPROXY', 'SIAINTRP', 
    'FIALANG', 'FIAPROXY', 'FIAINTRP', 'MIALANG', 'MIAPROXY', 'MIAINTRP', 'AIALANGA', 'INDHHIN2', 
    'INDFMIN2', 'INDFMPIR', 'HUQ010', 'HUQ020', 'HUQ030', 'HUQ041', 'HUQ051', 'HUQ061', 'HUQ071', 
    'HUD080', 'HUQ090', 'HOD050', 'HOQ065', 'WTDRD1', 'WTDR2D', 'DR1DRSTZ', 'DR2DRSTZ', 'DR1EXMER', 'DR2EXMER', 'DRABF', 'DRDINT', 
    'DR1DBIH', 'DR2DBIH', 'DR1DAY', 'DR2DAY', 'DR1LANG', 'DR2LANG', 'DR1MNRSP', 'DR2MNRSP', 
    'DR1HELPD', 'DR2HELPD']

# Count columns before removal
initial_col_count = len(merged_nhanes.columns)

# Remove specified columns
merged_nhanes = merged_nhanes.drop(columns=columns_to_remove, errors='ignore')

# Function to drop columns where more than 85% of values are missing
def drop_sparse_columns(df, threshold=0.85):
    missing_fraction = df.isna().mean()  # Calculate % of missing values per column
    sparse_cols = missing_fraction[missing_fraction >  threshold].index.tolist()  # Identify columns above threshold
    print(f"Columns Removed (>{threshold*100}% missing): {sparse_cols}\n")
    return df.drop(columns=sparse_cols)

merged_nhanes = merged_nhanes.dropna(axis=1, thresh=len(merged_nhanes) * 0.25)

print("0th check", len(merged_nhanes))

len(merged_nhanes.columns)
merged_nhanes['DIQ010'] = merged_nhanes['DIQ010'].dropna()
print("final check", len(merged_nhanes))
merged_nhanes

# Calculate the threshold for dropping rows
threshold = len(merged_nhanes.columns) * 0.2
	# DROPS to 44323 when 0.5, lost 6642/50965
	# DROPS to 45503 when 0.2, lost 5462/50965

# Drop rows with more than 50% missing values
merged_nhanes = merged_nhanes.dropna(thresh=threshold)

# Drop all rows with NA values in the 'DIQ170' column
merged_nhanes = merged_nhanes.dropna(subset=['DIQ170'])
# DROPS to 29430. lost 14893/50965. CANNOT REDUCE

# Function to determine if a column contains only 0, 1, or empty values
def is_binary_or_empty(col):
    unique_values = col.dropna().unique()
    return set(unique_values).issubset({0, 1})

# Function to determine if a column contains only whole numbers
def is_whole_number(col):
    return col.dropna().apply(float.is_integer).all()

# Fill missing values with the mean or median of each column
def fill_missing_values(col):
    if is_binary_or_empty(col):
        if col.dropna().nunique() == 1 and col.dropna().iloc[0] == 1:
            return col.fillna(0)
        return col.fillna(col.median())
    else:
        mean_value = col.mean()
        if is_whole_number(col):
            mean_value = round(mean_value)
        return col.fillna(mean_value)
    
# Apply the fill_missing_values function to each column
merged_nhanes = merged_nhanes.apply(fill_missing_values, axis=0)
merged_nhanes

#Z score
def z_score_conversion(df):
    df_normalized = df.apply(lambda col: (col - col.mean()) / col.std(), axis=0)
    df_normalized['DIQ170'] = df['DIQ170']  # Restore original DIQ170 values
    return df_normalized

merged_nhanes = z_score_conversion(merged_nhanes)

# Demographic + Diabetes Data
# Select demographic columns (assuming demographic columns start with 'DM')
demographic_cols = [col for col in merged_nhanes.columns if col.startswith('DM')]
# select diabetes columns (assuming demographic columns start with 'DI')
diabetes_cols = [col for col in merged_nhanes.columns if col.startswith('DI')]
# select diabetes + demographic columns 
demo_diabetes_cols = demographic_cols + diabetes_cols

# Create a correlation matrix for the demographic data
demographic_data = merged_nhanes[demographic_cols]
# for diabetes data
diabetes_data = merged_nhanes[diabetes_cols]
# for diabetes and demographic data
demo_diabetes_data = merged_nhanes[demo_diabetes_cols]

correlation_matrix_demographic = demographic_data.corr()
correlation_matrix_diabetes = diabetes_data.corr()
correlation_matrix_demo_diabetes = demo_diabetes_data.corr()

# Generate heatmaps
# heatmap for demographic data only
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix_demographic, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Demographic Data')
plt.show()

# heatmap for diabetes data only
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix_diabetes, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Diabetes Data')
plt.show()

# heatmap for demographic and diabetes data
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix_demo_diabetes, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Demographic and Diabetes Data')
plt.show()

# Physical Measurements and Diabetes Data
# Physical Measurments only 
physical_measurments_cols = [col for col in merged_nhanes.columns if col.startswith('BM')]
#dietary_nutrient_intake = [col for col in merged_nhanes.columns if col.startswith('DR1TC')]

# Physical Measurements and Diabetes Data
physical_measurments_diabetes_cols = physical_measurments_cols + diabetes_cols

# Creating a correlation matrix for Physical Measurements data
# Physical Measurments only 
physical_measurments_data = merged_nhanes[physical_measurments_cols]
correlation_matrix_physical_measurements = physical_measurments_data.corr()
# Both Physical and Diabetes Data
physical_measurments_diabetes_data = merged_nhanes[physical_measurments_diabetes_cols]
correlation_matrix_physical_measurements_diabetes = physical_measurments_diabetes_data.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix_physical_measurements, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Physical Measurements Data')
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix_physical_measurements_diabetes, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Physical Measurements and Diabetes Data')
plt.show()

# Laboratory Values and Diabetes Data
# Laboratory Values only 
laboratory_values_cols = [col for col in merged_nhanes.columns if col.startswith('LB')]
# Both Laboratory and Diabetes Data
laboratory_values_diabetes_cols = laboratory_values_cols + diabetes_cols

# Creating a correlation matrix for Laboratory Values data
# Laboratory Values only
laboratory_values_data = merged_nhanes[laboratory_values_cols]
correlation_matrix_laboratory_values = laboratory_values_data.corr()
# Both Laboratory and Diabetes Data
laboratory_values_diabetes_data = merged_nhanes[laboratory_values_diabetes_cols]
correlation_matrix_laboratory_values_diabetes = laboratory_values_diabetes_data.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix_laboratory_values, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Laboratory Values Data')
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix_laboratory_values_diabetes, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Laboratory Values and Diabetes Data')
plt.show()

# Laboratory Values and Physical Measurements data
laboratory_values_physical_measurements_cols = laboratory_values_cols + physical_measurments_cols

# Creating a correlation matrix for Laboratory Values and Physical Measurements data
laboratory_values_physical_measurements_data = merged_nhanes[laboratory_values_physical_measurements_cols]
correlation_matrix_laboratory_values_physical_measurements = laboratory_values_physical_measurements_data.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix_laboratory_values_physical_measurements, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Laboratory Values and Physical Measurements Data')
plt.show()

glucose_cols = ['LBXGLU', 'LBXTC']
adjusted_physical_measurments_cols = ['BMXWT', 'BMXBMI', 'BMXHT', 'BMXWAIST']

input_cols = glucose_cols + adjusted_physical_measurments_cols
output_col = 'DIQ170'

print(input_cols)

X = merged_nhanes[input_cols]
y = merged_nhanes[output_col]

# Split the data into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(y_pred)

np.savetxt('random_forest_sklearn.csv', y_pred, delimiter=",", fmt='%d')

accuracy = accuracy_score(y_test, y_pred)
balenced_accuracy = sklearn.metrics.balanced_accuracy_score(y_test, y_pred)

print(accuracy)
print(balenced_accuracy)

# Function to get user input for body measurements
#def get_user_input():
 #   user_data = {}
  #  for col in input_cols:
   #     user_data[col] = float(input(f"Enter your {col}: "))
    #return user_data

#LBXTC - Total cholesterol (mg/dL)
#LBXGLU - Plasma glucose (mg/dL)
#BMXWT - weight
#BMXBMI - Body Mass Index (kg/m²)
#BMXHT - Standing height (cm)
#BMXWAIST - Waist circumference (cm)

# Get user input
#user_input = get_user_input()
lbxglu = float(input("Please enter plasma glucose results "))
lbxtc = float(input("Please enter total cholesterol results "))
bmxwt = float(input("Please enter weight "))
bmxbmi = float(input("Please enter body mass index (BMI) "))
bmxht = float(input("Please enter standing height "))
bmxwaist = float(input("Please enter waist circumference "))

# [lbxglu, lbxtc, bmxwt, bmxht, bmxwaist]
# Convert user input to DataFram
input_list = {'LBXGLU': [lbxglu],
             'LBXTC': [lbxtc],
             'BMXWT': [bmxwt],
             'BMXBMI': [bmxbmi],
             'BMXHT': [bmxht],
             'BMXWAIST': [bmxwaist]}

user_df = pd.DataFrame(input_list)

# Predict the classification for the user
user_prediction = model.predict(user_df)

# Output the result
if user_prediction[0] == 1:
    print("Diabetes is likely, please mention to your health professional during your next visit")
elif user_prediction[0] == 2:
    print("Diabetes is unlikely.")
else:
    print("It is possible that you have diabetes, consult your doctor if concerned.")
