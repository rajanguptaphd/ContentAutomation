from fastapi import FastAPI
import requests

app = FastAPI()

REDDIT_BASE = "https://www.reddit.com"
HEADERS = {"User-Agent": "agentic-ai-research/0.1"}

@app.get("/search")
def search_reddit(query: str, limit: int = 10):
    print(f"[REDDIT MCP] Search called | query='{query}' | limit={limit}")
    url = f"{REDDIT_BASE}/search.json"
    params = {
        "q": query,
        "limit": limit,
        "sort": "hot"
    }

    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()

    data = response.json()

    results = []
    for child in data["data"]["children"]:
        post = child["data"]
        results.append({
            "title": post.get("title"),
            "subreddit": post.get("subreddit"),
            "score": post.get("score"),
            "url": f"https://reddit.com{post.get('permalink')}",
            "selftext": post.get("selftext", "")[:500]
        })

    return {"results": results}
