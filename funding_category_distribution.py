import pandas as pd

# Load the dataset
dataset2_df = pd.read_csv("dataset2.csv")

# Calculate the average number of investments per funder
average_investments = dataset2_df['Number of Investments_x'].mean()

# Define categories based on average number of investments
if average_investments < 5:
    category = 'Low'
elif average_investments < 10:
    category = 'Medium'
elif average_investments < 15:
    category = 'High'
else:
    category = 'Very High'

# Count the distribution across categories
category_distribution = dataset2_df.groupby(category).size().reset_index(name='funder_count')

# Save the result to a CSV file
category_distribution.to_csv("funder_category_distribution.csv", index=False)
