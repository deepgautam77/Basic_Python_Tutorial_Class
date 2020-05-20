from gtts import gTTS
import os

mytext = """I started feeling again,
I started dreaming again.
Where was I lost,
I started gleaming again."""

language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save('welcome.mp3')
os.system('welcome.mp3')