# Telco Churn Prediction – End-to-End ML Deployment Project

This project builds and deploys a machine learning model to predict teleco customer churn.

## Features
- Binary churn prediction using scikit-learn
- Model tracking and registry via MLflow
- API serving via FastAPI
- Free deployment on Render
- Monitoring with Evidently AI

## Data
[Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn?select=WA_Fn-UseC_-Telco-Customer-Churn.csv)

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Train and register model - Use notebooks 01_exploration_and_training.ipynb

3. Start the API locally: uvicorn api.main:app --reload

4. Generate drift report: python monitoring/drift_report.py

## API Endpoint
POST /predict – Send a JSON dict with customer features to receive churn prediction.
