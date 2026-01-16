from langgraph.graph import StateGraph, END
from src.graph.state import AgentState
from src.agents.planner_agent import PlannerAgent
from src.agents.collector_agent import CollectorAgent
from src.agents.generator_agent import GeneratorAgent

def build_graph():
    planner = PlannerAgent()
    collector = CollectorAgent()
    generator = GeneratorAgent()

    graph = StateGraph(AgentState)

    graph.add_node("plan", planner.run)
    graph.add_node("collect", collector.run)
    graph.add_node("generate", generator.run)

    graph.set_entry_point("plan")
    graph.add_edge("plan", "collect")
    graph.add_edge("collect", "generate")
    graph.add_edge("generate", END)

    return graph.compile()
