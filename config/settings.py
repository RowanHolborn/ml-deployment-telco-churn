from pydantic import BaseSettings
from typing import List


class AppConfig(BaseSettings):
    model_name: str = 'telco_churn_classifier'
    model_version: str = '2'
    model_stage: str = 'Staging'
    mlflow_tracking_uri: str = 'file:/app/mlruns'
    api_url: str = 'http://api:8000/predict'

    feature_columns: List[str] = [
        'tenure', 'MonthlyCharges', 'TotalCharges',
        'gender_Male', 'SeniorCitizen_1', 'Partner_Yes', 'Dependents_Yes',
        'PhoneService_Yes', 'MultipleLines_No', 'MultipleLines_No phone service',
        'MultipleLines_Yes', 'InternetService_DSL', 'InternetService_Fiber optic',
        'InternetService_No', 'OnlineSecurity_No', 'OnlineSecurity_No internet service',
        'OnlineSecurity_Yes', 'OnlineBackup_No', 'OnlineBackup_No internet service',
        'OnlineBackup_Yes', 'DeviceProtection_No', 'DeviceProtection_No internet service',
        'DeviceProtection_Yes', 'TechSupport_No', 'TechSupport_No internet service',
        'TechSupport_Yes', 'StreamingTV_No', 'StreamingTV_No internet service',
        'StreamingTV_Yes', 'StreamingMovies_No', 'StreamingMovies_No internet service',
        'StreamingMovies_Yes', 'Contract_Month-to-month', 'Contract_One year',
        'Contract_Two year', 'PaperlessBilling_Yes',
        'PaymentMethod_Bank transfer (automatic)', 'PaymentMethod_Credit card (automatic)',
        'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check'
    ]

    class Config:
        env_file = '.env'  # Optional file to override defaults


# Export a global instance
config = AppConfig()
