from script.requisicao import obtem_repositorios, obtem_issues
import csv


def grava_issues():
    def escreve_csv(repo, issues):
        arquivo_repositorios_csv = open(f"../issues_csv/{repo}.csv", 'w')

        output = csv.writer(arquivo_repositorios_csv)

        for i in issues:
            output.writerow(i)

    for i, repo in enumerate(obtem_repositorios()):
        repo_name, issues = obtem_issues(repo)
        issues_list = []

        for issue in issues:
            issues_list.append((issue['number'], issue['id'], issue['comments']['totalCount'], issue['title']))

        escreve_csv(repo_name, issues_list)


grava_issues()
