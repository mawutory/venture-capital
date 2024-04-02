import pandas as pd

# Load the dataset
objects_df = pd.read_csv("Datasets/dataset1/objects.csv")

# Convert 'founded_at' and 'closed_at' columns to datetime
objects_df['founded_at'] = pd.to_datetime(objects_df['founded_at'])
objects_df['closed_at'] = pd.to_datetime(objects_df['closed_at'])

# Calculate the startup age in years
objects_df['closed_at'] = objects_df['closed_at'].fillna(pd.to_datetime('2024-01-01'))
objects_df['age'] = (objects_df['closed_at'].dt.year - objects_df['founded_at'].dt.year)

# Remove rows with negative age (startup still running)
objects_df = objects_df[objects_df['age'] >= 0]

# Drop irrelevant columns
irrelevant_columns = ['entity_id', 'parent_id', 'permalink', 'homepage_url', 'twitter_username',
                      'short_description', 'description', 'overview', 'tag_list', 'country_code',
                      'state_code', 'city', 'region', 'first_investment_at', 'last_investment_at',
                      'first_funding_at', 'last_funding_at', 'first_milestone_at', 'last_milestone_at',
                      'created_by', 'created_at', 'updated_at']
objects_df.drop(columns=irrelevant_columns, inplace=True)

# Select only 'age', 'total_funding_usd', and 'status' columns
objects_df = objects_df[['age', 'funding_total_usd', 'status']]

# Save the preprocessed dataset to a new CSV file
objects_df.to_csv("preprocessed_objects_age_funding_status.csv", index=False)
