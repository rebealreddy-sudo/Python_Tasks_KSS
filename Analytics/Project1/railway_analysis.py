
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load Dataset
df = pd.read_csv("railway_gauges.csv")

# Step 2: Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Step 3: Display column names
print("\nColumn Names:")
print(df.columns)

# Step 4: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 5: Fill missing values
df = df.fillna(0)

# Step 6: Convert gauge columns to numeric
cols = ["Broad Gauge", "Metre Gauge",
        "Narrow Gauge", "Total"]

for col in cols:
    df[col] = pd.to_numeric(df[col])

print("\nData Types:")
print(df.dtypes)

print("\nDataset Cleaning Completed!")

# =====================================
# SCENARIO 2: SIMPLE VISUALIZATION
# =====================================

print("\nSCENARIO 2: RAILWAY TRACK GROWTH")

# 1. Extract Year and Total columns
year = df["Year"]
total = df["Total"]

# 2. Create line graph
plt.figure(figsize=(12, 6))

plt.plot(year, total, marker="o", 
         linestyle="-", label="Total Railway Tracks")

# 3. Add graph title
plt.title("Growth of Total Railway Tracks Over Years")

# 4. Add X-axis and Y-axis labels
plt.xlabel("Year")
plt.ylabel("Total Railway Tracks")

# 5. Rotate year labels
plt.xticks(rotation=45)

# 6. Add legend and grid
plt.legend()
plt.grid(True)

# 7. Adjust graph layout
plt.tight_layout()

# 8. Save graph
plt.savefig("Graphs/railway_growth.png")

# 9. Display graph
plt.show()

# 10. Identify trend
if total.iloc[-1] > total.iloc[0]:
    print("\nRailway track trend is INCREASING")
else:
    print("\nRailway track trend is DECREASING")

# =====================================
# SCENARIO 3: FILTERING + BAR CHART
# =====================================

print("\nSCENARIO 3: GAUGE COMPARISON AFTER 2000")

# Step 1: Filter years after 2000
df_after_2000 = df[
    df["Year"].str[:4].astype(int) > 2000
]

# Step 2: Select gauge columns
years = df_after_2000["Year"]

broad = df_after_2000["Broad Gauge"]
metre = df_after_2000["Metre Gauge"]
narrow = df_after_2000["Narrow Gauge"]

# Step 3: Create positions for bars
x = np.arange(len(years))
width = 0.25

# Step 4: Create grouped bar chart
plt.figure(figsize=(12, 6))

plt.bar(x - width, broad, width,
        label="Broad Gauge")

plt.bar(x, metre, width,
        label="Metre Gauge")

plt.bar(x + width, narrow, width,
        label="Narrow Gauge")

# Step 5: Add title and labels
plt.title("Railway Gauge Comparison After 2000")
plt.xlabel("Year")
plt.ylabel("Track Values")

# Step 6: Display year labels
plt.xticks(x, years, rotation=45)

# Step 7: Add legend and grid
plt.legend()
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

# Step 8: Save graph
plt.savefig("Graphs/gauge_comparison_after_2000.png")

# Step 9: Display graph
plt.show()

# Step 10: Identify dominating gauge
gauge_totals = df_after_2000[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].sum()

print("\nGauge Totals After 2000:")
print(gauge_totals)

print("\nDominating Gauge:")
print(gauge_totals.idxmax())

# =====================================
# SCENARIO 4: FEATURE ENGINEERING
# =====================================

print("\nSCENARIO 4: GAUGE CONTRIBUTION")

# Step 1: Calculate total of each gauge
gauge_sum = df[
    ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
].sum()

# Step 2: Display gauge totals
print("\nTotal Contribution:")
print(gauge_sum)

# Step 3: Create Pie Chart
plt.figure(figsize=(8, 6))

plt.pie(
    gauge_sum,
    labels=gauge_sum.index,
    autopct="%1.1f%%",
    startangle=90
)

# Step 4: Add title
plt.title("Railway Gauge Contribution")

# Step 5: Save graph
plt.savefig("Graphs/gauge_contribution.png")

# Step 6: Display graph
plt.show()

# Step 7: Identify highest contribution
print("\nHighest Contributing Gauge:")
print(gauge_sum.idxmax())

# ============================================
# SCENARIO 5: ADVANCED ANALYSIS
# ============================================

print("\nSCENARIO 5: ADVANCED RAILWAY ANALYSIS")

# PART 1: FEATURE ENGINEERING

# Calculate percentage of each gauge
df["% Broad Gauge"] = (
    df["Broad Gauge"] / df["Total"] * 100
)

df["% Metre Gauge"] = (
    df["Metre Gauge"] / df["Total"] * 100
)

df["% Narrow Gauge"] = (
    df["Narrow Gauge"] / df["Total"] * 100
)

print("\nGauge Percentage:")
print(df[["Year", "% Broad Gauge",
          "% Metre Gauge", "% Narrow Gauge"]].head())

# PART 2: NUMPY ANALYSIS

total_array = df["Total"].to_numpy()

yearly_growth = np.diff(total_array)

print("\nYearly Growth:")
print(yearly_growth)

# Find highest growth
growth_index = np.argmax(yearly_growth)

print("\nHighest Growth Year:")
print(df["Year"].iloc[growth_index + 1])

print("Highest Growth Value:")
print(yearly_growth[growth_index])

# PART 3: LINE GRAPH

plt.figure(figsize=(12, 6))

plt.plot(df["Year"], df["% Broad Gauge"],
         marker="o", label="Broad Gauge")

plt.plot(df["Year"], df["% Metre Gauge"],
         marker="o", label="Metre Gauge")

plt.plot(df["Year"], df["% Narrow Gauge"],
         marker="o", label="Narrow Gauge")

plt.title("Railway Gauge Percentage Trend")
plt.xlabel("Year")
plt.ylabel("Percentage (%)")

plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("Graphs/gauge_percentage_trend.png")
plt.show()

# PART 4: STACKED BAR CHART

plt.figure(figsize=(12, 6))

plt.bar(df["Year"], df["Broad Gauge"],
        label="Broad Gauge")

plt.bar(df["Year"], df["Metre Gauge"],
        bottom=df["Broad Gauge"],
        label="Metre Gauge")

plt.bar(df["Year"], df["Narrow Gauge"],
        bottom=df["Broad Gauge"] + df["Metre Gauge"],
        label="Narrow Gauge")

plt.title("Railway Gauge Composition")
plt.xlabel("Year")
plt.ylabel("Track Values")

plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig("Graphs/gauge_stacked_bar.png")
plt.show()

# PART 5: DECLINE ANALYSIS

print("\nGAUGE DECLINE ANALYSIS")

for col in ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]:
    change = df[col].iloc[-1] - df[col].iloc[0]
    print(col, "Overall Change:", change)

# PART 6: FINAL CONCLUSION

print("\nFINAL CONCLUSION")

if df["% Broad Gauge"].iloc[-1] > df["% Broad Gauge"].iloc[0]:
    print("Railway system is shifting towards Broad Gauge.")
else:
    print("Broad Gauge percentage has not increased.")
