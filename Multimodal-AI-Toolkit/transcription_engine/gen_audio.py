# pip install -q -U google-generativeai
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def transcribe_audio_with_diarization(audio_file_path):
    """
    Transcribes an audio file and attempts speaker diarization using Gemini 1.5 Flash.

    Args:
        audio_file_path: The path to the audio file.

    Returns:
        The transcribed text with speaker labels, or None if an error occurs.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash') # Use Gemini 1.5 Flash.

        with open(audio_file_path, "rb") as audio_file:
            audio_data = audio_file.read()

        prompt = """
        Please transcribe the following audio and perform speaker diarization. 
        Indicate who is speaking before each segment of speech. 
        If possible, please label speakers as Speaker 1, Speaker 2, and so on.
        If the model cannot perform speaker diarization, just provide the transcription.
        """

        response = model.generate_content([
            prompt,
            {"mime_type": "audio/*", "data": audio_data}
        ])

        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
audio_file = "path/to/your/audio.wav"  # Replace with your audio file path
result = transcribe_audio_with_diarization(audio_file)

if result:
    print(result)