from modules.soundscapes.soundscapes import SoundScapes
from config import AppConfig


class SoundScapesHandler:
    def __init__(
        self,
        path,
    ):
        self.path = path
        self.path = path.replace("\\", "/")
        self.path += "/modules/soundscapes/"
        self.soundscapes = SoundScapes(self.path, AppConfig().volume)

    def handle_response(self, sound, action):
        self.reply = ""
        if action == "play":
            self.soundscapes.play_sound(sound)
            self.reply = f"[Playing {sound}.]"
        if action == "exit":
            self.reply = f"[Stopping {self.soundscapes.currently_playing}.]"
            self.soundscapes.stop_sound()
        print("\n" + self.reply)
        return self.reply
