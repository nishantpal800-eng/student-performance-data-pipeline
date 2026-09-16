# Student Performance Data Pipeline

A Python-based ETL pipeline that extracts, cleans, validates, transforms, and loads student performance data into MySQL.

## Project Objective

This project aims to build a simple data pipeline that reads student data, cleans errors and missing values, validates the data, calculates results, and prepares the data for analysis and reporting.

## Technologies Used

- Python
- Pandas
- MySQL
- SQL
- CSV
- python-dotenv
- Git & GitHub

## Project Structure

```text
Student Performance Data Pipeline/
├── data/
│   ├── raw/
│   │   └── students_raw.csv
│   └── processed/
│       └── students_processed.csv
│
├── src/
│   ├── main.py
│   ├── extract.py
│   ├── clean.py
│   ├── validate.py
│   ├── transform.py
│   └── load.py
│
├── sql/
│   └── analysis.sql
│
├── .venv/
├── .env
├── .gitignore
├── requirements.txt
└── README.md

## ETL Workflow

### 1. Extract

The pipeline reads raw student performance data from a CSV file using Pandas.

### 2. Clean

The pipeline:
- Removes duplicate records
- Removes rows containing missing values

### 3. Validate

The pipeline validates:
- Mathematics marks
- Physics marks
- Chemistry marks
- Attendance values

All values must be within valid ranges.

### 4. Transform

The pipeline:
- Calculates total marks
- Calculates percentage
- Assigns grades
- Determines Pass/Fail status
- Determines attendance eligibility

### 5. Load

The processed data is:
- Saved as a processed CSV file
- Loaded into a MySQL database

## SQL Analysis

The project includes SQL queries for:

- Total number of students
- Number of passed students
- Average percentage
- Highest percentage
- Grade-wise student count
- Attendance eligibility
- Subject-wise average marks
- Average percentage by gender
- Highest attendance
- Students with attendance below 75%

## Database

Database name:

```text
student_performance
```

Table name:

```text
students
```

## Data Fields

| Field | Description |
|---|---|
| student_id | Unique ID of the student |
| name | Student name |
| gender | Student gender |
| maths | Marks obtained in Mathematics |
| physics | Marks obtained in Physics |
| chemistry | Marks obtained in Chemistry |
| attendance | Attendance percentage |
| total_marks | Total marks in three subjects |
| percentage | Overall percentage |
| grade | Grade based on percentage |
| status | Pass or Fail |
| attendance_status | Attendance eligibility |

## How to Run

1. Open the project folder in VS Code.
2. Activate the virtual environment.
3. Make sure MySQL is running.
4. Configure the MySQL password in the `.env` file.
5. Run:

```bash
python src/main.py
```

The pipeline will process the raw data, save the processed CSV, and load the data into MySQL.

## Security

The MySQL password is stored in the `.env` file and is excluded from Git using `.gitignore`.

## Author

Nishant Pal