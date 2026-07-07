from typing import TypedDict, List


class AgentState(TypedDict):
    # User Input
    user_query: str

    # Conversation Agent
    conversation_status: str
    awaiting_additional_help: bool

    # Inquiry Agent
    intent: str
    needs_more_info: bool
    follow_up_question: str

    # Knowledge Agent
    retrieved_docs: List[str]
    response: str

    # Support Agent
    resolved: bool
    show_quick_actions: bool

    # Resolution Agent
    escalation_required: bool
    escalation_summary: str