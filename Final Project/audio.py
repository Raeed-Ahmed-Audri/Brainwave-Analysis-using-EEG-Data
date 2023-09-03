import numpy as np
import librosa

class UserAudio:

    def __init__(self):
        self.signal = None
        self.sample_rate = None

    def load_audio(self, path):
        self.signal, self.sample_rate = librosa.load(path, sr=None)

    def get_audio_signal(self):
        return self.signal

    def get_sample_rate(self):
        return self.sample_rate

    def user_choice_load_audio(self):
        choice = input("Would you like to analyze your own audio file? (yes/no): ")

        if choice.lower() == "yes":
            path = input("Please enter the path to your audio file: ")
            self.load_audio(path)
            return True
        else:
            return False
