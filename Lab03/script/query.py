query = """
  query { 
  search(query: "stars:>100 language:Python", type: REPOSITORY, first: 100) {
    nodes {
      ... on Repository {
        createdAt
        openIssues: issues(states: [OPEN]) {
          totalCount
        }
        closedIssues: issues(states: [CLOSED]) {
          totalCount
        }
        url
        name
      }
    }
    pageInfo {
      endCursor
      hasNextPage
    }
  }
}
"""