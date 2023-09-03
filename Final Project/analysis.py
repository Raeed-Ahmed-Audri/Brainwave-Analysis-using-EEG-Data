import numpy as np
import matplotlib.pyplot as plt
import pywt  # For wavelet decomposition. You might need to install via pip
from signal_generation import Generate_Signal  # Assuming signal_generation is in the same directory

class SignalAnalysis:

    def __init__(self, signal):
        self.signal = signal

    def spectral_analysis(self):
        # FFT for spectral analysis
        signal_fft = np.fft.fft(self.signal)
        frequencies = np.fft.fftfreq(len(self.signal))
        plt.figure()
        plt.plot(frequencies, np.abs(signal_fft))
        plt.title("Spectral Analysis")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude")
        plt.grid()
        plt.show()

    def wavelet_decomposition(self):
        # Using continuous wavelet transform
        coeffs, freqs = pywt.cwt(self.signal, np.arange(1, 128), 'gaus1')
        plt.figure()
        plt.imshow(coeffs, aspect='auto', extent=[0, len(self.signal), 1, 127], cmap='jet')
        plt.colorbar(label='Magnitude')
        plt.title("Wavelet Decomposition")
        plt.xlabel("Sample Index")
        plt.ylabel("Scale")
        plt.show()

    def histogram(self):
        # Histogram of the signal
        plt.figure()
        plt.hist(self.signal, bins=50, color='blue', edgecolor='black')
        plt.title("Signal Histogram")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.grid()
        plt.show()

    def run_analysis_tools(self):
        user_input = input("Do you want to proceed with the analysis tools? (yes/no): ").strip().lower()
        
        if user_input == 'yes':
            self.spectral_analysis()
            self.wavelet_decomposition()
            self.histogram()

        elif user_input == 'no':
            print("Skipping the analysis tool.")
        else:
            print("Invalid choice.")