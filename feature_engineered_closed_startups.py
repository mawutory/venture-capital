import pandas as pd

# Load the preprocessed dataset
preprocessed_df = pd.read_csv("preprocessed_closed_startups.csv")

# Calculate startup age in years
preprocessed_df['founded_at'] = pd.to_datetime(preprocessed_df['founded_at']).dt.year
preprocessed_df['closed_at'] = pd.to_datetime(preprocessed_df['closed_at']).dt.year
preprocessed_df['age'] = preprocessed_df['closed_at'] - preprocessed_df['founded_at']
preprocessed_df['age'] = preprocessed_df['age'].apply(lambda x: max(x, 0))  # Replace negative values with 0
preprocessed_df.drop(columns=['founded_at', 'closed_at', 'investment_rounds'], inplace=True)

# Select relevant features
features_df = preprocessed_df[['age', 'funding_total_usd']]

# Save the feature-engineered dataset to a new CSV file
features_df.to_csv("feature_engineered_closed_startups.csv", index=False)
