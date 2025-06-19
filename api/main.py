from fastapi import FastAPI
import mlflow.pyfunc
import pandas as pd

app = FastAPI()
model = mlflow.pyfunc.load_model(model_uri="models:/TelcoChurnModel/Production")

@app.post("/predict")
def predict(input_data: dict):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)
    return {"churn_prediction": int(prediction[0])}
