from modulos.queries import query
from configuracao import cabecalho_api_github
from requests import post, HTTPError
from json import dumps
from logging import error


def _executa_query(json: dict) -> dict:

    try:
        resposta = post("https://api.github.com/graphql",
                        headers=cabecalho_api_github,
                        data=json)

        resposta.raise_for_status()

        return resposta.json()

    except HTTPError as e:
        error(e)


def obtem_repositorios() -> list:

    primeira_query = query.replace("{after}", "")

    json = {
        'query': primeira_query,
        'variables': {}
    }

    resposta = _executa_query(dumps(json))

    if not resposta:
        exit()

    nodes = resposta["data"]["search"]["nodes"]
    proxima_pagina = resposta["data"]["search"]["pageInfo"]["hasNextPage"]

    qtd_paginas = 1

    while proxima_pagina and qtd_paginas < 100:
        qtd_paginas += 1

        cursor = resposta["data"]["search"]["pageInfo"]["endCursor"]
        proxima_query = query.replace("{after}", ", after: \"%s\"" % cursor)


        json['query'] = proxima_query
        resposta = _executa_query(dumps(json))

        nodes.extend(resposta['data']['search']['nodes'])

        proxima_pagina = resposta["data"]["search"]["pageInfo"]["hasNextPage"]

    return nodes
