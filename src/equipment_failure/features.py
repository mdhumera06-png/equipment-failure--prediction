
# Features used by our machine learning model
FEATURE_COLUMNS = [
    "Type",
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]

# Column we want to predict
TARGET_COLUMN = "Machine failure"


def prepare_features_target(df):
    """
    Separate input features (X) and target (y).
    """

    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    return X, y
