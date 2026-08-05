from src.stt import listen
from src.llm import generate
from src.tts import speak


def run():
    while True:
        text = listen()

        if not text:
            continue

        print(f"\nYou: {text}")

        response = generate(text)

        print(f"\nAya: {response}")

        speak(response)