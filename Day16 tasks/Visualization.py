import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
data = np.array([100, np.nan, 200, 150, np.nan, 300])

# Convert into Pandas Series
s = pd.Series(data)

print("Original Data:")
print(s)

# Calculate mean
avg = s.mean()

# Replace NaN with mean
cleaned_data = s.fillna(avg)

print("Cleaned Data:")
print(cleaned_data)

# Filter values greater than average
filtered_data = cleaned_data[cleaned_data > avg]

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 1. Line Graph
axes[0].plot(cleaned_data, marker='o')
axes[0].set_title("Cleaned Data Line Graph")
axes[0].set_xlabel("Index")
axes[0].set_ylabel("Values")
axes[0].grid(True)

# 2. Bar Chart
axes[1].bar(filtered_data.index, filtered_data.values)
axes[1].set_title("Values Above Average")
axes[1].set_xlabel("Index")
axes[1].set_ylabel("Values")

plt.tight_layout()
plt.show()
