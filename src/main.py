from extract import extract_data
from transform import transform_data
from load import load_data
from clean import clean_data


# Extract
df = extract_data()
df = clean_data(df)

# Transform
df = transform_data(df)

# Load
load_data(df)