import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
DURATION = 5  # seconds, change this as needed

model = WhisperModel("base", device="cpu")


def listen():
    print("Listening...")

    recording = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
    )

    sd.wait()

    write("audio/input.wav", SAMPLE_RATE, recording)

    segments, _ = model.transcribe("audio/input.wav")

    text = " ".join(segment.text for segment in segments)

    return text.strip()