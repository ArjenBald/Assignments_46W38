# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import welch

# --- Part 1: Load and Plot Time Series Data ---

# Load the data from the specified sheet in the Excel file
# The Excel file should be in the same folder as this script.
df = pd.read_excel('Module 7 - Exercises data.xlsx', sheet_name='Exercise 1')

# Extract data into numpy arrays
time = df['Time (s)'].values
wind_speed = df['Wind speed (m/s)'].values

# Plot the time series data
plt.figure(figsize=(14, 7))
plt.plot(time, wind_speed, label='Wind Speed')
plt.title('Wind Speed Time Series')
plt.xlabel('Time (s)')
plt.ylabel('Wind Speed (m/s)')
plt.grid(True)
plt.legend()
plt.show()


# --- Part 2: Frequency Analysis ---

# Calculate parameters for FFT
sampling_interval = time[1] - time[0]
sampling_frequency = 1 / sampling_interval
N = len(wind_speed)

# Perform FFT
yf = fft(wind_speed)
xf = fftfreq(N, sampling_interval)[:N//2]

# Plot the FFT spectrum
plt.figure(figsize=(14, 7))
plt.plot(xf[1:], 2.0/N * np.abs(yf[1:N//2]))
plt.xscale('log')
plt.title('Fast Fourier Transform (FFT) Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


# Calculate PSD using Welch's method
frequencies, psd = welch(wind_speed, fs=sampling_frequency, nperseg=1024)

# Plot the PSD
plt.figure(figsize=(14, 7))
plt.semilogy(frequencies, psd)
plt.title('Power Spectral Density (PSD) using Welch\'s Method')
plt.xlabel('Frequency (Hz)')
plt.ylabel('PSD (m²/s²/Hz)')
plt.grid(True)
plt.show()