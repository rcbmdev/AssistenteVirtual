import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import sys
from datetime import datetime

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
    # Comandos CMD
    if 'horas' in trigger:
        hora = datetime.now().strftime("%H:%M")
        mensagem = f'São exatamente{hora}'
        cria_audio(mensagem)
    elif 'desligar o computador' and 'uma hora' in trigger:
        os.system("shutdown -s -t 3600")
    elif 'desligar o computador' and 'meia hora' in trigger:
        os.system("shutdown -s -t 1800")
    elif 'cancelar desligamento' in trigger:
        os.system("shutdown -a")
    elif 'jupyter notebook' in trigger:
        os.system("jupyter notebook")
    elif 'fechar assistente' in trigger:
        sys.exit()


def main():
    while True:
        monitora_audio()

main()
