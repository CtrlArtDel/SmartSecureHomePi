import speech_recognition as sr

class VoiceControl:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.commands = {"arm": "arm", "disarm": "disarm"}

    def listen_for_command(self):
        with sr.Microphone() as source:
            print("Listening for command...")
            try:
                audio = self.recognizer.listen(source)
                command = self.recognizer.recognize_google(audio)
                return self.commands.get(command.lower(), "unknown")
            except sr.UnknownValueError:
                return "unknown"

