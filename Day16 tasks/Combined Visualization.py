import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

# Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

print(df)

# Create subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1. Line Graph
axes[0].plot(products, sales, marker='o')
axes[0].set_title("Sales Trend")
axes[0].set_xlabel("Products")
axes[0].set_ylabel("Sales")

# 2. Bar Chart
axes[1].bar(products, sales)
axes[1].set_title("Sales Comparison")
axes[1].set_xlabel("Products")
axes[1].set_ylabel("Sales")

# 3. Pie Chart
axes[2].pie(sales, labels=products, autopct='%1.1f%%')
axes[2].set_title("Sales Distribution")

# Display all graphs
plt.tight_layout()
plt.show()
