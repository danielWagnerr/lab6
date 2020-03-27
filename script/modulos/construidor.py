from csv import DictWriter
from configuracao import colunas_node

def constroi_dicionario_node(node: dict) -> dict:

    return {
        'nome': node['name'],
        'linguagem': node['primaryLanguage']['name'] if node['primaryLanguage'] else '',
        'stargazes': node['stargazers']['totalCount'],
        'watchers': node['watchers']['totalCount'],
        'data_criacao': node['createdAt'],
        'forks': node['forks']['totalCount'],
        'url': node['url'],
        'releases': node['releases']['totalCount'],
    }


def escreve_repositorios_csv(repositorios: list) -> None:

    with open('resultados/resultado1.csv', 'w') as resultado_1:
        writer = DictWriter(resultado_1, fieldnames=colunas_node)
        writer.writeheader()

        for repo in repositorios:
            node_dict = constroi_dicionario_node(repo)
            writer.writerow(node_dict)
