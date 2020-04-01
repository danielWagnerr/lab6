from csv import DictWriter
from configuracao import colunas_node, colunas_repo_loc

def constroi_dicionario_node(node: dict) -> dict:

    return {
        'nome': node['nameWithOwner'],
        'linguagem': node['primaryLanguage']['name'] if node['primaryLanguage'] else '',
        'stargazes': node['stargazers']['totalCount'],
        'watchers': node['watchers']['totalCount'],
        'data_criacao': node['createdAt'],
        'forks': node['forkCount'],
        'url': node['url'],
        'releases': node['releases']['totalCount'],
    }


def escreve_dados_repositorios(repositorios: list) -> None:

    with open('resultados/dados_repositorios.csv', 'w') as dados_repositorios:
        writer = DictWriter(dados_repositorios, fieldnames=colunas_node)
        writer.writeheader()

        for repo in repositorios:
            node_dict = constroi_dicionario_node(repo)
            writer.writerow(node_dict)


def escreve_loc_repositorios(repo_loc: list) -> None:

    with open('resultados/loc_repositorios.csv', 'w') as loc_repo:
        writer = DictWriter(loc_repo, fieldnames=colunas_repo_loc)
        writer.writeheader()

        for rl in repo_loc:
            repo, loc = rl

            nome_repositorio = repo.split('/')[-1]

            writer.writerow({
                'nome': nome_repositorio,
                'loc': loc
            })
