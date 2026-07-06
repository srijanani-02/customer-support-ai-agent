from typing import TypedDict, List


class AgentState(TypedDict):
    user_query: str
    intent: str
    retrieved_docs: List[str]
    response: str
    resolved: bool
    escalation_summary: str