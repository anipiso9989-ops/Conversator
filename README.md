# Conversator

Conversator is a local voice assistant built in Python, built by me because I needed to have a local way to practice speaking while learning new languages. See my other repository for more information on that though. 

It combines:
- **Speech-to-Text:** Faster Whisper
- **Language Model:** CohereLabs Tiny Aya Global
- **Text-to-Speech:** pyttsx3

The project is designed with a modular architecture so each component can be replaced independently.

---

## Features

- Local speech recognition
- Multilingual language model
- Offline text-to-speech
- Modular design
- Python-based

---

## Project Structure

```
Conversator/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── src/
│   ├── conversation.py
│   ├── llm.py
│   ├── stt.py
│   └── tts.py
└── audio/
```

---

## Requirements

- Python 3.11+
- Windows 11 (tested)
- Microphone
- Internet connection for the initial model download

---

## Installation

Clone the repository:

```bash
git clone https://github.com/anipiso9989-ops/Conversator.git
cd Conversator
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running

```bash
python app.py
```

The first run will download the Tiny Aya model from Hugging Face.

---

## Architecture

```
Microphone
      ↓
Speech-to-Text (Whisper)
      ↓
Tiny Aya
      ↓
Text-to-Speech (pyttsx3)
      ↓
Speaker
```

---

## Current Limitations

- CPU inference is slow, probably best to use a GPU with a good amount of VRAM.
- Recording uses a fixed duration instead of voice activity detection.
- No conversation memory.
- No streaming responses.

---

## Future Improvements

- Voice Activity Detection (VAD)
- Streaming generation
- GPU acceleration
- Quantized inference
- Higher-quality text-to-speech
- Conversation memory

---

## License

This project is licensed under the MIT License.
