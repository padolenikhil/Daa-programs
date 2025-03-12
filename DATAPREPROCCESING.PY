import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

# Load the CSV file
file_path = 'C:\Users\LENOVO\Documents\Book1.csv'
data = pd.read_csv(C:\Users\LENOVO\Documents\Book1.csv)

# Display the first few rows of the dataframe
print("Original Data:")
print(data.head())

# Define the preprocessing for numerical data
numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# Define the preprocessing for categorical data
categorical_features = data.select_dtypes(include=['object']).columns
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine the preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Preprocess the data
preprocessed_data = preprocessor.fit_transform(data)

# Convert preprocessed data back to a DataFrame
preprocessed_df = pd.DataFrame(preprocessed_data)

# Display the first few rows of the preprocessed dataframe
print("Preprocessed Data:")
print(preprocessed_df.head())
