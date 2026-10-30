"""
functions.py
Reusable helper functions for the Student Performance Analytics System.
"""

import numpy as np
import pandas as pd


SUBJECTS = ["Maths", "Python", "Data_Science", "English", "Physics"]

PASS_MARK = 40           
MIN_ATTENDANCE = 75      


def load_data(file_path):
    """Read the CSV file into a DataFrame."""
    return pd.read_csv(file_path)


def calculate_total_and_average(df):
    """Add Total and Average columns for every student."""
    marks = df[SUBJECTS].to_numpy()                
    df["Total"] = np.sum(marks, axis=1)            
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    return df


def get_grade(average):
    """Return a grade letter for one average mark (grading rule below)."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


def assign_grades(df):
    """Loop through every student's average and store the grade."""
    grades = []
    for avg in df["Average"]:
        grades.append(get_grade(avg))
    df["Grade"] = grades
    return df


def check_pass_fail(df):
    """A student passes only if they score >= PASS_MARK in all subjects."""
    results = []
    for _, row in df.iterrows():
        passed_all = True
        for subject in SUBJECTS:
            if row[subject] < PASS_MARK:
                passed_all = False
                break
        results.append("Pass" if passed_all else "Fail")
    df["Result"] = results
    return df


def flag_low_attendance(df):
    """Mark students whose attendance is under the minimum required."""
    df["Attendance_Status"] = np.where(
        df["Attendance"] >= MIN_ATTENDANCE, "OK", "Shortage"
    )
    return df


def class_statistics(df):
    """Highest, lowest and overall class average (returned as a dict)."""
    top = df.loc[df["Average"].idxmax()]
    bottom = df.loc[df["Average"].idxmin()]
    return {
        "highest_name": top["Name"],
        "highest_avg": top["Average"],
        "lowest_name": bottom["Name"],
        "lowest_avg": bottom["Average"],
        "class_average": round(float(np.mean(df["Average"])), 2),
        "class_std": round(float(np.std(df["Average"])), 2),
    }


def pass_fail_summary(df):
    """Count passed / failed students and the pass percentage."""
    passed = int((df["Result"] == "Pass").sum())
    failed = int((df["Result"] == "Fail").sum())
    percentage = round(passed / len(df) * 100, 2)
    return passed, failed, percentage


def subject_analysis(df):
    """Average, highest and lowest marks for each subject."""
    rows = []
    for subject in SUBJECTS:
        column = df[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(column)), 2),
            "Highest": int(np.max(column)),
            "Lowest": int(np.min(column)),
            "Failed": int(np.sum(column < PASS_MARK)),
        })
    return pd.DataFrame(rows).sort_values("Average", ascending=False)


def top_performers(df, n=5):
    """Return the top n students ranked by average marks."""
    ranked = df.sort_values("Average", ascending=False).head(n)
    return ranked[["Student_ID", "Name", "Department", "Total", "Average", "Grade"]]


def department_analysis(df):
    """Average marks and pass count per department."""
    summary = df.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Avg_Marks=("Average", "mean"),
        Avg_Attendance=("Attendance", "mean"),
    ).round(2)
    summary["Passed"] = df[df["Result"] == "Pass"].groupby("Department").size()
    summary["Passed"] = summary["Passed"].fillna(0).astype(int)
    return summary
