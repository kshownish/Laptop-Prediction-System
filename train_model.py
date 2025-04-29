import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load dataset
df = pd.read_csv('data/laptop_data.csv')

# Drop unnecessary column
df.drop(columns=['Unnamed: 0'], inplace=True)

# Clean data
df['Ram'] = df['Ram'].str.replace('GB', '').astype('int32')
df['Weight'] = df['Weight'].str.replace('kg', '').astype('float32')

# Simplify CPU and GPU for demo
df['Cpu brand'] = df['Cpu'].apply(lambda x: 'Intel Core i5' if 'i5' in x else 'Intel Core i7' if 'i7' in x else 'Other')
df['Gpu brand'] = df['Gpu'].apply(lambda x: 'Intel' if 'Intel' in x else 'AMD' if 'AMD' in x else 'Nvidia')

# Select features (simplified for demo)
df = df[['Company', 'Ram', 'Cpu brand', 'Price']]

# Define features and target
X = df.drop('Price', axis=1)
y = df['Price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create preprocessing pipeline
numeric_features = ['Ram']
categorical_features = ['Company', 'Cpu brand']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

# Create pipeline
pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train model
pipe.fit(X_train, y_train)

# Save DataFrame and pipeline
pickle.dump(df, open('df.pkl', 'wb'))
pickle.dump(pipe, open('pipe.pkl', 'wb'))

print("Model and DataFrame saved successfully!")