import gtts
from playsound import playsound
tts = gtts.gTTS("Hola Mundo", lang="es")
tts.save("hello.mp3")