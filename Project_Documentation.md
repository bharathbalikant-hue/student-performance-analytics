# Project Documentation - Student Performance Analytics System

## 1. Project Title
Student Performance Analytics System
Student: <Your Name> | Roll No: <Your Roll No> | Course: Python with AI, EWB Courses

## 2. Objective
Teachers usually check marks by hand, which is slow and easy to get wrong. This project automates it: it reads student data and quickly reports totals, averages, grades, pass/fail status and which subjects or students need attention.

## 3. Technologies Used
Python 3, NumPy (numerical calculations), Pandas (DataFrames, grouping, sorting), VS Code, Git and GitHub.

## 4. Dataset Description
`students.csv` has 20 records with columns: Student_ID, Name, Department (CSE, ECE, IT, MECH), five subject marks (Maths, Python, Data_Science, English, Physics) and Attendance %. The marks were created by me to look realistic, with a mix of high, average and weak students.

## 5. Implementation
1. **Loading:** `pd.read_csv()` loads the file; I check the shape, column names and missing values.
2. **Totals and averages:** subject marks are converted to a NumPy array and `np.sum` / `np.mean` with `axis=1` give row-wise results.
3. **Grades:** a function `get_grade()` applies if/elif rules and a loop assigns it to every student.
4. **Pass/fail:** a nested loop checks every subject against the pass mark of 40.
5. **Attendance:** `np.where()` flags students below 75%.
6. **Analysis:** `idxmax`/`idxmin` find highest and lowest; a loop over subjects builds the subject-wise table; `groupby` gives the department summary.
7. **Output:** results are printed in sections and saved to `student_report.csv`.

## 6. Key Features
`load_data`, `calculate_total_and_average`, `get_grade`, `assign_grades`, `check_pass_fail`, `flag_low_attendance`, `class_statistics`, `pass_fail_summary`, `subject_analysis`, `top_performers`, `department_analysis`.

## 7. Output / Screenshots
See `screenshots/output.txt`. Add your own terminal screenshots here.

## 8. Final Outcome
The program runs without errors and answers every required question: Sneha Iyer has the highest average (93.0), the class average is 70.0, 17 of 20 students passed (85%), English is the best subject and Physics the weakest, and the MECH department needs the most support.

## 9. Challenges and Learning
- Harsha Vardhan had an average below 50 but passed every subject, so my first grade table showed "F" with "Pass". I fixed it by adding an "E" grade for 40-49, which taught me to test rules against edge cases.
- Choosing between loops and vectorised NumPy operations: I used loops where logic is per-student and NumPy for bulk maths.
- I learned DataFrame handling, groupby, writing reusable functions, and using Git.

## 10. GitHub Repository
https://github.com/bharathbalikant-hue/student-performance-analytics
