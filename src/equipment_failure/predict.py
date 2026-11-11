
import joblib
import pandas as pd

from equipment_failure.config import MODEL_PATH
from equipment_failure.features import FEATURE_COLUMNS


def predict_failure(input_data):

    # Load the trained model
    model = joblib.load(MODEL_PATH)

    # Convert input into a DataFrame
    input_df = pd.DataFrame(
        [input_data],
        columns=FEATURE_COLUMNS
    )

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Calculate failure probability
    probability = model.predict_proba(input_df)[0][1]

    # Prepare prediction result
    if prediction == 1:
        result = "Machine Failure Predicted"
    else:
        result = "No Machine Failure Predicted"

    return {
        "prediction": int(prediction),
        "result": result,
        "failure_probability": round(float(probability), 4)
    }
