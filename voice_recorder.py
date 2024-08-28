import sounddevice as sd
from scipy.io.wavfile import write

# Set the sample rate and duration
sample_rate = 44100  # Sample rate in Hertz
duration = 30  # Duration in seconds

print("Recording...")

# Record the audio
recorded_audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
sd.wait()  # Wait until recording is finished

# Save the recorded audio to a WAV file
write("output.wav", sample_rate, recorded_audio)

print("Recording saved as output.wav")
