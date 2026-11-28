import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

# Create DataFrame
df = pd.DataFrame({
    "Student": names,
    "Marks": marks
})

print(df)

# Bar Chart
plt.bar(names, marks)

plt.title("Student Marks")
plt.xlabel("Student Names")
plt.ylabel("Marks")

plt.show()
