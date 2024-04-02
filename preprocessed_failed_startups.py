import pandas as pd

# Define data types for each column
dtype_dict = {
    'id': str,
    'entity_type': str,
    'name': str,
    'normalized_name': str,
    'category_code': str,
    'status': str,  # Assuming 'status' is a categorical variable
    'founded_at': str,  # Change to datetime if needed
    'closed_at': str,  # Change to datetime if needed
    'investment_rounds': int,
    'invested_companies': int,
    'funding_rounds': int,
    'funding_total_usd': float,
    'milestones': int,
    'relationships': int,
}

# Load the dataset
objects_df = pd.read_csv("Datasets/dataset1/objects.csv", dtype=dtype_dict)

# Filter to include only closed startups
closed_startups_df = objects_df[objects_df['status'] == 'closed']

# Remove irrelevant columns
irrelevant_columns = ['domain', 'logo_url', 'logo_width', 'logo_height', 'entity_id', 'parent_id', 'permalink', 'homepage_url',
                      'twitter_username', 'short_description', 'description', 'overview', 'tag_list', 
                      'country_code', 'state_code', 'city', 'region', 'first_investment_at', 
                      'last_investment_at', 'first_funding_at', 'last_funding_at', 'first_milestone_at', 
                      'last_milestone_at', 'created_by', 'created_at', 'updated_at']
closed_startups_df.drop(columns=irrelevant_columns, inplace=True)

# Drop rows with missing values
closed_startups_df.dropna(inplace=True)

# Save the preprocessed dataset to a new CSV file
closed_startups_df.to_csv("preprocessed_closed_startups.csv", index=False)
