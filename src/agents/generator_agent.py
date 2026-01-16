from src.agents.base_agent import BaseAgent
from src.graph.state import AgentState
import time
from src.llm.factory import create_llm
from src.utils.config_loader import load_yaml
from src.llm.prompts import GENERATOR_PROMPT

class GeneratorAgent(BaseAgent):
    name = "GeneratorAgent"

    def __init__(self):
        print(">>> [GeneratorAgent] __init__ started")

        cfg = load_yaml("configs/models.yaml")["generator"]
        self.llm = create_llm(cfg)
        print(">>> [GeneratorAgent] model loaded successfully")

    def run(self, state: AgentState) -> AgentState:
        self.log(state, "Generating summary using LLM")

        print(">>> [GeneratorAgent] Entered run()")
        print(">>> [GeneratorAgent] Preparing prompt")

        sources_text = "\n".join(
            f"- {item['title']}: {item['summary']}"
            for item in state.sources
        )
        prompt = GENERATOR_PROMPT.format(sources=sources_text)

        print(">>> [GeneratorAgent] entering model.generate()")

        start_time = time.time()
        output = self.llm.generate(prompt)
        elapsed = time.time() - start_time

        print(f">>> [GeneratorAgent] model.generate() finished in {elapsed:.2f} seconds")

        state.summary = output.strip()

        print(">>> [GeneratorAgent] Summary set, exiting run()")

        return state
    