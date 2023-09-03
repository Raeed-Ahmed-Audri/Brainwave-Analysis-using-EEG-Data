Signal Analysis Tool README
1. Introduction
This Signal Analysis Tool is built using Python and is designed to provide a comprehensive platform for signal generation, processing, analysis, and comparison. Users have the flexibility to generate signals with optional noise addition, process these signals with a variety of techniques, analyze them using several tools, and even input their own audio for analysis. The toolset also includes provisions for image processing.

Features
Generate five types of signals:
Sine
Square
Triangle
Sawtooth
Pulse
Add noise:
Gaussian
Salt & Pepper
Combination of both
Prerequisites
Ensure you have the following installed:

Python 3.x
NumPy
Matplotlib
How to Use
Clone or download this repository.
Navigate to the directory containing the signal_generation.py module.
Run the main program to generate and visualize the signal with potential noise:
bash
Copy code
python main.py
Follow the on-screen prompts to select the signal type, frequency, amplitude, duration, phase, and sampling rate.
Optionally, choose to add noise to the generated signal.
Documentation
Inline comments and docstrings are provided within the code for more detailed understanding.

2. Time Array Generation
np.linspace(start, stop, num, endpoint)

Generates a sequence of evenly spaced values over a specified interval.

Parameters:
start: (float) The starting value of the sequence.
stop: (float) The end value of the sequence.
num: (int) The number of evenly spaced samples to generate. Commonly used to determine the number of samples based on the sample_rate and the duration.
endpoint: (bool) Whether the stop value should be included in the sequence. If set to False, the stop value is excluded, ensuring the sequence has exactly num values.
Usage: This function is utilized to generate time values for the signal over its duration with the specified sampling rate.

3. Signal Generation
Allows users to generate a signal, add noise, and view its plot. Users are also prompted to decide if they want noise added to the signal.

4. Signal Processing
Provides the following functionalities:

Filtering: Filters the signal using a Butterworth filter with user-specified parameters.
Modulation: Modulates the signal using a specified carrier frequency.
Sampling: Samples the signal at regular intervals specified by the user.
Convolution: Convolves the signal with a specified kernel.

5. Signal Analysis
Consists of multiple tools for signal analysis:

Spectral Analysis: Analyzes the frequency domain representation of the signal.
Wavelet Decomposition: Decomposes the signal using wavelets.
Histogram: Plots the histogram of the signal to represent its amplitude distribution.
6. Multiple Signal Comparison
Allows users to generate and compare multiple signal graphs side by side.

7. Audio Input
Users can input their own audio file for analysis. The system processes and analyzes the uploaded audio signal.

9. Imag Processing
This tool is in development and aims to provide functionalities similar to the signal analysis tool but tailored for images.

8. How to Use
Run main.py.
Follow the prompts to generate a signal, process it, and run analysis tools. Users have the option to use their own audio or compare multiple signals.

10. Dependencies
This tool utilizes several Python libraries including:

Numpy
Matplotlib
Scipy
Pywt
Librosa (for audio processing)

Author


Raeed Ahmed Audri

