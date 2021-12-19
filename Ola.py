import requests
import json

requisicao = requests.get('https://economia.awesomeapi.com.br/all/BTC-BRL')

cotacao = requisicao.json()

print('#### Cotação do Bitcoin ####')

print(cotacao)
nome = cotacao['BTC']['name']
data = cotacao['BTC']['create_date']
valor = cotacao['BTC']['bid']
mensagem = f'Cotação do {nome} em {data} é {valor}'
print(mensagem)
