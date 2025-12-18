# Multimodal Transcription & Diarization

This project uses **Google Gemini 1.5 Flash** to process audio and video files. It can transcribe speech, identify different speakers (diarization), and provide precise timestamps.

## ✨ Key Features
* **Video Audio Extraction**: Automatically extracts audio from `.mp4` files using `MoviePy`.
* **Speaker Diarization**: Identifies and labels multiple speakers (e.g., Speaker 1, Speaker 2).
* **JSON Timestamps**: Generates structured output containing `start_time`, `end_time`, and `text` for every utterance.
* **Large File Support**: Utilizes the Google Generative AI File API for efficient processing.

## 🛠️ Setup
1. Install dependencies: `pip install google-generativeai moviepy`.
2. Set your API Key: `os.getenv("GOOGLE_API_KEY")`.

## 🚀 Usage
Update the `audio_file` path in `gentest.py` and run:
`python gentest.py`
