# Student Performance Data Pipeline

A Python-based ETL pipeline that processes student performance data.

## Project Objective

The objective of this project is to collect, transform, and process student performance data using Python and Pandas.

## Technologies Used

- Python
- Pandas
- CSV
- ETL

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
│   ├── transform.py
│   └── load.py
│
├── .venv/
└── README.md

## ETL Workflow

### 1. Extract
The pipeline reads raw student data from a CSV file using Pandas.

### 2. Transform
The pipeline:
- Calculates total marks
- Calculates percentage
- Assigns grades
- Determines Pass/Fail status
- Checks attendance eligibility

### 3. Load
The transformed data is saved as a processed CSV file.

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
3. Run the following command:

```bash
python src/main.py

data/processed/students_processed.csv