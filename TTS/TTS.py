from gtts import gTTS


class GTTS:
    def __init__(self):
        pass

    def TTS(self, text, filename):
        myobj = gTTS(text=text, lang="en", slow=False)
        myobj.save(f"{filename}.mp3")
