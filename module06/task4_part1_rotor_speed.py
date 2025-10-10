"""
Task 4 – Part 1 (46W38 Scientific Programming in Wind Energy)
Goal: Plot time series of rotor speed for three turbines on one chart.

Assumptions:
- Excel file "Module 6 - Exercises Data.xlsx" is in the same folder as this script.
- Sheets: "Exercise 4 - Baseline", "Exercise 4 - A", "Exercise 4 - B".
- Columns used: "Time (s)", "Rotor speed (rpm)".
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    excel = Path(__file__).parent / "Module 6 - Exercises Data.xlsx"
    sheets = ["Exercise 4 - Baseline", "Exercise 4 - A", "Exercise 4 - B"]
    time_col = "Time (s)"
    value_col = "Rotor speed (rpm)"

    # Load all three sheets
    data = {s: pd.read_excel(excel, sheet_name=s) for s in sheets}

    # Single figure with all series
    fig, ax = plt.subplots(figsize=(10, 5))
    for s in sheets:
        df = data[s]
        ax.plot(df[time_col].values, df[value_col].values, label=s)

    ax.set_xlabel(time_col)
    ax.set_ylabel(value_col)
    ax.set_title("Exercise 4 — Rotor speed vs Time (Baseline vs A vs B)")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend(title="Turbine")

    # Save and show
    out_png = Path(__file__).parent / "module06_task4_part1_rotor_speed.png"
    plt.savefig(out_png, dpi=200, bbox_inches="tight")
    print(f"✅ Plot saved as {out_png}")
    plt.show()

if __name__ == "__main__":
    main()