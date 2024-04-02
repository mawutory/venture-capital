import pandas as pd

# Read funding_rounds.csv file
funding_rounds_df = pd.read_csv("Datasets/dataset1/funding_rounds.csv")

# Calculate total raised amount USD for each startup
total_raised_amounts = funding_rounds_df.groupby('object_id')['raised_amount_usd'].sum().reset_index()

# Calculate average raised amount USD across all startups
average_raised_amount = total_raised_amounts['raised_amount_usd'].mean()

# Define categories based on average raised amount
categories = ['Very Low', 'Low', 'Moderate', 'High', 'Very High']

# Define bins based on average raised amount
bins = [0, average_raised_amount/2, average_raised_amount, average_raised_amount*2, average_raised_amount*5, max(total_raised_amounts['raised_amount_usd'])]

# Categorize startups based on total raised amount
total_raised_amounts['category'] = pd.cut(total_raised_amounts['raised_amount_usd'], bins, labels=categories, right=False)

# Count startups in each category
category_counts = total_raised_amounts['category'].value_counts().reset_index()
category_counts.columns = ['category', 'startup_count']

# Read ipos.csv file
ipos_df = pd.read_csv("Datasets/dataset1/ipos.csv")

# Get list of IPOed startups
ipoed_startups = ipos_df['object_id'].tolist()

# Filter IPOed startups from total raised amounts
ipoed_total_raised_amounts = total_raised_amounts[total_raised_amounts['object_id'].isin(ipoed_startups)]

# Count IPOed startups in each category
ipoed_category_counts = ipoed_total_raised_amounts['category'].value_counts().reset_index()
ipoed_category_counts.columns = ['category', 'ipoed_startup_count']

# Merge counts of IPOed startups with all startup counts
merged_category_counts = pd.merge(category_counts, ipoed_category_counts, on='category', how='left')

# Export to CSV
merged_category_counts.to_csv("startup_total_funding_amount_categories_with_ipos.csv", index=False)
