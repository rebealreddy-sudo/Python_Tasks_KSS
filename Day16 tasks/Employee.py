import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

# Create DataFrame
df = pd.DataFrame({
    "Department": departments,
    "Salary": salaries
})

print(df)

# 1. Line Graph
plt.plot(range(len(salaries)), salaries, marker='o')
plt.title("Employee Salary Trend")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.show()

# 2. Bar Chart
plt.bar(departments, salaries)
plt.title("Department-wise Salary Comparison")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()

# 3. Pie Chart
dept_counts = df["Department"].value_counts()

plt.pie(dept_counts.values,
        labels=dept_counts.index,
        autopct='%1.1f%%')
plt.title("Department Distribution")
plt.show()

# 4. Histogram
plt.hist(salaries, bins=5, edgecolor='black')
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot
plt.scatter(range(len(salaries)), salaries)
plt.title("Employee Index vs Salary")
plt.xlabel("Index")
plt.ylabel("Salary")
plt.show()
