import pandas as pd

# Read the CSV file
df = pd.read_csv("Datasets/dataset1/funding_rounds.csv")

# Convert 'funded_at' column to datetime
df['funded_at'] = pd.to_datetime(df['funded_at'])

# Extract year from 'funded_at' column
df['year'] = df['funded_at'].dt.year

# Group by year and calculate total raised amount for each year
yearly_total_raised = df.groupby('year')['raised_amount_usd'].sum().reset_index()

# Write the result to a new CSV file
yearly_total_raised.to_csv("yearly_total_raised.csv", index=False)
