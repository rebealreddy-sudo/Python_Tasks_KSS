import pandas as pd
import matplotlib.pyplot as plt

# Create data
data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Store_A": [100, 150, 200],
    "Store_B": [90, 140, 210]
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)

# Multi-Line Graph
plt.plot(df["Month"], df["Store_A"], marker='o', label="Store A")

plt.plot(df["Month"], df["Store_B"], marker='o', label="Store B")

plt.title("Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.legend()

plt.show()
