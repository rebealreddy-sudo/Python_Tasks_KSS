import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]

# Create DataFrame
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print(df)

# Line Graph
plt.plot(months, sales, marker='o')

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()
