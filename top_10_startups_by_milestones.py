import pandas as pd

# Load the dataset
objects_df = pd.read_csv('Datasets/dataset1/objects.csv')

# Sort the dataframe by number of milestones in descending order
top_10_startups = objects_df.sort_values(by='milestones', ascending=False).head(10)

# Select only the 'name' column
top_10_startups = top_10_startups[['name']]

# Save the top 10 startups to a CSV file
top_10_startups.to_csv('top_10_startups_by_milestones.csv', index=False)
