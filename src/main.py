from extract import extract_data
from transform import transform_data
from load import load_data


# Extract
df = extract_data()

# Transform
df = transform_data(df)

# Load
load_data(df)