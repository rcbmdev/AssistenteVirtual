import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
import wikipedia
import webbrowser as browser
import requests
import json

tts = gTTS("Olá sou a Maria. Em que posso ajudá-lo?", lang="pt")
tts.save("audios/welcome.mp3")
playsound("audios/welcome.mp3")

def cria_audio(mensagem):
    tts = gTTS(mensagem, lang='pt-br')
    file = 'audios/mensagem.mp3'
    tts.save(file)
    playsound("audios/mensagem.mp3")
    os.remove(file)

def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            
            print("Aguardando o Comando: ")
            audio = microfone.listen(source)
            try:
                trigger = microfone.recognize_google(audio, language='pt-BR')
                trigger = trigger.lower()

                print('COMANDO: ', trigger)
                executa_comandos(trigger)
                break

            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
    return trigger

def executa_comandos(trigger):
    # Funções de SO #
    if 'desligar computador' and 'uma hora' in trigger: 
        os.system("shutdown -s -t 3600") #3600 milissegundos = 60 minutos
    elif 'desligar computador' and 'meia hora' in trigger: 
        os.system("shutdown -s -t 1800") #3600 milissegundos = 30 minutos
    elif 'cancelar desligamento' in trigger:
        os.system("shutdown -a")
    elif 'jupyter notebook' in trigger:
        os.system("jupyter notebook")
    elif 'horas' in trigger:
        hora = datetime.now().strftime('%H:%M')
        mensagem = f'Agora são{hora}'
        cria_audio(mensagem)
    elif 'toca' in trigger and 'libertadores' in trigger:
        playlists('libertadores')
    elif 'toca' in trigger and 'instrumental' in trigger:
        playlists('instrumental')
    elif 'toca' in trigger and 'jogo' in trigger:
        playlists('jogo')
    elif 'toca' in trigger and 'filme' in trigger:
        playlists('filme')
    elif 'toca' in trigger and 'série' in trigger:
        playlists('série ')
    elif 'cotação' and 'dólar' in trigger:
        cotacao_dolar()
    elif 'procure por' in trigger:
        consulta_wikipedia(trigger)
    elif 'notícias' in trigger:
        ultimas_noticias()
    elif 'fechar assistente' in trigger:
        os.system("exit")

def cotacao_dolar():
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    cotacao = requisicao.json()
    nome = cotacao['USD']['name']
    data = cotacao['USD']['create_date']
    valor = cotacao['USD']['bid']
    mensagem = f'Cotação do {nome} em {data} é {valor} reais'
    cria_audio(mensagem)


def consulta_wikipedia(trigger):
    procurar = trigger.replace('procure por', '')
    wikipedia.set_lang("pt")
    resultado = wikipedia.summary(procurar, 2)
    print(resultado)
    cria_audio(resultado)

def ultimas_noticias():
    site = get('https://news.google.com/news/rss?ned=pt_br&gl=BR&hl=pt')
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:7]:
        mensagem = item.title.text
        cria_audio(mensagem)

def playlists(album):
    if album == 'libertadores':
        browser.open('https://open.spotify.com/track/3ASPG6p16BCawf6fAJ0qmr?si=08a3b3d8e0db43ee')
    elif album == 'instrumental':
        browser.open('https://open.spotify.com/track/0enLtCNBPxgqHQJ68Uk1H8?si=c95097c06d344136')
    elif album == 'jogo':
        browser.open('https://open.spotify.com/track/00jNnMfEuG861HUy37Mo6Q?si=028f0d1ca36d436e')
    elif album == 'filme':
        browser.open('https://open.spotify.com/track/1FL7eUG80aeUeyMO2N4btN?si=0d4490e925904e92')
    elif album == 'série':
        browser.open('https://open.spotify.com/track/2hsLpiKNkWpd4e9QuVdhar?si=ffb498c00b1548ce')   


def main():
    while True:
        monitora_audio()

main()