import pandas as pd

# Read dataset3.csv
data = pd.read_csv("Datasets/dataset3.csv")

# Filter startups that closed and calculate their average number of participants
closed_startups_avg_participants = data[data['status'] == 'closed']['avg_participants'].mean()

# Filter startups that didn't close and calculate their average number of participants
nonclosed_startups_avg_participants = data[data['status'] != 'closed']['avg_participants'].mean()

# Create a DataFrame to store the results
result_df = pd.DataFrame({'category': ['closed_startups', 'nonclosed_startups'],
                          'avg_participants': [closed_startups_avg_participants, nonclosed_startups_avg_participants]})

# Export to CSV
result_df.to_csv("closed_vs_nonclosed_avg_participants.csv", index=False)
