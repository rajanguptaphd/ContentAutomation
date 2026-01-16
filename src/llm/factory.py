from src.llm.hf_backend import HFBackend
from src.llm.ollama_backend import OllamaBackend

def create_llm(cfg: dict):
    backend = cfg["backend"]

    if backend == "hf":
        return HFBackend(
            model_name=cfg["model_name"],
            device=cfg["device"],
            max_new_tokens=cfg["max_new_tokens"],
        )

    if backend == "ollama":
        return OllamaBackend(
            model_name=cfg["model_name"],
            max_new_tokens=cfg["max_new_tokens"],
        )

    raise ValueError(f"Unknown LLM backend: {backend}")
