"""
Task 4 – Parts 2–4 (46W38 Scientific Programming in Wind Energy)
Goal:
1) Compute standard deviations of time-series output metrics for each turbine.
2) Compare graphically in two ways:
   - Raw standard deviations (clustered bars)
   - Normalized vs Baseline: ((std_variant / std_baseline) - 1) * 100 [%]
3) Provide a clear visualization to show differences (normalized plot is recommended).

Assumptions:
- Excel "Module 6 - Exercises Data.xlsx" is in the same folder as this script.
- Sheets exist: "Exercise 4 - Baseline", "Exercise 4 - A", "Exercise 4 - B".
- Time column is "Time (s)"; all other columns are output metrics.
"""

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    # --- Load data ---
    excel = Path(__file__).parent / "Module 6 - Exercises Data.xlsx"
    sheets = {"Baseline": "Exercise 4 - Baseline", "A": "Exercise 4 - A", "B": "Exercise 4 - B"}
    dfs = {k: pd.read_excel(excel, sheet_name=v) for k, v in sheets.items()}

    # --- Define metrics (exclude time) ---
    time_col = "Time (s)"
    metrics = [c for c in dfs["Baseline"].columns if c != time_col]

    # --- Compute standard deviations (sample std, ddof=1) ---
    std_df = pd.DataFrame({k: df[metrics].std(ddof=1) for k, df in dfs.items()})
    std_df = std_df.loc[metrics]  # keep column order consistent

    # Save numeric results for the report
    out_dir = Path(__file__).parent
    std_csv = out_dir / "module06_task4_std_values.csv"
    std_df.to_csv(std_csv, float_format="%.6f")

    # --- Raw std deviations (clustered bars) ---
    x = np.arange(len(metrics))
    width = 0.25
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.bar(x - width, std_df["Baseline"].values, width, label="Baseline")
    ax1.bar(x,         std_df["A"].values,        width, label="A")
    ax1.bar(x + width, std_df["B"].values,        width, label="B")
    ax1.set_xticks(x)
    ax1.set_xticklabels(metrics, rotation=20, ha="right")
    ax1.set_ylabel("Standard deviation [units vary]")
    ax1.set_title("Exercise 4 — Raw standard deviations by metric and turbine")
    ax1.grid(True, axis="y", linestyle="--", alpha=0.4)
    ax1.legend()
    raw_png = out_dir / "module06_task4_std_raw.png"
    plt.tight_layout()
    plt.savefig(raw_png, dpi=200, bbox_inches="tight")

    # --- Normalized vs Baseline (percent change) ---
    norm_pct = pd.DataFrame(index=metrics)
    norm_pct["A vs Baseline (%)"] = (std_df["A"] / std_df["Baseline"] - 1.0) * 100.0
    norm_pct["B vs Baseline (%)"] = (std_df["B"] / std_df["Baseline"] - 1.0) * 100.0
    norm_csv = out_dir / "module06_task4_std_normalized_percent.csv"
    norm_pct.to_csv(norm_csv, float_format="%.6f")

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    width2 = 0.35
    ax2.bar(x - width2 / 2, norm_pct["A vs Baseline (%)"].values, width2, label="A vs Baseline")
    ax2.bar(x + width2 / 2, norm_pct["B vs Baseline (%)"].values, width2, label="B vs Baseline")
    ax2.axhline(0, linewidth=1)  # baseline reference
    ax2.set_xticks(x)
    ax2.set_xticklabels(metrics, rotation=20, ha="right")
    ax2.set_ylabel("Std dev change vs Baseline [%]")
    ax2.set_title("Exercise 4 — Normalized std devs vs Baseline (percent change)")
    ax2.grid(True, axis="y", linestyle="--", alpha=0.4)
    ax2.legend()
    norm_png = out_dir / "module06_task4_std_normalized_percent.png"
    plt.tight_layout()
    plt.savefig(norm_png, dpi=200, bbox_inches="tight")

    print(f"✅ Saved: {std_csv.name}, {norm_csv.name}, {raw_png.name}, {norm_png.name}")
    plt.show()


if __name__ == "__main__":
    main()