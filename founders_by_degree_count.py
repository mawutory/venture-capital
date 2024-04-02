import pandas as pd

# Load the degrees.csv file
degrees_df = pd.read_csv("Datasets/dataset1/degrees.csv")

# Group by object_id (founder) and count the number of degrees
founder_degree_count = degrees_df.groupby('object_id').size().reset_index(name='degree_count')

# Group by degree count and count the number of founders
founders_by_degree_count = founder_degree_count.groupby('degree_count').size().reset_index(name='founder_count')

# Save the result to a CSV file
founders_by_degree_count.to_csv("founders_by_degree_count.csv", index=False)
