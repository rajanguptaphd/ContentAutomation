import requests

REDDIT_MCP_URL = "http://localhost:3333/search"

def search_reddit_mcp(query: str, limit: int = 10):
    params = {
        "query": query,
        "limit": limit
    }

    response = requests.get(REDDIT_MCP_URL, params=params)
    response.raise_for_status()

    return response.json()["results"]
