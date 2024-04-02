# predict.py

import argparse
import joblib

def predict_status(age, total_funding_usd):
    # Load the trained model
    model = joblib.load('gradient_boost_model.pkl')
    
    # Make predictions
    prediction = model.predict([[age, total_funding_usd]])
    
    return prediction[0]

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Predict startup status')
    parser.add_argument('--age', type=int, help='Age of the startup')
    parser.add_argument('--total_funding_usd', type=float, help='Total funding amount in USD')
    args = parser.parse_args()
    
    # Call predict_status function with provided arguments
    prediction = predict_status(args.age, args.total_funding_usd)
    
    # Output the prediction
    print("Predicted status:", prediction)