def load_data(df):
    df.to_csv("data/processed/students_processed.csv", index=False)
    print("Processed data saved successfully!")