import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
scores = np.array([40, 60, 80, 30, 90])

# Categorize Pass and Fail
pass_count = np.sum(scores > 50)
fail_count = np.sum(scores <= 50)

# Create DataFrame
df = pd.DataFrame({
    "Category": ["Pass", "Fail"],
    "Count": [pass_count, fail_count]
})

print(df)

# Pie Chart
plt.pie(
    df["Count"],
    labels=df["Category"],
    autopct='%1.1f%%'
)

plt.title("Pass vs Fail")

plt.show()
