import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])

# Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

print(df)

# Bar Chart
plt.bar(products, sales)

plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()
