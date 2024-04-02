import pandas as pd

# Load the degrees.csv file
degrees_df = pd.read_csv("Datasets/dataset1/degrees.csv")

# Count the number of distinct founders by degree_type
founder_count_by_degree = degrees_df.groupby('degree_type')['object_id'].nunique().reset_index(name='founder_count')

# Save the result to a CSV file
founder_count_by_degree.to_csv("founder_count_by_degree.csv", index=False)
