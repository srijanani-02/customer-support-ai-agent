from graph.state import AgentState


def resolution_agent(state: AgentState):

    print("\n========== Resolution Agent ==========")

    if not state["escalation_required"]:

        print("No escalation required.")

        return state

    # Message shown to the customer
    state["response"] = (
        "I'm sorry, but your request requires assistance from our human support team.\n\n"
        "Your request has been forwarded, and a support representative will assist you shortly."
    )

    # Internal escalation summary
    state["escalation_summary"] = f"""
========== HUMAN SUPPORT SUMMARY ==========

Customer Query:
{state["user_query"]}

Detected Intent:
{state["intent"]}

Conversation Status:
{state["conversation_status"]}

Reason for Escalation:
The request requires official company information, account-specific action,
or human intervention that cannot be safely handled by the AI assistant.

Status:
Pending Human Support

==========================================
""".strip()

    print("Escalation summary created.")

    return state