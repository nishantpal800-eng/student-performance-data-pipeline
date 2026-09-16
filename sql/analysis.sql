-- Total number of students
SELECT COUNT(*) AS total_students
FROM students;

-- Number of passed students
SELECT COUNT(*) AS passed_students
FROM students
WHERE status = 'Pass';

-- Average student percentage
SELECT ROUND(AVG(percentage), 2) AS average_percentage
FROM students;

-- Average student percentage
SELECT ROUND(AVG(percentage), 2) AS average_percentage
FROM students;

-- Number of students in each grade
SELECT grade, COUNT(*) AS student_count
FROM students
GROUP BY grade
ORDER BY grade;

-- Attendance eligibility count
SELECT attendance_status, COUNT(*) AS student_count
FROM students
GROUP BY attendance_status;

-- Average marks in each subject
SELECT
    ROUND(AVG(maths), 2) AS average_maths,
    ROUND(AVG(physics), 2) AS average_physics,
    ROUND(AVG(chemistry), 2) AS average_chemistry
FROM students;

-- Average percentage by gender
SELECT
    gender,
    ROUND(AVG(percentage), 2) AS average_percentage
FROM students
GROUP BY gender;

-- Student with the highest attendance
SELECT name, attendance
FROM students
ORDER BY attendance DESC
LIMIT 1;

-- Students with attendance below 75%
SELECT name, attendance
FROM students
WHERE attendance < 75
ORDER BY attendance;