from time import strptime
from datetime import datetime
from csv import reader

def _obtem_repositorios():
    with open('./resultados/resultado1.csv') as repositorios:
        leitor = list(reader(repositorios))

    return leitor


repositorios = _obtem_repositorios()
repositorios.pop(0)


def _questao_01():
    global repositorios
    qtd_repositorios_maduros = 0
    qtd_repositorios_novos = 0

    ano_atual = datetime.now().year

    for repositorio in repositorios:
        data_criacao = repositorio[1]
        ano_repositorio = strptime(data_criacao, "%Y-%m-%dT%H:%M:%SZ").tm_year

        idade = ano_atual - ano_repositorio

        if idade > 3:
            qtd_repositorios_maduros += 1
        else:
            qtd_repositorios_novos += 1

    print("--------------------------------QUESTÃO 01-----------------------------------------------")

    print(f"Tendo em vista que a quantidade de repositórios novos é: {qtd_repositorios_novos} "
          f"e a de maduros é: {qtd_repositorios_maduros}")

    if qtd_repositorios_maduros > qtd_repositorios_novos:
        print("Repositorios populares são maduros!")
    else:
        print("Repositorios populares não são maduros!")

    print("-----------------------------------------------------------------------------------------")


def _questao_02():
    global repositorios
    pull_requests_totais = 0

    muita_contribuicao = 0
    pouca_contribuicao = 0

    for repositorio in repositorios:
        pull_requests_aceitas = int(repositorio[3])
        pull_requests_totais += pull_requests_aceitas

    media = pull_requests_totais/1000

    for repositorio in repositorios:
        pull_requests_aceitas = int(repositorio[3])

        if pull_requests_aceitas > media:
            muita_contribuicao += 1
        else:
            pouca_contribuicao += 1

    print("--------------------------------QUESTÃO 02-----------------------------------------------")

    print(f"Tendo em vista que a quantidade de repositórios com muita contribuição externa é: {muita_contribuicao} "
          f"e com pouca contribuição externa é: {pouca_contribuicao}")

    if muita_contribuicao > pouca_contribuicao:
        print("Repositorios populares tem muita contribuição externa!")
    else:
        print("Repositorios populares tem pouca contribuição externa!")

    print("-----------------------------------------------------------------------------------------")


def _questao_03():
    global repositorios
    releases_totais = 0
    releases = []

    muita_release = 0
    pouca_release = 0

    for repositorio in repositorios:
        qtd_releases = int(repositorio[4])
        releases_totais += qtd_releases
        releases.append(qtd_releases)

    media = releases_totais/1000

    for release in releases:
        if release > media:
            muita_release += 1
        else:
            pouca_release += 1


    print("--------------------------------QUESTÃO 03-----------------------------------------------")

    print(f"Tendo em vista que a quantidade de repositórios com muitas releases é: {muita_release} "
          f"e com poucas releases é: {pouca_release}")

    if muita_release > pouca_release:
        print("Repositorios populares tem muitas releases!")
    else:
        print("Repositorios populares tem poucas releases!")

    print("-----------------------------------------------------------------------------------------")


def _questao_04():
    global repositorios
    diferenca_total = 0
    diferencas = []

    qtd_diferenca_menor = 0
    qtd_diferenca_maior = 0

    for repositorio in repositorios:
        data_criacao = datetime.strptime(repositorio[1], "%Y-%m-%dT%H:%M:%SZ")
        data_atualizacao = datetime.strptime(repositorio[2], "%Y-%m-%dT%H:%M:%SZ")

        diferenca = (data_atualizacao - data_criacao).days
        diferenca_total += diferenca
        diferencas.append(diferenca)

    media = diferenca_total/1000

    for diff in diferencas:

        if diff > media:
            qtd_diferenca_maior += 1
        else:
            qtd_diferenca_menor += 1

    print("--------------------------------QUESTÃO 04-----------------------------------------------")

    print(f"Tendo em vista que a quantidade de repositórios populares atualizados com frequência é "
          f"{qtd_diferenca_maior} e os que não são atualizados com frequência é {qtd_diferenca_menor}")

    if qtd_diferenca_maior > qtd_diferenca_menor:
        print("Repositórios populares não são atualizados com frequencia!")
    else:
        print("Repositórios populares são atualizados com frequencia!")

    print("-----------------------------------------------------------------------------------------")


def _questao_05():
    print("--------------------------------QUESTÃO 05-----------------------------------------------")

    print("Os repositórios populares são escritos nas linguagens populares. Isso se dá pelo fato de "
          "que a maioria das linguagens primárias nos repositórios são as linguagens mais populares.")

    print("-----------------------------------------------------------------------------------------")

def _questao_06():
    global repositorios

    qtd_muitas_issues_fechadas = 0
    qtd_poucas_issues_fechadas = 0

    for repositorio in repositorios:
        issues_fechadas = int(repositorio[6])
        issues_totais = int(repositorio[7])

        if issues_totais == 0:
            pass

        elif issues_fechadas == 0:
            qtd_muitas_issues_fechadas += 1

        else:
            porcentagem = (issues_fechadas/issues_totais) * 100

            if porcentagem > 70:
                qtd_muitas_issues_fechadas += 1
            else:
                qtd_poucas_issues_fechadas += 1

    print("--------------------------------QUESTÃO 06-----------------------------------------------")

    print(f"Tendo em mente que uma quantidade alta de issues fechadas seja em torno de 70% e a quantidade de "
          f"repositórios que tem um percentual maior que esse é: {qtd_muitas_issues_fechadas} "
          f"e a quantidade dos que tem um percentual menor é: {qtd_poucas_issues_fechadas}")

    if qtd_muitas_issues_fechadas> qtd_poucas_issues_fechadas:
        print("Repositórios populares tem muitas issues fechadas!")
    else:
        print("Repositórios populares não tem muitas issues fechadas!")

    print("-----------------------------------------------------------------------------------------")


def questoes():
    _questao_01()
    _questao_02()
    _questao_03()
    _questao_04()
    _questao_05()
    _questao_06()
