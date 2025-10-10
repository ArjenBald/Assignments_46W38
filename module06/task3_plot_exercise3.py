"""
Task 3 – Module 6 (46W38 Scientific Programming in Wind Energy)
Goal: Auto-plot Exercise 3 using a sensible default.
- If categorical + numeric -> bar
- Else if >=2 numeric -> scatter (first two)
- Else -> line by index
Data: 'Module 6 - Exercises Data.xlsx', sheet 'Exercise 3' (same folder).
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

excel_path = Path(__file__).parent / "Module 6 - Exercises Data.xlsx"
sheet = "Exercise 3"

df = pd.read_excel(excel_path, sheet_name=sheet)

num = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]
non = [c for c in df.columns if c not in num]

if non and num:
    # bar: first numeric vs first categorical
    x, y = df[non[0]].astype(str).values, df[num[0]].values
    kind, xlabel, ylabel = "bar", str(non[0]), str(num[0])
elif len(num) >= 2:
    # scatter: first two numeric
    x, y = df[num[0]].values, df[num[1]].values
    kind, xlabel, ylabel = "scatter", str(num[0]), str(num[1])
else:
    # line: single numeric vs index
    x, y = np.arange(len(df)), df[num[0]].values
    kind, xlabel, ylabel = "line", "Index", str(num[0])

fig, ax = plt.subplots(figsize=(9, 5))
if kind == "bar":
    ax.bar(x, y)
elif kind == "scatter":
    ax.scatter(x, y)
else:
    ax.plot(x, y, marker="o")

ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_title(f"Exercise 3 — {kind.capitalize()} plot")
ax.grid(True, linestyle="--", alpha=0.4)

if kind == "bar" and len(x) > 6:
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

out_path = Path(__file__).parent / "module06_task3_plot.png"
plt.savefig(out_path, dpi=200, bbox_inches="tight")
print(f"✅ Plot saved as {out_path}")
plt.show()