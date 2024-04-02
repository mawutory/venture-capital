import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score

# Load the preprocessed dataset
data = pd.read_csv("preprocessed_objects_age_funding_status.csv")

# Split the dataset into features (X) and target variable (y)
X = data[['age', 'funding_total_usd']]
y = data['status']

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Selection
models = {
    'Logistic Regression': LogisticRegression(),
    'Random Forest': RandomForestClassifier(),
    'Gradient Boosting': GradientBoostingClassifier()
}

# Train and evaluate each model
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    roc_auc = roc_auc_score(y_test, model.predict_proba(X_test), multi_class='ovr')
    results[name] = {'Accuracy': accuracy, 'Precision': precision, 'Recall': recall, 'ROC AUC': roc_auc}

# Convert results to DataFrame
results_df = pd.DataFrame(results)

# Add a new column for evaluation metric
evaluation_metric = ['Accuracy', 'Precision', 'Recall', 'ROC AUC']
results_df.insert(0, 'Evaluation Metric', evaluation_metric)

# Output the results to a CSV file
results_df.to_csv("model_evaluation_results.csv", index=False)