import pandas as pd

# Read investments.csv and dataset3.csv
investments_df = pd.read_csv("Datasets/dataset1/investments.csv")
dataset3_df = pd.read_csv("Datasets/dataset3.csv")

# Merge investments data with dataset3 to get categories for each investor
merged_df = pd.merge(investments_df, dataset3_df, left_on='investor_object_id', right_on='id', how='left')

# Filter for startups funded by VC firms
startup_vc_df = merged_df[merged_df['funded_object_id'].str.startswith('c:')]

# Initialize a dictionary to store the count of unique VC firms in each category
vc_firm_count = {}

# Iterate through each category column
for category in ['is_software', 'is_web', 'is_mobile', 'is_enterprise', 'is_advertising', 
                 'is_gamesvideo', 'is_ecommerce', 'is_biotech', 'is_consulting', 'is_othercategory']:
    # Get unique VC firms for each category
    unique_vc_firms = startup_vc_df[startup_vc_df[category] == 1]['investor_object_id'].nunique()
    
    # Store the count in the dictionary
    vc_firm_count[category] = unique_vc_firms

# Convert the dictionary to a DataFrame
result_df = pd.DataFrame(list(vc_firm_count.items()), columns=['Category', 'Unique_VC_Firms'])

# Export the result to a CSV file
result_df.to_csv("unique_vc_firms_per_category.csv", index=False)
