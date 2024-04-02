import pandas as pd

# Read the CSV file
df = pd.read_csv("Datasets/dataset1/funding_rounds.csv")

# Convert 'funded_at' column to datetime
df['funded_at'] = pd.to_datetime(df['funded_at'])

# Calculate total raised amount and total startups funded
total_raised_amount = df['raised_amount_usd'].sum()
total_startups_funded = df['object_id'].nunique()

# Determine the period of data (year to year)
start_year = df['funded_at'].dt.year.min()
end_year = df['funded_at'].dt.year.max()

# Create a DataFrame for the output
output_df = pd.DataFrame({
    'total_raised_amount_usd': [total_raised_amount],
    'total_startups_funded': [total_startups_funded],
    'start_year': [start_year],
    'end_year': [end_year]
})

# Write the output DataFrame to a CSV file
output_df.to_csv("analysis_output.csv", index=False)
