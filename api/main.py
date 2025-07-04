from config.settings import config
from fastapi import FastAPI
import mlflow.pyfunc
import pandas as pd


mlflow.set_tracking_uri(config.mlflow_tracking_uri)

# Initialize FastAPI app and load the model
app = FastAPI()
try:
    model = mlflow.pyfunc.load_model(model_uri=f'models:/{config.model_name}/{config.model_version}')
    print('Successfully loaded model:', config.model_name)
except Exception as e:
    print(f'Could not load model: {config.model_name} | Error: {e}')


@app.post('/predict')
def predict(input_data: dict):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)
    return {'churn_prediction': int(prediction[0])}
