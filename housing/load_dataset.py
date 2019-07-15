import pandas as pd
from constants import CSV_PATH

def load_housing_data():
    return pd.read_csv(CSV_PATH)
