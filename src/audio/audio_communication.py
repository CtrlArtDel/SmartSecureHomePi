import pyaudio
import socket

class TwoWayAudio:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.audio = pyaudio.PyAudio()

    def start_audio_stream(self):
        stream = self.audio.open(format=pyaudio.paInt16,
                                 channels=1,
                                 rate=44100,
                                 input=True,
                                 output=True,
                                 frames_per_buffer=1024)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            while True:
                data = stream.read(1024)
                s.sendall(data)
                received = s.recv(1024)
                stream.write(received)

    def stop_audio_stream(self):
        self.audio.terminate()

