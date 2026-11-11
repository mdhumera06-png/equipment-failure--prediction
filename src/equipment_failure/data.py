
import pandas as pd

from equipment_failure.config import DATASET_PATH


def load_data():
    """
    Load the equipment failure dataset.
    """
    df = pd.read_csv(DATASET_PATH)

    return df
