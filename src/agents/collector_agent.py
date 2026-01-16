from src.agents.base_agent import BaseAgent
from src.graph.state import AgentState
from src.tools.rss_tool import fetch_rss
from src.tools.mcp.reddit_client import search_reddit_mcp

class CollectorAgent(BaseAgent):
    name = "CollectorAgent"

    def run(self, state: AgentState) -> AgentState:
        self.log(state, "Collecting data from planned sources")

        plan = state.plan
        rss_feeds = plan.get("rss_feeds", [])
        limit = plan.get("max_items_per_feed", 5)

        all_articles = []

        for feed_url in rss_feeds:
            try:
                articles = fetch_rss(feed_url, limit)
                all_articles.extend(articles)
            except Exception as e:
                self.log(state, f"Failed to fetch {feed_url}: {e}")

        state.sources = all_articles
        self.log(state, f"Collected {len(all_articles)} articles")

        # Reddit MCP
        queries = ["AI agents", "open source LLM", "LangGraph"]

        for q in queries:
            try:
                self.log(state, f"Calling Reddit MCP for query: {q}")
                posts = search_reddit_mcp(q, limit=5)
                for post in posts:
                    state.sources.append({
                        "title": post["title"],
                        "summary": post["selftext"],
                        "link": post["url"],
                        "source": f"reddit:{post['subreddit']}"
                    })
                self.log(state, f"Reddit MCP returned {len(posts)} posts for '{q}'")
            except Exception as e:
                self.log(state, f"Reddit MCP failed for '{q}': {e}")
                
        return state
