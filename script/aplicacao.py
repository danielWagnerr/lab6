# v3.0.0

from modulos.construidor import escreve_repositorios_csv
from logging import basicConfig, INFO
from modulos.requisicoes import obtem_repositorios
from modulos.questoes import questoes
from modulos.baixador import baixa_repositorios

basicConfig(format='%(asctime)s - %(message)s', level=INFO)


def script() -> None:

    repositorios = obtem_repositorios()

    if not repositorios:
        exit()

    escreve_repositorios_csv(repositorios)


script()
#questoes()
baixa_repositorios()