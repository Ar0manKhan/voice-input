import wave
import pyaudio
import threading


class AudioRecorder:
    def __init__(self, filename="recording.wav", channels=1, sample_rate=44100, chunk=1024, format=pyaudio.paInt16):
        self.filename = filename
        self.channels = channels
        self.rate = sample_rate
        self.chunk = chunk
        self.format = format

        self._audio = pyaudio.PyAudio()
        self._frames = []
        self._thread = None
        self._stop_event = threading.Event()
        self._is_recording = False

    @property
    def is_recording(self):
        return self._is_recording

    @property
    def wave_frames(self):
        return self._frames

    def _record(self):
        self._frames = []
        stream = self._audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk,
        )
        self._is_recording = True
        print("Recording started")
        while not self._stop_event.is_set():
            data = stream.read(self.chunk)
            self._frames.append(data)
        stream.stop_stream()
        stream.close()
        self._is_recording = False
        self._save()
        print(f'Recording stopped, saved to {self.filename}')

    def _save(self):
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self._audio.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(self._frames))
        wf.close()

    def start_recording(self, filename=None):
        if self._is_recording:
            print("Already recording")
            return
        if filename:
            self.filename = filename
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._record)
        self._thread.start()

    def stop_recording(self):
        if not self._is_recording:
            print("Not recording")
            return
        self._stop_event.set()
        self._thread.join()

    def __del__(self):
        self.stop_recording()
        self._audio.terminate()


if __name__ == "__main__":
    recorder = AudioRecorder()
    recorder.start_recording()

    import time
    time.sleep(5)
    recorder.stop_recording()
