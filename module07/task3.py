# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import weibull_min

# --- Load Data for Task 3 ---
df_annual_wind = pd.read_excel('Module 7 - Exercises data.xlsx', sheet_name='Exercise 3')
wind_speed_annual = df_annual_wind['Wind Speed (m/s)'].values

# --- Part 1: Plot a histogram ---
plt.figure(figsize=(12, 7))

# Plot the histogram. 'density=True' normalizes it to form a probability density.
# 'bins='auto'' is a good way to get a reasonable number of bins.
plt.hist(wind_speed_annual, bins='auto', density=True, alpha=0.7, label='Measured Data Histogram')

# --- Part 2: Fit the Weibull parameters ---
# Use the fit() method from weibull_min to find the shape and scale parameters.
# floc=0 sets the location parameter to 0, which is standard for wind speed.
shape, loc, scale = weibull_min.fit(wind_speed_annual, floc=0)

# --- Part 3: Create and plot the Weibull PDF ---
# Create a range of wind speeds for plotting the PDF curve
v_range = np.linspace(wind_speed_annual.min(), wind_speed_annual.max(), 500)

# Calculate the PDF using the fitted parameters
weibull_pdf = weibull_min.pdf(v_range, shape, loc=loc, scale=scale)

# Overlay the PDF plot on the histogram
plt.plot(v_range, weibull_pdf, 'r-', linewidth=2, label='Fitted Weibull PDF')

# Add labels and title
plt.title('Wind Speed Distribution and Fitted Weibull PDF')
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.savefig('weibull_fit.png')
plt.show()

# Print the fitted parameters
print(f"Fitted Weibull Parameters:")
print(f"Shape (k): {shape:.4f}")
print(f"Scale (A): {scale:.4f}")