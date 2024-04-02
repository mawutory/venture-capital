import pandas as pd

# Load the dataset
dataset2_df = pd.read_csv("Datasets/dataset2.csv")

# Calculate the average number of investments per funder
average_investments = dataset2_df['Number of Investments_x'].mean()

# Define bin sizes based on the total average number of investments
bin_size = 3

# Create bin edges
bin_edges = list(range(0, int(average_investments) + bin_size, bin_size))

# Create bins labels
bin_labels = [f"{i}-{i+bin_size-1} Investments" for i in range(0, int(average_investments), bin_size)]

# Assign bins to each funder based on the total average number of investments
dataset2_df['Investment Category'] = pd.cut(dataset2_df['Number of Investments_x'], bins=bin_edges, labels=bin_labels, include_lowest=True)

# Count the distribution across categories
investment_distribution = dataset2_df.groupby('Investment Category').size().reset_index(name='funder_count')

# Save the distribution to a CSV file
investment_distribution.to_csv('funder_investment_distribution.csv', index=False)
