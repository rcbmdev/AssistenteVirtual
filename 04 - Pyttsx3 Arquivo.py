import pyttsx3
engine = pyttsx3.init()
engine.setProperty("voice", "brazil")
arquivo = open("dados/frase.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
print(conteudo)
engine.say(conteudo)
engine.runAndWait()
arquivo.close()