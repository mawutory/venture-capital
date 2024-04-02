# Predictive Analysis for Startup Success Prediction

This repository contains a predictive analysis project aimed at determining the likelihood of success or failure for startups based on certain features such as age and total funding. The analysis involves training a machine learning model using historical startup data and deploying it to make predictions on new startup entries.

## Project Overview

The predictive analysis consists of the following key steps:

1. **Data Preprocessing**: Clean and preprocess the raw startup data to extract relevant features and prepare it for model training.

2. **Feature Engineering**: Engineer new features such as startup age (in years), which is derived from the difference between the founded date and closed date (if available).

3. **Model Training**: Train a Gradient Boosting Classifier using scikit-learn to learn the patterns in the startup data and predict their success or failure.

4. **Model Evaluation**: Evaluate the trained model's performance using various metrics including accuracy, precision, recall, and area under the ROC curve (AUC).

5. **Model Deployment**: Deploy the trained model as a standalone script (`predict_startup.py`) to make real-time predictions for new startup entries.

## Dependencies

Before running the `predict_startup.py` script, ensure you have the following dependencies installed:

- Python 3.x
- scikit-learn
- pandas
- joblib

You can install these dependencies using pip:

```bash
pip install scikit-learn pandas joblib
```

## Usage

To make predictions using the trained model, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/predictive-analysis.git
```

2. Navigate to the repository directory:

```bash
cd predictive-analysis
```

3. Run the `predict_startup.py` script with the following command:

```bash
python3 predict_startup.py <age> <funding_total_usd>
```

Replace `<age>` and `<funding_total_usd>` with the age (in years) and total funding amount (in USD) of the startup you want to predict.

## Example

```bash
python3 predict_startup.py 3 50000
```

This command will predict the success or failure of a startup that is 3 years old and has received $50,000 in total funding.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.