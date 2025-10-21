# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from scipy.interpolate import interp1d

# --- Data Loading and Filtering (from Task 1) ---

# Load data from the Excel file
df_wind = pd.read_excel('Module 7 - Exercises data.xlsx', sheet_name='Exercise 1')
df_pitch = pd.read_excel('Module 7 - Exercises data.xlsx', sheet_name='Exercise 2')

# Extract time and wind speed data
time = df_wind['Time (s)'].values
wind_speed = df_wind['Wind speed (m/s)'].values

# Apply the chosen low-pass filter from Task 1
sampling_interval = time[1] - time[0]
sampling_frequency = 1 / sampling_interval
filter_order = 4
cutoff_freq = 1.0 # The suitable cutoff frequency we determined
b, a = butter(filter_order, cutoff_freq, btype='low', analog=False, fs=sampling_frequency)
filtered_wind_speed = filtfilt(b, a, wind_speed)

# --- Task 2, Part 1: Plot pitch curve and create interpolation function ---

# Extract pitch curve data
pitch_curve_wind_speed = df_pitch['Wind speed (m/s)'].values
blade_pitch = df_pitch['Blade pitch (degrees)'].values

# Plot the blade pitch vs. wind speed curve
plt.figure(figsize=(12, 6))
plt.plot(pitch_curve_wind_speed, blade_pitch, 'o-', label='Pitch Curve Data')
plt.title('Blade Pitch vs. Wind Speed Curve')
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Blade Pitch (degrees)')
plt.grid(True)
plt.legend()
plt.savefig('pitch_curve.png')
plt.show()

# Create an interpolation function
# We use 'extrapolate' to handle wind speeds outside the given range
pitch_interpolator = interp1d(pitch_curve_wind_speed, blade_pitch, kind='linear', bounds_error=False, fill_value=(min(blade_pitch), max(blade_pitch)))


# --- Task 2, Part 2: Determine and plot the time series of blade pitch ---

# Use the interpolation function on the filtered wind speed data
expected_pitch_variation = pitch_interpolator(filtered_wind_speed)

# Plot the expected time series of the blade pitch
plt.figure(figsize=(14, 7))
plt.plot(time, expected_pitch_variation, label='Expected Blade Pitch')
plt.title('Expected Time Series Variation of Blade Pitch')
plt.xlabel('Time (s)')
plt.ylabel('Blade Pitch (deg)')
plt.grid(True)
plt.legend()
plt.savefig('expected_pitch_timeseries.png')
plt.show()