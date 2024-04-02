import pandas as pd

# Read the CSV file
df = pd.read_csv('Datasets/dataset1/objects.csv')

# Filter out rows with missing funding information
df = df[df['funding_total_usd'].notna()]

# Convert funding_total_usd column to numeric
df['funding_total_usd'] = pd.to_numeric(df['funding_total_usd'], errors='coerce')

# Sort the DataFrame by funding_total_usd in descending order
df_sorted = df.sort_values(by='funding_total_usd', ascending=False)

# Select the top 10 startups
top_10_startups = df_sorted.head(10)

# Extract only the 'name' and 'funding_total_usd' columns
top_10_startups = top_10_startups[['name', 'funding_total_usd']]

# Save the result to a CSV file
top_10_startups.to_csv('top_10_startups_by_funding.csv', index=False)
