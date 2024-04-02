import pandas as pd

# Read dataset3.csv
dataset3_df = pd.read_csv("Datasets/dataset3.csv")

# Count the number of distinct startups in each category
category_counts = {}
categories = ['is_software', 'is_web', 'is_mobile', 'is_enterprise', 'is_advertising', 
              'is_gamesvideo', 'is_ecommerce', 'is_biotech', 'is_consulting', 'is_othercategory']

for category in categories:
    category_counts[category] = dataset3_df.loc[dataset3_df[category] == 1, 'object_id'].nunique()

# Convert the counts to a DataFrame
category_counts_df = pd.DataFrame.from_dict(category_counts, orient='index', columns=['Startup_Count'])

# Reset index to have categories as a column
category_counts_df.reset_index(inplace=True)
category_counts_df.rename(columns={'index': 'Category'}, inplace=True)

# Export the result to a CSV file
category_counts_df.to_csv("startup_count_per_category.csv", index=False)
