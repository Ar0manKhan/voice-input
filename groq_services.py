from os import environ, path
from groq import Groq


client = Groq(
    api_key=environ.get("GROQ_API_KEY"),
)


def transcribe_audio(filename=None):
    if filename is None:
        raise ValueError("filename is None")
    file_path = path.join(".", filename)
    with open(file_path, "rb") as f:
        transcription = client.audio.transcriptions.create(
            file=(file_path, f.read()),
            model="whisper-large-v3-turbo",
            response_format="text"
        )
        return transcription
    return ""


if __name__ == "__main__":
    transcribe_audio("audio_recording_1749704814.0248532.wav")
