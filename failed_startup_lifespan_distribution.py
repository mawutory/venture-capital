import pandas as pd

# Read dataset3.csv
data = pd.read_csv("Datasets/dataset3.csv")

# Filter closed startups
closed_startups = data[data['status'] == 'closed']

# Calculate lifespan in years
closed_startups['founded_at'] = pd.to_datetime(closed_startups['founded_at'])
closed_startups['closed_at'] = pd.to_datetime(closed_startups['closed_at'])
closed_startups['lifespan_years'] = (closed_startups['closed_at'].dt.year - closed_startups['founded_at'].dt.year)

# Exclude negative lifespans (founded after closed)
closed_startups = closed_startups[closed_startups['lifespan_years'] >= 0]

# Count distribution of failed startups by lifespan in years
lifespan_distribution = closed_startups['lifespan_years'].value_counts().reset_index()
lifespan_distribution.columns = ['lifespan_years', 'startup_count']

# Export to CSV
lifespan_distribution.to_csv("failed_startup_lifespan_distribution.csv", index=False)
