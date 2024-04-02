import pandas as pd

# Load dataset
dataset2_df = pd.read_csv('Datasets/dataset2.csv')

# Define popularity bins
popularity_bins = [0, 10, 20, 30, 40, 50, float('inf')]
popularity_labels = ['Very Low', 'Low', 'Moderate', 'High', 'Very High', 'Extremely High']

# Categorize funders by popularity
dataset2_df['Popularity'] = pd.cut(dataset2_df['Number of News Articles'], bins=popularity_bins, labels=popularity_labels)

# Count the distribution of funders by popularity
popularity_distribution = dataset2_df.groupby('Popularity').size().reset_index(name='Funder Count')

# Output to CSV
popularity_distribution.to_csv('popularity_distribution.csv', index=False)
