import pandas as pd

# Read the CSV file
df = pd.read_csv("Datasets/dataset1/funding_rounds.csv")

# Convert 'funded_at' column to datetime
df['funded_at'] = pd.to_datetime(df['funded_at'])

# Extract year from 'funded_at' column
df['year'] = df['funded_at'].dt.year

# Group by year and calculate statistics for number of participants per round
yearly_investors_stats = df.groupby('year')['participants'].agg(['mean', 'max', 'min']).reset_index()
yearly_investors_stats.columns = ['year', 'avg_investors_per_round', 'max_investors_per_round', 'min_investors_per_round']

# Round the average number to the nearest whole number
yearly_investors_stats['avg_investors_per_round'] = yearly_investors_stats['avg_investors_per_round'].round()

# Convert the average number to integer
yearly_investors_stats['avg_investors_per_round'] = yearly_investors_stats['avg_investors_per_round'].astype(int)

# Write the result to a new CSV file
yearly_investors_stats.to_csv("yearly_investors_stats.csv", index=False)
