import pandas as pd

def extract_data():
    df = pd.read_csv("data/raw/students_raw.csv")
    return df