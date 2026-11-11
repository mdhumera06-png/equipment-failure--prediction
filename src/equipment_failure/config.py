from pathlib import Path

# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Define important project directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_DIR = BASE_DIR / "models"
REPORT_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORT_DIR / "figures"

# Dataset path
DATASET_PATH = RAW_DATA_DIR / "ai4i2020.csv"

# Trained model path
MODEL_PATH = MODEL_DIR / "random_forest_pipeline.joblib"