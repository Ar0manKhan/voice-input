import customtkinter as ctk
import tkinter as tk
from audio_recorder import AudioRecorder
import tempfile
import os
import pyperclip

from groq_services import transcribe_audio


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Voice Input")
        self.geometry("400x400")
        self.resizable(False, False)
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.main_frame.configure(width=400, height=400)

        self.status_label = ctk.CTkLabel(
            self.main_frame, text="Status: Stopped", fg_color="transparent", width=250
        )
        self.status_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.button = ctk.CTkButton(self.main_frame, text="Stop", command=self.stop)
        self.button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Key bindings
        self.bind("<Escape>", self.on_escape)
        self.bind("<space>", self.on_space)
        self.focus_set()  # Ensure window can receive key events

        self.audio_recorder = AudioRecorder()
        self.temp_audio_file = None
        self.start()

        self.mainloop()

    def on_escape(self, event):
        print("pressed escape")
        # Clean up temp file if it exists
        if self.temp_audio_file and os.path.exists(self.temp_audio_file):
            os.unlink(self.temp_audio_file)
        self.destroy()

    def on_space(self, event):
        print("pressed space")
        self.stop()

    def start(self):
        # Create temporary file
        temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        self.temp_audio_file = temp_file.name
        temp_file.close()

        self.audio_recorder.start_recording(filename=self.temp_audio_file)
        self.status_label.configure(text="Status: Recording... (Press Space to stop)")

    def stop(self):
        filename = self.audio_recorder.stop_recording()
        self.button.place_forget()
        self.status_label.configure(text="Status: Processing transcription...")

        if filename and type(filename) == str:
            transcription = transcribe_audio(filename)

            # Delete the temporary file after transcription
            try:
                if os.path.exists(filename):
                    os.unlink(filename)
                    print(f"Deleted temporary file: {filename}")
            except OSError as e:
                print(f"Error deleting temporary file: {e}")

            if (
                transcription is None
                or type(transcription) != str
                or len(transcription) == 0
            ):
                print("Transcription is empty")
                self.destroy()
                return

            pyperclip.copy(transcription)
            print("Transcribed:", transcription)
            print("Transcription copied to clipboard")

            # Terminate the program after copying
            self.destroy()


if __name__ == "__main__":
    MainWindow()
