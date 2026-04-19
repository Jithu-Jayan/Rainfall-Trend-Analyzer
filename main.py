import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# --- Step 3: Load and clean ---
df = pd.read_csv("data/rainfall.csv")
print("Missing values:\n", df.isnull().sum())
df = df.fillna(0)

# --- Step 4: Annual trend (all of India averaged) ---
yearly = df.groupby("YEAR")["ANNUAL"].mean()

slope, intercept, r, p, se = stats.linregress(yearly.index, yearly.values)
print(f"\nTrend: {slope:.2f} mm per year")
if slope > 0:
    print("Rainfall is INCREASING over time")
else:
    print("Rainfall is DECREASING over time")

# --- Step 5: Seasonal averages ---
months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
monthly_avg = df[months].mean()

# --- Step 6: Chart 1 - Monthly average rainfall ---
plt.figure(figsize=(10, 5))
monthly_avg.plot(kind="bar", color="steelblue")
plt.title("Average Rainfall by Month (All Subdivisions)")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.tight_layout()
plt.savefig("monthly_chart.png")
plt.show()

# --- Chart 2 - Annual trend over years ---
plt.figure(figsize=(10, 5))
yearly.plot(color="teal")
plt.title("Annual Rainfall Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Rainfall (mm)")
plt.tight_layout()
plt.savefig("trend_chart.png")
plt.show()

print("\nDone! Charts saved.")

# --- Chart 3: Seasonal Heatmap ---


months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
heatmap_data = df.groupby("SUBDIVISION")[months].mean()

plt.figure(figsize=(14, 10))
sns.heatmap(heatmap_data, cmap="Blues", linewidths=0.5)
plt.title("Average Monthly Rainfall by Subdivision")
plt.xlabel("Month")
plt.ylabel("Subdivision")
plt.tight_layout()
plt.savefig("heatmap.png")
plt.show()