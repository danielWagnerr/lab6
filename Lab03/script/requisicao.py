from script.api_key_github import api_key
from script.queries import query_repositorios, query_issues
import requests
import csv

headers = {'Authorization': f'Bearer {api_key}'}


def obtem_repositorios():
    resposta = requests.post('https://api.github.com/graphql',
                            json={'query': query_repositorios},
                            headers=headers)

    repositorios = resposta.json()["data"]["search"]["nodes"]

    return repositorios


def obtem_issues(repositorio):
    owner_repo = repositorio['nameWithOwner'].split('/')
    owner_name = owner_repo[0]
    repo_name = owner_repo[1]

    final_query = query_issues.replace("{owner_name}", owner_name)
    final_query = final_query.replace("{repo_name}", repo_name)

    resposta = requests.post('https://api.github.com/graphql',
                             json={'query': final_query},
                             headers=headers)

    issues = resposta.json()["data"]["repository"]["issues"]["nodes"]

    return repo_name, issues
