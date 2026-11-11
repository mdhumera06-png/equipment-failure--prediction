
from typing import Literal
import pandas as pd
from pathlib import Path

import joblib
from fastapi import FastAPI
from pydantic import BaseModel


# Find the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load the trained ML pipeline
MODEL_PATH = BASE_DIR / "models" / "random_forest_pipeline.joblib"

model = joblib.load(MODEL_PATH)

# Create FastAPI application
app = FastAPI(title="Equipment Failure Prediction API")


# Define the input data structure
class SensorData(BaseModel):
    Type: Literal["L", "M", "H"]
    Air_temperature: float
    Process_temperature: float
    Rotational_speed: float
    Torque: float
    Tool_wear: float



# Test endpoint
@app.get("/")
def home():
    return {"message": "Equipment Failure Prediction API is running!"}
# Prediction endpoint
@app.post("/predict")
def predict(data: SensorData):

    # Convert input data into a DataFrame
    input_data = pd.DataFrame([{
        "Type": data.Type,
        "Air temperature [K]": data.Air_temperature,
        "Process temperature [K]": data.Process_temperature,
        "Rotational speed [rpm]": data.Rotational_speed,
        "Torque [Nm]": data.Torque,
        "Tool wear [min]": data.Tool_wear
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Get estimated probability of machine failure
    failure_probability = model.predict_proba(input_data)[0][1]

    # Return prediction result
    if prediction == 1:
        result = "Machine Failure Predicted"
    else:
        result = "No Machine Failure Predicted"

    return {
        "prediction": int(prediction),
        "result": result,
        "failure_probability": round(float(failure_probability), 4)
    }
