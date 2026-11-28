import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

# Create DataFrame
df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

print(df)

# 1. Line Graph
plt.plot(students, marks, marker='o')
plt.title("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 2. Bar Chart
plt.bar(students, marks)
plt.title("Student vs Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Pie Chart (Pass vs Fail)
passed = sum(marks > 50)
failed = sum(marks <= 50)

plt.pie([passed, failed], labels=["Pass", "Fail"],
        autopct='%1.1f%%')
plt.title("Pass vs Fail")
plt.show()

# 4. Histogram
plt.hist(marks, bins=5, edgecolor='black')
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot
plt.scatter(range(len(marks)), marks)
plt.title("Index vs Marks")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.show()
