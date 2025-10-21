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
plt.savefig('time_series.png')
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
plt.savefig('fft_spectrum.png')
plt.show()

# --- Part 3: Apply a Low-Pass Filter ---

from scipy.signal import butter, filtfilt

# --- Filter Design and Application ---

# Define the filter parameters
filter_order = 4  # A common choice for the filter order
cutoff_freq_1 = 1.0  # First cutoff frequency in Hz
cutoff_freq_2 = 0.2  # Second, more aggressive cutoff frequency in Hz

# --- First Filter (Cutoff = 1.0 Hz) ---

# Get filter coefficients for the first filter
b1, a1 = butter(filter_order, cutoff_freq_1, btype='low', analog=False, fs=sampling_frequency)
# Apply the filter to the wind speed data
filtered_wind_speed_1 = filtfilt(b1, a1, wind_speed)

# --- Second Filter (Cutoff = 0.2 Hz) ---

# Get filter coefficients for the second filter
b2, a2 = butter(filter_order, cutoff_freq_2, btype='low', analog=False, fs=sampling_frequency)
# Apply the filter to the wind speed data
filtered_wind_speed_2 = filtfilt(b2, a2, wind_speed)


# --- Plotting Comparisons ---

# 1. Time Domain Comparison
plt.figure(figsize=(14, 7))
plt.plot(time, wind_speed, label='Original Signal', alpha=0.5)
plt.plot(time, filtered_wind_speed_1, label=f'Filtered (Cutoff = {cutoff_freq_1} Hz)', linewidth=2)
plt.plot(time, filtered_wind_speed_2, label=f'Filtered (Cutoff = {cutoff_freq_2} Hz)', linewidth=2)
plt.title('Time Domain: Original vs. Filtered Signals')
plt.xlabel('Time (s)')
plt.ylabel('Wind Speed (m/s)')
plt.legend()
plt.grid(True)
plt.savefig('time_domain_comparison.png')
plt.show()

# 2. Frequency Domain Comparison (FFT)

# Perform FFT on the filtered signals
yf_filtered_1 = fft(filtered_wind_speed_1)
yf_filtered_2 = fft(filtered_wind_speed_2)

# Plot the FFT spectra
plt.figure(figsize=(14, 7))
plt.plot(xf[1:], 2.0/N * np.abs(yf[1:N//2]), label='Original Signal', alpha=0.5)
plt.plot(xf[1:], 2.0/N * np.abs(yf_filtered_1[1:N//2]), label=f'Filtered (Cutoff = {cutoff_freq_1} Hz)', linewidth=2)
plt.plot(xf[1:], 2.0/N * np.abs(yf_filtered_2[1:N//2]), label=f'Filtered (Cutoff = {cutoff_freq_2} Hz)', linewidth=2)
plt.xscale('log')
plt.title('Frequency Domain (FFT): Original vs. Filtered Spectra')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.savefig('frequency_domain_comparison.png')
plt.show()