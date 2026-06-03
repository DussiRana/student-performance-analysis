#  Student Performance Analysis

A beginner-friendly **Python Data Analytics** project that analyzes student marks, calculates grades, and creates visual charts.

##  Technologies Used
- **Python 3**
- **pandas** — for data loading, cleaning, and analysis
- **matplotlib** — for charts and visualization
- **CSV** — dataset format

##  Project Structure
```
student_analysis/
│
├── analysis.py          # Main Python script
├── students.csv         # Dataset (20 students, 5 subjects)
├── students_results.csv # Output: cleaned data with grades (auto-generated)
├── charts/
│   ├── subject_avg.png          # Bar chart: subject-wise average
│   ├── grade_distribution.png   # Pie chart: grade breakdown
│   └── top10_students.png       # Bar chart: top 10 students
└── README.md
```

## Features
<!-- - Loads and cleans student data from CSV
- Calculates total marks and percentage for each student
- Assigns grades (A+, A, B, C, D, F)
- Shows top 3 and bottom 3 students
- Displays subject-wise class averages
- Saves 3 charts as PNG images -->




##  Sample Output
```
[RESULTS] Subject-wise Average Marks:
  Math        : 72.40 / 100
  Science     : 73.75 / 100
  English     : 71.45 / 100
  Hindi       : 70.80 / 100
  Computer    : 73.50 / 100

[RESULTS] Top 3 Students:
       Name  Total  Percentage Grade
Kavya Iyer    474       94.80    A+
Ananya Joshi  469       93.80    A+
Priya Singh   462       92.40    A+

Class Average: 72.41%
```

## 👤 Author
**Dushyant Rana**  
BCA Student | Aspiring Data Analyst  
[LinkedIn](https://linkedin.com/in/dushyantrana1608)
