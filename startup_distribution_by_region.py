import pandas as pd

# Read ipos.csv to get list of IPOed startups
ipos_df = pd.read_csv("Datasets/dataset1/ipos.csv")
ipoed_startups = ipos_df['object_id'].tolist()

# Read objects.csv to get startup details
objects_df = pd.read_csv("Datasets/dataset1/objects.csv")

# Filter startups that match IPOed startups
ipoed_startup_details = objects_df[objects_df['id'].isin(ipoed_startups)]

# Count startups by region
startup_distribution = ipoed_startup_details['region'].value_counts().reset_index()
startup_distribution.columns = ['region', 'startup_count']

# Export to CSV
startup_distribution.to_csv("startup_distribution_by_region.csv", index=False)
