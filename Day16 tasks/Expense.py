import numpy as np
import matplotlib.pyplot as plt

# Create data
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]

# Pie Chart
plt.pie(expenses, labels=labels, autopct='%1.1f%%')

plt.title("Monthly Expense Distribution")

plt.show()
