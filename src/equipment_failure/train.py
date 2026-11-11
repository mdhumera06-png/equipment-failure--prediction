
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from equipment_failure.config import MODEL_PATH
from equipment_failure.data import load_data
from equipment_failure.features import (
    FEATURE_COLUMNS,
    TARGET_COLUMN,
    prepare_features_target
)


def train_model():

    # Load dataset
    df = load_data()

    # Separate features and target
    X, y = prepare_features_target(df)

    # Identify numerical and categorical columns
    numerical_features = FEATURE_COLUMNS[1:]
    categorical_features = ["Type"]

    # Create preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical_features),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
        ]
    )

    # Create Random Forest pipeline
    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", RandomForestClassifier(
                n_estimators=200,
                class_weight="balanced",
                random_state=42,
                n_jobs=-1
            ))
        ]
    )

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Train model
    model.fit(X_train, y_train)

    # Save trained model
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print("Model trained successfully!")
    print(f"Model saved at: {MODEL_PATH}")

    return model, X_test, y_test


if __name__ == "__main__":
    train_model()
