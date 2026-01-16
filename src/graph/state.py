from typing import List, Dict, Any
from pydantic import BaseModel, Field

class AgentState(BaseModel):
    run_id: str
    mode: str = "demo"

    plan: Dict[str, Any] = Field(default_factory=dict)
    sources: List[Dict[str, Any]] = Field(default_factory=list)

    summary: str | None = None
    validation_score: float | None = None
    validation_feedback: str | None = None

    logs: List[str] = Field(default_factory=list)
