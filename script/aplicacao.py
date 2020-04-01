# v3.0.0

from modulos.construidor import escreve_dados_repositorios, escreve_loc_repositorios
from logging import basicConfig, INFO
from modulos.requisicoes import obtem_repositorios
from modulos.baixador import baixa_repositorios
from modulos.contador_loc import obtem_loc

basicConfig(format='%(asctime)s - %(message)s', level=INFO)


def script() -> None:

    repositorios = obtem_repositorios()

    if not repositorios:
        exit()

    escreve_dados_repositorios(repositorios)

    baixa_repositorios()

    repo_locs = obtem_loc()

    escreve_loc_repositorios(repo_locs)


script()