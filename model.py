# Step 1: Train the Model
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd

# Load the preprocessed dataset
data = pd.read_csv('preprocessed_objects_age_funding_status.csv')

# Define features (X) and target variable (y)
X = data[['age', 'funding_total_usd']]
y = data['status']

# Rename columns to provide valid feature names
X.columns = ['age', 'funding_total_usd']

# Train the Gradient Boosting model
model = GradientBoostingClassifier()
model.fit(X, y)

# Step 2: Save the Model
import joblib

# Save the trained model to a file
joblib.dump(model, 'gradient_boost_model.pkl')

# Step 3: Create the predict.py Script
# This script can be called with age and total_funding_usd arguments to make predictions
# Example usage: python predict.py --age 2 --total_funding_usd 100000
