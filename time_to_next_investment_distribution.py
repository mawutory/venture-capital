import pandas as pd

# Read investments.csv
investments_df = pd.read_csv("Datasets/dataset1/investments.csv")

# Convert 'created_at' column to datetime
investments_df['created_at'] = pd.to_datetime(investments_df['created_at'])

# Sort data by investor_object_id and created_at
investments_df.sort_values(by=['investor_object_id', 'created_at'], inplace=True)

# Calculate time difference between consecutive investments for each VC firm
investments_df['time_to_next_investment'] = investments_df.groupby('investor_object_id')['created_at'].diff().dt.days / 30

# Compute average time to next investment for each VC firm
vc_firm_avg_time = investments_df.groupby('investor_object_id')['time_to_next_investment'].mean()

# Create distribution of time to next investment
time_intervals = pd.cut(vc_firm_avg_time, bins=[0, 3, 6, 9, 12, 15, float('inf')], right=False)
vc_firm_counts = time_intervals.value_counts().sort_index()

# Define labels for time intervals
time_interval_labels = ['0-3 Months', '3-6 Months', '6-9 Months', '9-12 Months', '12-15 Months', '15+ Months']

# Output results as CSV
vc_firm_counts.to_csv("time_to_next_investment_distribution.csv", header=['vc_firm_count'], index_label='time_to_next_investment', line_terminator='\n')

print("Distribution of VC firms based on time to next investment has been saved to time_to_next_investment_distribution.csv.")
