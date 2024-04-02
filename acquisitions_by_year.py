import pandas as pd

# Load data from acquisitions.csv
acquisitions_data = pd.read_csv('Datasets/dataset1/acquisitions.csv')

# Convert 'acquired_at' column to datetime format
acquisitions_data['acquired_at'] = pd.to_datetime(acquisitions_data['acquired_at'])

# Extract year from 'acquired_at' column and create a new 'year' column
acquisitions_data['year'] = acquisitions_data['acquired_at'].dt.year

# Count the number of acquisitions for each year
acquisitions_by_year = acquisitions_data['year'].value_counts().sort_index().reset_index()
acquisitions_by_year.columns = ['year', 'acquisition_count']

# Save the result to a CSV file
acquisitions_by_year.to_csv('acquisitions_by_year.csv', index=False)
