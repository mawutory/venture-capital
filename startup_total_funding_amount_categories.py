import pandas as pd

# Read ipos.csv file
ipos_df = pd.read_csv("Datasets/dataset1/ipos.csv")

# Get list of startups that IPOed
ipoed_startups = ipos_df['object_id'].tolist()

# Read funding_rounds.csv file
funding_rounds_df = pd.read_csv("Datasets/dataset1/funding_rounds.csv")

# Filter funding rounds for IPOed startups
ipoed_funding_rounds = funding_rounds_df[funding_rounds_df['object_id'].isin(ipoed_startups)]

# Calculate total raised amount USD for each startup
total_raised_amounts = ipoed_funding_rounds.groupby('object_id')['raised_amount_usd'].sum().reset_index()

# Define categories based on total raised amount
min_raised_amount = total_raised_amounts['raised_amount_usd'].min()
max_raised_amount = total_raised_amounts['raised_amount_usd'].max()
bin_size = (max_raised_amount - min_raised_amount) / 5

# Define category labels
categories = ['Very Low', 'Low', 'Moderate', 'High', 'Very High']

# Define bins
bins = [min_raised_amount + i * bin_size for i in range(6)]

# Categorize startups based on total raised amount
total_raised_amounts['category'] = pd.cut(total_raised_amounts['raised_amount_usd'], bins, labels=categories, right=False)

# Count startups in each category
category_counts = total_raised_amounts['category'].value_counts().reset_index()
category_counts.columns = ['category', 'startup_count']

# Export to CSV
category_counts.to_csv("startup_total_funding_amount_categories.csv", index=False)
