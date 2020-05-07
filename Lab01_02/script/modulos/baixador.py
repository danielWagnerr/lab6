from git import Git
from csv import DictReader
from git.exc import GitCommandError
from logging import info


def baixa_repositorios():
    with open('./resultados/dados_repositorios.csv') as dados_repositorios:
        reader = DictReader(dados_repositorios)

        for repo in reader:
            print(f"Baixando repositório {repo['nome']}.")

            try:
                Git('./repositorios').clone(repo['url'])
            except GitCommandError as e:
                info(f"Repositório {repo['nome']} já está contido na pasta repositorios.")
