import customtkinter as ctk
import tkinter as tk
from audio_recorder import AudioRecorder
from time import time


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

        self.button = ctk.CTkButton(self.main_frame, text="Start", command=self.start)
        self.button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # on press escape, stop the program
        self.bind("<Escape>", self.on_escape)

        self.audio_recorder = AudioRecorder()
        self.start()

        self.mainloop()

    def on_escape(self, event):
        print("pressed escape")
        self.destroy()

    def start(self):
        filename = f"audio_recording_{time()}.wav"
        self.audio_recorder.start_recording(filename=filename)
        self.button.configure(text="Stop")
        self.button.configure(command=self.stop)
        self.status_label.configure(text="Status: Started Recording")

    def stop(self):
        filename = self.audio_recorder.stop_recording()
        self.button.place_forget()
        self.status_label.configure(
            text=f"Status: Stopped Recording, saved to {filename}"
        )


if __name__ == "__main__":
    MainWindow()
