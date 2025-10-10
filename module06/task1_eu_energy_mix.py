# Task 1 – EU Energy Mix (2023)
# Course: 46W38 Scientific Programming in Wind Energy
# Topic: Basic plotting with matplotlib

import matplotlib.pyplot as plt

def main():
    # Data: EU total energy generation by source (2023, %)
    labels = ["Crude oil", "Natural gas", "Renewable energy", "Solid fuels", "Nuclear energy"]
    values = [37.7, 20.4, 19.5, 10.6, 11.8]

    # Create a pie chart
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    # Keep the pie chart circular
    ax.axis("equal")
    ax.set_title("EU Energy Generation Mix (2023)")

    # Save figure to file
    output_file = "eu_energy_mix_2023.png"
    plt.savefig(output_file, dpi=200, bbox_inches="tight")
    print(f"Plot saved as {output_file}")

    # Optional: show the plot
    plt.show()

if __name__ == "__main__":
    main()