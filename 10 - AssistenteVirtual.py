import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import sys

tts = gTTS("Olá me chamo Maria. Em que posso ajudá-lo", lang="pt-BR")
tts.save("audios/welcome.mp3")
playsound("audios/welcome.mp3")

def cria_audio(mensagem):
    tts = gTTS(mensagem, lang="pt-BR")
    tts.save("audios/mensagem.mp3")
    playsound("audios/mensagem.mp3")

def monitora_audio():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Diga algo: ")
            audio = recon.listen(source)
            try:
                trigger = recon.recognize_google(audio, language='pt-BR')
                trigger = trigger.lower()

                print('Você disse: ', trigger)
                executa_comandos(trigger)
                break

            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
    return trigger

def executa_comandos(trigger):
    if 'dia' in trigger:
        cria_audio("Hoje é domingo")
    elif 'fechar assistente' in trigger:
        sys.exit()


def main():
    while True:
        monitora_audio()

main()
