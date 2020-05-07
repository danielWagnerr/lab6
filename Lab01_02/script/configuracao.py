from token_daniel import token


cabecalho_api_github = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {token}"
}

colunas_node = ['nome', 'linguagem', 'stargazes', 'watchers', 'data_criacao', 'forks', 'url', 'releases']

colunas_repo_loc = ['nome', 'loc']