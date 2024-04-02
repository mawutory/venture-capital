import pandas as pd

# Read the CSV file
df = pd.read_csv("Datasets/dataset1/funding_rounds.csv")

# Convert 'funded_at' column to datetime
df['funded_at'] = pd.to_datetime(df['funded_at'])

# Extract year from 'funded_at' column
df['year'] = df['funded_at'].dt.year

# Group by year and calculate total startups funded for each year
yearly_total_startups_funded = df.groupby('year')['object_id'].nunique().reset_index()
yearly_total_startups_funded.columns = ['year', 'total_startups_funded']

# Write the result to a new CSV file
yearly_total_startups_funded.to_csv("yearly_total_startups_funded.csv", index=False)
