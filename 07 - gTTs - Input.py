from gtts import gTTS
from playsound import playsound
frase = input("Digite o nome da frase que você deseja \n")
tts = gTTS(frase, lang='pt-br')
tts.save('ola.mp3')
playsound('ola.mp3')
