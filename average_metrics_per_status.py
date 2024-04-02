import pandas as pd

# Load the dataset
objects_df = pd.read_csv('Datasets/dataset1/objects.csv')

# Group by status and calculate the average of each metric
avg_metrics_per_status = objects_df.groupby('status').agg({
    'funding_rounds': 'mean',
    'invested_companies': 'mean',
    'milestones': 'mean'
}).reset_index()

# Rename columns for clarity
avg_metrics_per_status = avg_metrics_per_status.rename(columns={
    'funding_rounds': 'avg_investment_rounds',
    'invested_companies': 'avg_invested_companies',
    'milestones': 'avg_milestones'
})

# Round the metrics to 2 decimal places
avg_metrics_per_status = avg_metrics_per_status.round(2)

# Save the results to a CSV file
avg_metrics_per_status.to_csv('average_metrics_per_status.csv', index=False)
