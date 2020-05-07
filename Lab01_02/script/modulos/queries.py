

query = """
{
    search(query:"stars:>100 language:Python", type:REPOSITORY, first:10{after}){
        nodes{
          ... on Repository
          {
            nameWithOwner
            url
            primaryLanguage
            {
              name
            }
            stargazers
            {
              totalCount
            }
            watchers
            {
              totalCount
            }
            forkCount
            releases
            {
              totalCount
            }
            createdAt
          }
        }
        pageInfo
        {
          hasNextPage
          endCursor
        }
      }
  }
"""
