import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def load_data(df):

    df.to_csv("data/processed/students_processed.csv", index=False)

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="student_performance"
    )

    cursor = connection.cursor()

    query = """
    INSERT INTO students (
        student_id, name, gender, maths, physics, chemistry,
        attendance, total_marks, percentage, grade, status, attendance_status
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        name = VALUES(name),
        gender = VALUES(gender),
        maths = VALUES(maths),
        physics = VALUES(physics),
        chemistry = VALUES(chemistry),
        attendance = VALUES(attendance),
        total_marks = VALUES(total_marks),
        percentage = VALUES(percentage),
        grade = VALUES(grade),
        status = VALUES(status),
        attendance_status = VALUES(attendance_status)
    """

    for row in df.itertuples(index=False):
        cursor.execute(query, tuple(row))

    connection.commit()

    cursor.close()
    connection.close()

    print("Data loaded into MySQL successfully!")