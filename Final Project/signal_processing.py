import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve, butter, lfilter, freqz

class SignalProcessing:

    def __init__(self, signal, sample_rate):
        """
        Initialize the SignalProcessing object with the signal and its sample rate.

        :param signal: numpy array, the input signal
        :param sample_rate: int, the sample rate of the signal (samples per second)
        """
        self.signal = signal
        self.sample_rate = sample_rate
        self.processed_signal = signal  # initially, processed signal is just the original signal

    def filter_signal(self, cutoff, btype='low', order=5):
        """
        Filters the signal using a Butterworth filter.

        :param cutoff: int or float, the cutoff frequency for the filter
        :param btype: str, the type of filter (options: 'low', 'high', 'band', 'stop')
        :param order: int, the order of the filter (default is 5)
        :return: numpy array, the filtered signal
        """
        nyq = 0.5 * self.sample_rate
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype=btype, analog=False)
        self.processed_signal = lfilter(b, a, self.signal)
        return self.processed_signal

    def modulate_signal(self, carrier_freq):
        """
        Modulates the signal using a simple carrier frequency.

        :param carrier_freq: int or float, the frequency of the carrier signal
        :return: numpy array, the modulated signal
        """
        t = np.arange(len(self.signal)) / self.sample_rate
        carrier = np.cos(2 * np.pi * carrier_freq * t)
        self.processed_signal = self.signal * carrier
        return self.processed_signal

    def sample_signal(self, sampling_interval):
        """
        Samples the signal at regular intervals.

        :param sampling_interval: int, the interval at which to sample the signal
        :return: numpy array, the sampled signal
        """
        self.processed_signal = self.signal[::sampling_interval]
        return self.processed_signal

    def convolve_signal(self, kernel):
        """
        Convolves the signal with a given kernel.

        :param kernel: numpy array, the convolution kernel
        :return: numpy array, the convolved signal
        """
        self.processed_signal = convolve(self.signal, kernel, mode='same')
        return self.processed_signal

    def plot_signal(self, signal, title="Signal"):
        """
        Plots the given signal.

        :param signal: numpy array, the signal to be plotted
        :param title: str, the title of the plot
        """
        t = np.arange(len(signal)) / self.sample_rate
        plt.plot(t, signal)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title(title)
        plt.grid()
        plt.show()

    def user_interaction(self):
        """
        Interacts with the user to choose the signal processing technique and decide whether to plot the processed signal.
        """
        print("Choose the signal processing technique:")
        print("1. Filtering")
        print("2. Modulation")
        print("3. Sampling")
        print("4. Convolution")
        print("5. None (No processing)")
        
        choice = input()

        if choice == "1":
            cutoff = float(input("Enter the cutoff frequency: "))
            btype = input("Enter the filter type (low/high/band/stop): ")
            order = int(input("Enter the filter order (default is 5): "))
            processed_signal = self.filter_signal(cutoff, btype, order)

        elif choice == "2":
            carrier_freq = float(input("Enter the carrier frequency: "))
            processed_signal = self.modulate_signal(carrier_freq)

        elif choice == "3":
            sampling_interval = int(input("Enter the sampling interval: "))
            processed_signal = self.sample_signal(sampling_interval)

        elif choice == "4":
            kernel_size = int(input("Enter the size of the kernel: "))
            kernel = np.ones(kernel_size) / kernel_size  # Simple average kernel
            processed_signal = self.convolve_signal(kernel)

        elif choice == "5":
            print("No processing selected.")
            processed_signal = self.signal  # Return the original signal unprocessed

        else:
            print("Invalid choice.")
            return

        plot_choice = input("Do you want to plot the processed signal? (yes/no): ")
        if plot_choice.lower() == "yes":
            self.plot_signal(processed_signal, title="Processed Signal")

    def get_processed_signal(self):
        """
        Retrieve the processed signal.
        """
        return self.processed_signal



