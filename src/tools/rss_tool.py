import feedparser

def fetch_rss(feed_url: str, limit: int = 5):
    feed = feedparser.parse(feed_url)

    articles = []
    for entry in feed.entries[:limit]:
        articles.append({
            "title": entry.get("title", ""),
            "summary": entry.get("summary", ""),
            "link": entry.get("link", ""),
            "source": feed_url
        })

    return articles
