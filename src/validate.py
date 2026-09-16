def validate_data(df):

    if not df["maths"].between(0, 100).all():
        raise ValueError("Invalid Maths marks")

    if not df["physics"].between(0, 100).all():
        raise ValueError("Invalid Physics marks")

    if not df["chemistry"].between(0, 100).all():
        raise ValueError("Invalid Chemistry marks")

    if not df["attendance"].between(0, 100).all():
        raise ValueError("Invalid attendance values")

    return df