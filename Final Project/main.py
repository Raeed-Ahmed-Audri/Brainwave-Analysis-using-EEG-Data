from signal_generation import Generate_Signal
from signal_processing import SignalProcessing
from analysis import SignalAnalysis
from audio import UserAudio
from multiple import MultipleSignalComparison

def main():
    # Check if the user wants to use their own audio file
    user_audio = UserAudio()
    use_own_audio = user_audio.user_choice_load_audio()

    if use_own_audio:
        signal = user_audio.get_audio_signal()
        sample_rate = user_audio.get_sample_rate()
        
        # Now that the user's audio signal is loaded, we can process it
        sp_instance = SignalProcessing(signal, sample_rate)
        sp_instance.user_interaction()

        # Now we will analyze the processed signal
        analysis_instance = SignalAnalysis(sp_instance.get_processed_signal())  
        analysis_instance.run_analysis_tools()
    else:
        # Ask the user if they want to compare multiple signals
        compare = input("Do you want to compare multiple signals? (yes/no): ")

        if compare.lower() == "yes":
            # If they want to compare multiple signals
            comparator = MultipleSignalComparison()
            comparator.generate_and_process()
            comparator.plot_compared_signals()
        else:
            # Otherwise, follow the original flow
            signal_instance = Generate_Signal.signal()
            signal_instance.user_choice_noise()
            signal_instance.user_plot_choice()
            signal = signal_instance.get_signal_array()
            sample_rate = signal_instance.sample_rate

            # Process and analyze the signal
            sp_instance = SignalProcessing(signal, sample_rate)
            sp_instance.user_interaction()

            analysis_instance = SignalAnalysis(sp_instance.get_processed_signal())
            analysis_instance.run_analysis_tools()

if __name__ == "__main__":
    main()



