

query = """
{
  user(login: "gvanrossum") {
    repositories(first: 50,isFork:false) {
      nodes {
        name
        primaryLanguage {
          name
        }
        stargazers {
          totalCount
        }
        watchers {
          totalCount
        }
        createdAt
        forks {
          totalCount
        }
        url
         releases {
          totalCount
        }
      }
    }
  }
} 
"""
