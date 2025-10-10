"""
Task 2 – Module 6 (46W38 Scientific Programming in Wind Energy)
Goal: Plot turbine metrics vs. wind speed from 'Exercise 2' sheet.

Assumptions:
- The Excel file "Module 6 - Exercises Data.xlsx" is in the same folder as this script.
- The sheet name is exactly "Exercise 2".
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Path to Excel file (same folder as the script)
excel_path = Path(__file__).parent / "Module 6 - Exercises Data.xlsx"
sheet_name = "Exercise 2"

# Read Excel data
df = pd.read_excel(excel_path, sheet_name=sheet_name)

# Detect wind speed column (first matching or first column)
possible_ws = [
    c for c in df.columns
    if str(c).strip().lower() in ("wind speed", "windspeed", "wind_speed", "ws", "u")
]
ws_col = possible_ws[0] if possible_ws else df.columns[0]

# Define data
wind_speed = df[ws_col].values
metric_cols = [c for c in df.columns if c != ws_col]

# Plot
fig, ax = plt.subplots(figsize=(9, 5))
for col in metric_cols:
    ax.plot(wind_speed, df[col].values, marker="o", label=str(col))

ax.set_xlabel(f"{ws_col} [m/s]")
ax.set_ylabel("Metric value [units]")
ax.set_title("Turbine Metrics vs. Wind Speed — Exercise 2")
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(title="Metrics")

# Save and show
out_path = Path(__file__).parent / "module06_task2_metrics_vs_windspeed.png"
plt.savefig(out_path, dpi=200, bbox_inches="tight")
print(f"✅ Plot saved as {out_path}")
plt.show()