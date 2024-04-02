import pandas as pd

# Load the investments data
investments_df = pd.read_csv('Datasets/dataset1/investments.csv')

# Group by investor_object_id and count the number of investments
investor_counts = investments_df.groupby('investor_object_id').size().reset_index(name='investment_count')

# Calculate the average number of investments per VC firm
average_investments = investor_counts['investment_count'].mean()

# Define categories based on the average number of investments
bins = [0, average_investments, 2 * average_investments, 3 * average_investments, float('inf')]
labels = ['Low', 'Medium', 'High', 'Very High']

# Categorize VC firms based on the number of investments
investor_counts['investment_category'] = pd.cut(investor_counts['investment_count'], bins=bins, labels=labels, right=False)

# Count the number of VC firms in each category
category_counts = investor_counts['investment_category'].value_counts().reset_index()
category_counts.columns = ['category', 'vc_firm_count']

# Output the results to a CSV file
category_counts.to_csv('vc_firm_categories.csv', index=False)
