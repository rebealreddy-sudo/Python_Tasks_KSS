import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

# Create DataFrame
df = pd.DataFrame({
    "Student": names,
    "Marks": marks
})

print("Original Data:")
print(df)

# Filter marks greater than 50
filtered_df = df[df["Marks"] > 50]

print("Filtered Data:")
print(filtered_df)

# Bar Chart
plt.bar(filtered_df["Student"], filtered_df["Marks"])

plt.title("Students Scoring Above 50")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
