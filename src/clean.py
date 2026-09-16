def clean_data(df):

    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove rows with missing values
    df = df.dropna()

    return df