query_repositorios = """
{
    search(query:"stars:>500 language:Python", type:REPOSITORY, first:11){
        nodes{
          ... on Repository
            {
                name
                nameWithOwner
                primaryLanguage {
                    name
                }
            }
        }
    }
}
"""


query_issues = """
{
    repository(name: "{repo_name}", owner: "{owner_name}") {
        issues(orderBy: {field: COMMENTS, direction: DESC}, first: 50) {
            nodes {
                number
                id
                comments {
                    totalCount
                }
                title
            }
        }
    }
}
"""