import pandas as pd

# Read dataset3.csv
data = pd.read_csv("Datasets/dataset3.csv")

# Filter startups that closed and are in top 500
closed_top500 = data[(data['status'] == 'closed') & (data['is_top500'] == 1)]

# Filter startups that are in top 500 but are not closed
nonclosed_top500 = data[(data['status'] != 'closed') & (data['is_top500'] == 1)]

# Count the number of startups in each category
closed_top500_count = closed_top500.shape[0]
nonclosed_top500_count = nonclosed_top500.shape[0]

# Create a DataFrame to store the counts
result_df = pd.DataFrame({'category': ['closed_top500', 'nonclosed_top500'],
                          'startup_count': [closed_top500_count, nonclosed_top500_count]})

# Export to CSV
result_df.to_csv("closed_and_nonclosed_top500_count.csv", index=False)
