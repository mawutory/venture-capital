import sys
import joblib

# Suppress scikit-learn warnings
import warnings
warnings.filterwarnings("ignore")

# Load the trained model
model = joblib.load('gradient_boost_model.pkl')

# Get arguments from command line
age = float(sys.argv[1])
funding_total_usd = float(sys.argv[2])

# Make predictions
prediction = model.predict([[age, funding_total_usd]])

# Output the prediction message
if prediction[0] == 'closed':
    print("Startup is likely to fail")
else:
    print("Startup is likely to succeed")
