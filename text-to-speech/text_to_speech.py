from gtts import gTTS
import os

mytext = "Wie geht es dir heute?"

language = 'de'
myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save('welcome.mp3')
os.system('welcome.mp3')