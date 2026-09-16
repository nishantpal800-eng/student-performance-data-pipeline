def transform_data(df):

    df["total_marks"] = (
        df["maths"] +
        df["physics"] +
        df["chemistry"]
    )

    df["percentage"] = ((df["total_marks"] / 300) * 100).round(2)

    df["grade"] = df["percentage"].apply(calculate_grade)

    df["status"] = df["grade"].apply(
    lambda grade: "Pass" if grade != "F" else "Fail"
)

    df["attendance_status"] = df["attendance"].apply(
    lambda attendance: "Eligible" if attendance >= 75 else "Not Eligible"
)

    return df

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"