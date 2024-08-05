import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('diabetes_data.csv')

# Display basic information
print(data.info())
print(data.head())

# Handle missing values
data = data.replace('?', np.nan)
data = data.dropna()

# Convert categorical variables to numeric
data = pd.get_dummies(data)

# Split features and target
X = data.drop('readmitted', axis=1)
y = data['readmitted']
