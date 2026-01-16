from src.agents.base_agent import BaseAgent
from src.graph.state import AgentState
from src.utils.config_loader import load_yaml
from src.llm.factory import create_llm
from src.llm.prompts import VALIDATOR_PROMPT


class ValidatorAgent(BaseAgent):
    name = "ValidatorAgent"

    def __init__(self):
        print(">>> [ValidatorAgent] __init__ started")

        cfg = load_yaml("configs/models.yaml")["validator"]
        self.llm = create_llm(cfg)

        print(">>> [ValidatorAgent] model loaded successfully")
        
    def run(self, state: AgentState) -> AgentState:
        self.log(state, "Validating summary using LLM")

        prompt = VALIDATOR_PROMPT.format(summary=state.summary)

        output = self.llm.generate(prompt)

        # Simple parsing (improve later)
        state.validation_score = 0.9
        state.validation_feedback = output.strip()

        return state
