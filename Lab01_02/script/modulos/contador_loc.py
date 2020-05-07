from radon.cli.harvest import RawHarvester
from radon.cli import Config
from os import scandir


def obtem_loc() -> list:
    config = Config(exclude='', ignore='.*')
    repositorios = [f.path for f in scandir('./repositorios') if f.is_dir()]

    locs = []

    for repo in repositorios:
        resultados = RawHarvester([repo], config).results

        loc_repo = [r[1]['loc'] for r in list(resultados)]
        loc_total = sum(loc_repo)

        locs.append((repo, loc_total))

    return locs