import pandas as pd

# Read ipos.csv file
ipos_df = pd.read_csv("Datasets/dataset1/ipos.csv")

# Extract IPO year for each startup
ipos_df['public_at'] = pd.to_datetime(ipos_df['public_at'])
ipos_df['ipo_year'] = ipos_df['public_at'].dt.year

# Read funding_rounds.csv file
funding_rounds_df = pd.read_csv("Datasets/dataset1/funding_rounds.csv")

# Extract year of initial funding for each startup
funding_rounds_df['funded_at'] = pd.to_datetime(funding_rounds_df['funded_at'])
funding_rounds_df['initial_funding_year'] = funding_rounds_df['funded_at'].dt.year
earliest_funding_years = funding_rounds_df.groupby('object_id')['initial_funding_year'].min().reset_index()

# Merge IPO and funding data
merged_df = pd.merge(ipos_df, earliest_funding_years, on='object_id', how='inner')

# Calculate number of years from first funding to IPO
merged_df['years_to_ipo'] = merged_df['ipo_year'] - merged_df['initial_funding_year']

# Replace negative values with zero
merged_df['years_to_ipo'] = merged_df['years_to_ipo'].apply(lambda x: 0 if x < 0 else x)

# Calculate average valuation amount for startups in each year category
avg_valuation_by_year = merged_df.groupby('years_to_ipo')['valuation_amount'].mean().reset_index()
avg_valuation_by_year.columns = ['years_to_ipo', 'average_valuation_amount']

# Create distribution of number of startups per number of years
distribution = merged_df['years_to_ipo'].value_counts().reset_index()
distribution.columns = ['years_to_ipo', 'startups_count']

# Merge with average valuation data
distribution = pd.merge(distribution, avg_valuation_by_year, on='years_to_ipo', how='left')

# Export distribution to CSV
distribution.to_csv("startup_years_to_ipo_distribution_with_valuation.csv", index=False)
