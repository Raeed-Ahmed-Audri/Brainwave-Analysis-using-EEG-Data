from signal_generation import Generate_Signal
from signal_processing import SignalProcessing
import matplotlib.pyplot as plt

class MultipleSignalComparison:

    def __init__(self):
        self.signals = []
        self.sample_rates = []

    def generate_and_process(self):
        """
        Interacts with the user to generate and process multiple signals.
        """
        num_signals = int(input("How many signals would you like to generate and compare? "))
        
        for i in range(num_signals):
            print(f"\nGenerating and processing Signal {i + 1}:\n")
            
            # Generate the signal
            signal_instance = Generate_Signal.signal()
            signal_instance.user_choice_noise()
            signal_instance.user_plot_choice()
            signal = signal_instance.get_signal_array()
            sample_rate = signal_instance.sample_rate

            # Process the signal
            sp_instance = SignalProcessing(signal, sample_rate)
            sp_instance.user_interaction()
            processed_signal = sp_instance.get_processed_signal()

            # Store the processed signal and sample rate
            self.signals.append(processed_signal)
            self.sample_rates.append(sample_rate)

    def plot_compared_signals(self):
        """
        Plots all processed signals on the same graph for comparison.
        """
        for i, signal in enumerate(self.signals):
            t = [x/self.sample_rates[i] for x in range(len(signal))]
            plt.plot(t, signal, label=f'Signal {i + 1}')
        
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('Compared Processed Signals')
        plt.legend()
        plt.grid()
        plt.show()

