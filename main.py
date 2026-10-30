"""
Student Performance Analytics System
Run with:  python main.py
"""

import pandas as pd
import functions as fn


def line(title=""):
    print("\n" + "=" * 70)
    if title:
        print(title)
        print("=" * 70)


def main():
    pd.set_option("display.width", 120)
    pd.set_option("display.max_columns", None)

    
    df = fn.load_data("students.csv")
    line("1. DATASET OVERVIEW")
    print(f"Records : {df.shape[0]}")
    print(f"Columns : {list(df.columns)}")
    print(f"Missing values: {int(df.isnull().sum().sum())}")
    print("\nFirst 5 rows:")
    print(df.head())

    
    df = fn.calculate_total_and_average(df)
    df = fn.assign_grades(df)
    df = fn.check_pass_fail(df)
    df = fn.flag_low_attendance(df)

    line("2. STUDENT REPORT (Total, Average, Grade, Result)")
    print(df[["Student_ID", "Name", "Department", "Total", "Average",
              "Grade", "Result", "Attendance_Status"]].to_string(index=False))

    
    stats = fn.class_statistics(df)
    passed, failed, pct = fn.pass_fail_summary(df)

    line("3. CLASS PERFORMANCE")
    print(f"Highest average : {stats['highest_name']} ({stats['highest_avg']})")
    print(f"Lowest average  : {stats['lowest_name']} ({stats['lowest_avg']})")
    print(f"Class average   : {stats['class_average']}")
    print(f"Std deviation   : {stats['class_std']}")
    print(f"Passed: {passed} | Failed: {failed} | Pass %: {pct}%")

    line("4. GRADE DISTRIBUTION")
    print(df["Grade"].value_counts().sort_index().to_string())

    line("5. SUBJECT-WISE ANALYSIS")
    subjects = fn.subject_analysis(df)
    print(subjects.to_string(index=False))
    best = subjects.iloc[0]
    print(f"\nBest subject  : {best['Subject']} (avg {best['Average']})")
    weak = subjects.iloc[-1]
    print(f"Weakest subject: {weak['Subject']} (avg {weak['Average']})")

    line("6. TOP 5 PERFORMERS")
    print(fn.top_performers(df, 5).to_string(index=False))

    line("7. DEPARTMENT-WISE SUMMARY")
    print(fn.department_analysis(df))

    line("8. STUDENTS NEEDING ATTENTION")
    attention = df[(df["Result"] == "Fail") | (df["Attendance_Status"] == "Shortage")]
    print(attention[["Name", "Average", "Result", "Attendance"]].to_string(index=False))

    
    df.to_csv("student_report.csv", index=False)
    line()
    print("Full report saved to student_report.csv")


if __name__ == "__main__":
    main()
