# app/utils/data_loader.py
import pandas as pd

def load_data(file_path: str):
    return pd.read_csv(file_path)
