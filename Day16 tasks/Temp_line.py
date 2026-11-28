import pandas as pd
import matplotlib.pyplot as plt

# Create data
temps = [28, 30, 32, 31, 29]

# Convert into Pandas Series
s = pd.Series(temps)

print(s)

# Line Graph
plt.plot(s, marker='o')

plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature")

plt.grid(True)

plt.show()
