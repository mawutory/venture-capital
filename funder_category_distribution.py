import pandas as pd

# Load the dataset
dataset2_df = pd.read_csv("Datasets/dataset2.csv")

# Calculate the average number of investments per funder
average_investments = dataset2_df['Number of Investments_x'].mean()

# Define bin sizes based on average number of investments
if average_investments < 5:
    bin_size = 5
elif average_investments < 10:
    bin_size = 10
elif average_investments < 15:
    bin_size = 15
else:
    bin_size = 20

# Create bin edges
bin_edges = list(range(0, int(average_investments) + bin_size, bin_size))

# Create bins labels
bin_labels = [f"{i}-{i+bin_size-1} Investments" for i in range(0, int(average_investments), bin_size)]

# Assign bins to each funder based on the average number of investments
dataset2_df['Category'] = pd.cut(dataset2_df['Number of Investments_x'], bins=bin_edges, labels=bin_labels, include_lowest=True)

# Count the distribution across categories
category_distribution = dataset2_df.groupby('Category').size().reset_index(name='funder_count')

# Save the distribution to a CSV file
category_distribution.to_csv('funder_category_distribution.csv', index=False)
