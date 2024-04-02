import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder

# Load the preprocessed dataset
data = pd.read_csv('preprocessed_objects_age_funding_status.csv')

# Encode the 'status' column to numerical values
label_encoder = LabelEncoder()
data['status'] = label_encoder.fit_transform(data['status'])

# Define features (X) and target variable (y)
X = data[['age', 'funding_total_usd']]
y = data['status']

# Train a Gradient Boosting classifier
model = GradientBoostingClassifier()
model.fit(X, y)

# Plot decision boundary
x_min, x_max = X['age'].min() - 1, X['age'].max() + 1
y_min, y_max = X['funding_total_usd'].min() - 1, X['funding_total_usd'].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.4)
plt.scatter(X['age'], X['funding_total_usd'], c=y, s=20, edgecolor='k')
plt.xlabel('Age')
plt.ylabel('Funding Total USD')
plt.title('Decision Boundary of Gradient Boosting Classifier')
plt.show()
