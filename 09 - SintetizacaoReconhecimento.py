import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

recon = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga algo..")
    audio = recon.listen(source)
    
frase = recon.recognize_google(audio, language='pt-BR')

print("Você disse ", frase)

tts = gTTS(frase, lang="pt")
tts.save("audios/hello.mp3")
playsound("audios/hello.mp3")