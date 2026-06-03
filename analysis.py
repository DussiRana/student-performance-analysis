# ============================================================
#  Student Performance Analysis
#  Author  : Dushyant Rana
#  Tools   : Python, pandas, matplotlib
#  Dataset : students.csv (included in this project)
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import os

# ----------------------------------------------------------
# 1. Load the dataset
# ----------------------------------------------------------
df = pd.read_csv("students.csv")

print("=" * 50)
print("   STUDENT PERFORMANCE ANALYSIS")
print("=" * 50)

# ----------------------------------------------------------
# 2. Basic info about the dataset
# ----------------------------------------------------------
print("\n[INFO] First 5 rows of the dataset:")
print(df.head())

print(f"\n[INFO] Total students: {len(df)}")
print(f"[INFO] Columns: {list(df.columns)}")

# ----------------------------------------------------------
# 3. Check for missing values
# ----------------------------------------------------------
print("\n[INFO] Missing values in each column:")
print(df.isnull().sum())

# Drop rows where marks are missing (data cleaning)
df = df.dropna(subset=["Math", "Science", "English", "Hindi", "Computer"])
print(f"\n[INFO] Rows after cleaning: {len(df)}")

# ----------------------------------------------------------
# 4. Calculate total marks and percentage
# ----------------------------------------------------------
subjects = ["Math", "Science", "English", "Hindi", "Computer"]
max_marks_per_subject = 100
total_max = max_marks_per_subject * len(subjects)

df["Total"] = df[subjects].sum(axis=1)
df["Percentage"] = (df["Total"] / total_max) * 100
df["Percentage"] = df["Percentage"].round(2)

# ----------------------------------------------------------
# 5. Assign grades
# ----------------------------------------------------------
def assign_grade(pct):
    if pct >= 90:
        return "A+"
    elif pct >= 80:
        return "A"
    elif pct >= 70:
        return "B"
    elif pct >= 60:
        return "C"
    elif pct >= 40:
        return "D"
    else:
        return "F"

df["Grade"] = df["Percentage"].apply(assign_grade)

# ----------------------------------------------------------
# 6. Summary statistics
# ----------------------------------------------------------
print("\n[RESULTS] Subject-wise Average Marks:")
for subject in subjects:
    avg = df[subject].mean()
    print(f"  {subject:<12}: {avg:.2f} / 100")

print("\n[RESULTS] Top 3 Students:")
top3 = df.nlargest(3, "Percentage")[["Name", "Total", "Percentage", "Grade"]]
print(top3.to_string(index=False))

print("\n[RESULTS] Bottom 3 Students (need improvement):")
bottom3 = df.nsmallest(3, "Percentage")[["Name", "Total", "Percentage", "Grade"]]
print(bottom3.to_string(index=False))

print("\n[RESULTS] Grade Distribution:")
print(df["Grade"].value_counts().sort_index())

print(f"\n[RESULTS] Class Average Percentage: {df['Percentage'].mean():.2f}%")
print(f"[RESULTS] Highest Score: {df['Percentage'].max():.2f}%")
print(f"[RESULTS] Lowest Score : {df['Percentage'].min():.2f}%")

# ----------------------------------------------------------
# 7. Save cleaned data to a new CSV
# ----------------------------------------------------------
df.to_csv("students_results.csv", index=False)
print("\n[INFO] Results saved to students_results.csv")

# ----------------------------------------------------------
# 8. Charts — saved as PNG files
# ----------------------------------------------------------
os.makedirs("charts", exist_ok=True)

# Chart 1: Subject-wise average bar chart
avg_marks = df[subjects].mean()
plt.figure(figsize=(8, 5))
bars = plt.bar(avg_marks.index, avg_marks.values, color=["#3498db","#2ecc71","#e74c3c","#f39c12","#9b59b6"])
plt.title("Subject-wise Average Marks", fontsize=14, fontweight="bold")
plt.xlabel("Subject")
plt.ylabel("Average Marks (out of 100)")
plt.ylim(0, 100)
for bar, val in zip(bars, avg_marks.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f"{val:.1f}", ha="center", fontsize=10)
plt.tight_layout()
plt.savefig("charts/subject_avg.png")
plt.close()
print("[INFO] Chart saved: charts/subject_avg.png")

# Chart 2: Grade distribution pie chart
grade_counts = df["Grade"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(grade_counts.values, labels=grade_counts.index, autopct="%1.1f%%",
        colors=["#2ecc71","#3498db","#f39c12","#e74c3c","#9b59b6","#1abc9c"])
plt.title("Grade Distribution", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("charts/grade_distribution.png")
plt.close()
print("[INFO] Chart saved: charts/grade_distribution.png")

# Chart 3: Top 10 students percentage bar chart
top10 = df.nlargest(10, "Percentage")
plt.figure(figsize=(10, 5))
plt.barh(top10["Name"], top10["Percentage"], color="#3498db")
plt.xlabel("Percentage (%)")
plt.title("Top 10 Students by Percentage", fontsize=14, fontweight="bold")
plt.xlim(0, 100)
plt.tight_layout()
plt.savefig("charts/top10_students.png")
plt.close()
print("[INFO] Chart saved: charts/top10_students.png")

print("\n[DONE] Analysis complete!")
