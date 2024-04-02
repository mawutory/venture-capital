import pandas as pd

# Load the dataset
dataset2_df = pd.read_csv("Datasets/dataset2.csv")

# Count the number of funders by gender
gender_distribution = dataset2_df.groupby('Gender').size().reset_index(name='funder_count')

# Save the distribution to a CSV file
gender_distribution.to_csv('funder_gender_distribution.csv', index=False)
