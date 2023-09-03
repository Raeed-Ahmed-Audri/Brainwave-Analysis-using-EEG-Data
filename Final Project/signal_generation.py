import numpy as np
import matplotlib.pyplot as plt

class Generate_Signal():
    def __init__(self, signal_type, freq, amplitude, duration, phase, sample_rate):
        #Choosing a signal type
        if signal_type not in ["sine", "square", "triangle", "sawtooth", "cosine"]:
            raise ValueError("Not an applicable signal type.")
        #Setting range of values
        if freq <= 0:
            raise ValueError("Non-positive frequencies cannot generate a signal.")
        if amplitude < 0:
            raise ValueError("Amplitude cannot be negative.")
        if duration <= 0:
            raise ValueError("Duration should be positive.")
        if not (0 <= sample_rate <= 100000):  
            raise ValueError("Invalid sample rate.")
        
        self.signal_type = signal_type
        self.freq = freq
        self.amplitude = amplitude
        self.duration = duration
        self.phase = phase
        self.sample_rate = sample_rate
        self.t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    #A class method developed to get user input
    @classmethod
    def signal(cls):
    # Prompt the user for signal parameters

        # Check signal type
        signal_type = input("Choose the signal type (sine/square/triangle/sawtooth/cosine): ")
        while signal_type not in ["sine", "square", "triangle", "sawtooth", "cosine"]:
            print("Invalid signal type. Please choose from sine, square, triangle, sawtooth, or cosine.")
            signal_type = input("Choose the signal type (sine/square/triangle/sawtooth/cosine): ")

        # Check frequency
        try:
            freq = float(input("Enter the frequency (e.g., 1 for 1Hz): "))
            while freq <= 0:
                print("Non-positive frequencies cannot generate a signal.")
                freq = float(input("Enter the frequency (e.g., 1 for 1Hz): "))
        except ValueError:
            print("Please enter a valid number for the frequency.")
            return

        # Check amplitude
        try:
            amplitude = float(input("Enter the amplitude (e.g., 1 for unit amplitude): "))
            while amplitude < 0:
                print("Amplitude cannot be negative.")
                amplitude = float(input("Enter the amplitude (e.g., 1 for unit amplitude): "))
        except ValueError:
            print("Please enter a valid number for the amplitude.")
            return

        # Check duration
        try:
            duration = float(input("Enter the duration of the signal in seconds (e.g., 5 for 5 seconds): "))
            while duration <= 0:
                print("Duration should be positive.")
                duration = float(input("Enter the duration of the signal in seconds (e.g., 5 for 5 seconds): "))
        except ValueError:
            print("Please enter a valid number for the duration.")
            return

        # Check phase (Note: Since no specific condition is given for phase, we'll just validate if it's a number)
        try:
            phase = float(input("Enter the phase in radians (e.g., 1.57 for π/2): "))
        except ValueError:
            print("Please enter a valid number for the phase.")
            return

        # Check sample rate
        try:
            sample_rate = int(input("Enter the sampling rate (e.g., 44100 for audio): "))
            while not (0 <= sample_rate <= 100000):
                print("Sample rate should be between 1 and 100000.")
                sample_rate = int(input("Enter the sampling rate (e.g., 44100 for audio): "))
        except ValueError:
            print("Please enter a valid integer for the sampling rate.")
            return
        
        return cls(signal_type, freq, amplitude, duration, phase, sample_rate)

        
    
    def generate_time_values(self):
        #Generate an array of time values (self.t) starting from 0 to duration, with the number of points being sample_rate * duration.
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), endpoint=False)
        return t

    def get_generate_array(self):
        t = self.generate_time_values()

        # Generate the signal based on user's choice
        if self.signal_type == "sine":
            signal = self.amplitude * np.sin(2 * np.pi * self.freq * t + self.phase)
        elif self.signal_type == "square":
            signal = self.amplitude * np.sign(np.sin(2 * np.pi * self.freq * t + self.phase))
        elif self.signal_type == "triangle":
            signal = self.amplitude * 2 * np.arcsin(np.sin(2 * np.pi * self.freq * t + self.phase)) / np.pi
        elif self.signal_type == "sawtooth":
            signal = 2 * (t * self.freq - np.floor(t * self.freq + 0.5))
        elif self.signal_type == "pulse":
            signal = self.amplitude * (np.sin(2 * np.pi * self.freq * t) > 0).astype(float)
        else:
            raise ValueError("Invalid signal type chosen.")

        self.signal_array = signal
        return self.signal_array

    def add_gaussian_noise(self, signal, noise_level=0.5):
        noise = np.random.normal(0, noise_level, signal.shape)
        return signal + noise

    def add_salt_pepper_noise(self, signal, salt_prob=0.01, pepper_prob=0.01):
        noisy_signal = np.copy(signal)
        total_samples = len(signal)

        # Add Salt noise
        num_salt = np.ceil(salt_prob * total_samples)
        salt_indices = np.random.choice(total_samples, int(num_salt), replace=False)
        noisy_signal[salt_indices] = 1

        # Add Pepper noise
        num_pepper = np.ceil(pepper_prob * total_samples)
        pepper_indices = np.random.choice(total_samples, int(num_pepper), replace=False)
        noisy_signal[pepper_indices] = -1

        return noisy_signal

    def user_choice_noise(self):
        signal = self.get_generate_array()
        print("Choose noise type:\n1. Gaussian\n2. Salt & Pepper\n3. Both\n4. None")
        choice = input()

        if choice == "1":
            noise_level = float(input("Enter the Gaussian noise level (0.5 is a typical value): "))
            signal = self.add_gaussian_noise(signal, noise_level)

        elif choice == "2":
            salt_prob = float(input("Enter the probability of salt noise (0.01 is a typical value): "))
            pepper_prob = float(input("Enter the probability of pepper noise (0.01 is a typical value): "))
            signal = self.add_salt_pepper_noise(signal, salt_prob, pepper_prob)

        elif choice == "3":
            noise_level = float(input("Enter the Gaussian noise level (0.5 is a typical value): "))
            signal = self.add_gaussian_noise(signal, noise_level)
            salt_prob = float(input("Enter the probability of salt noise (0.01 is a typical value): "))
            pepper_prob = float(input("Enter the probability of pepper noise (0.01 is a typical value): "))
            signal = self.add_salt_pepper_noise(signal, salt_prob, pepper_prob)
        
        elif choice == "4":
            pass

        else:
            print("Invalid choice.")
            return
        
    def get_signal_array(self):
        return self.signal_array



    def plot_signal(self, time_values, signal):
        """Plots the signal in the time domain."""
        plt.plot(time_values, signal)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title(f'{self.signal_type.capitalize()} Wave with Noise')
        plt.grid()
        plt.show()

    def plot_frequency_domain(self, signal):
        """Plots the signal in the frequency domain using Fourier analysis."""
        signal_fft = np.fft.fft(signal)
        frequencies = np.fft.fftfreq(len(signal), 1/self.sample_rate)
        
        plt.figure()
        plt.plot(frequencies, np.abs(signal_fft))
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude')
        plt.title(f'Frequency Spectrum of {self.signal_type.capitalize()} Wave')
        plt.grid()
        plt.show()

    def user_plot_choice(self):
        """Asks the user about their plotting preferences and plots accordingly."""
        plot_choice = input("Do you want to plot the signal in the time domain? (yes/no): ").lower()
        if plot_choice == 'yes':
            t = self.generate_time_values()
            signal = self.generate_signal()
            self.plot_signal(t, signal)
        elif plot_choice == 'no':
            print("Signal not plotted in time domain.")
        else:
            print("Invalid choice for time domain plot.")

        freq_plot_choice = input("Do you want to view the signal in the frequency domain? (yes/no): ").lower()
        if freq_plot_choice == 'yes':
            signal = self.generate_signal()  # You may need to retrieve the signal again or store it from the previous choice
            self.plot_frequency_domain(signal)
        elif freq_plot_choice == 'no':
            print("Signal not plotted in frequency domain.")
        else:
            print("Invalid choice for frequency domain plot.")


      

    
    









