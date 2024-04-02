import pandas as pd

# Define data types for each column
dtype_dict = {
    'id': str,
    'entity_type': str,
    'entity_id': str,
    'parent_id': str,
    'name': str,
    'normalized_name': str,
    'permalink': str,
    'category_code': str,
    'status': str,  # Assuming 'status' is a categorical variable
    'founded_at': str,  # Change to datetime if needed
    'closed_at': str,  # Change to datetime if needed
    'domain': str,
    'homepage_url': str,
    'twitter_username': str,
    'short_description': str,
    'description': str,
    'overview': str,
    'tag_list': str,
    'country_code': str,
    'state_code': str,
    'city': str,
    'region': str,
    'first_investment_at': str,  # Change to datetime if needed
    'last_investment_at': str,  # Change to datetime if needed
    'investment_rounds': int,
    'invested_companies': int,
    'first_funding_at': str,  # Change to datetime if needed
    'last_funding_at': str,  # Change to datetime if needed
    'funding_rounds': int,
    'funding_total_usd': float,
    'first_milestone_at': str,  # Change to datetime if needed
    'last_milestone_at': str,  # Change to datetime if needed
    'milestones': int,
    'relationships': int,
    'created_by': str,
    'created_at': str,  # Change to datetime if needed
    'updated_at': str,  # Change to datetime if needed
}

# Load the dataset
objects_df = pd.read_csv("Datasets/dataset1/objects.csv", dtype=dtype_dict)

# Remove irrelevant columns
irrelevant_columns = ['domain', 'logo_url', 'logo_width', 'logo_height', 'entity_id', 'parent_id', 'permalink', 'homepage_url',
                      'twitter_username', 'short_description', 'description', 'overview', 'tag_list', 
                      'country_code', 'state_code', 'city', 'region', 'first_investment_at', 
                      'last_investment_at', 'first_funding_at', 'last_funding_at', 'first_milestone_at', 
                      'last_milestone_at', 'created_by', 'created_at', 'updated_at']
objects_df.drop(columns=irrelevant_columns, inplace=True)

# Drop rows with missing values
objects_df.dropna(inplace=True)

# Save the preprocessed dataset to a new CSV file
objects_df.to_csv("preprocessed_objects.csv", index=False)
