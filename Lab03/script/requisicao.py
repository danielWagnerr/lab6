from script.api_key_github import api_key
from script.query import query
import requests
import csv

headers = {'Authorization': f'Bearer {api_key}'}


def obtem_repositorios():
    request = requests.post('https://api.github.com/graphql',
                            json={'query': query},
                            headers=headers)

    if request.status_code == 200:
        return request.json()


def grava_repositorios():
    arquivo_repositorios_csv = open("repositorios.csv", 'w')
    dados = obtem_repositorios()['data']['search']['nodes']

    output = csv.writer(arquivo_repositorios_csv)
    output.writerow(dados[0].keys())

    for row in dados:
        output.writerow(row.values())