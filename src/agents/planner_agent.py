from src.agents.base_agent import BaseAgent
from src.graph.state import AgentState

class PlannerAgent(BaseAgent):
    name = "PlannerAgent"

    def run(self, state: AgentState) -> AgentState:
        self.log(state, "Planning data sources")

        # Simple heuristic planner (LLM planner comes later)
        state.plan = {
            "rss_feeds": [
                "https://feeds.bbci.co.uk/news/technology/rss.xml",
                "https://techcrunch.com/feed/",
                "https://www.theverge.com/rss/index.xml",
            ],
            "max_items_per_feed": 5
        }

        return state
