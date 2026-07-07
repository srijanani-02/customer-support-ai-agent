from graph.state import AgentState


def resolution_agent(state: AgentState):

    print("\n========== Resolution Agent ==========")

    if not state["escalation_required"]:

        print("No escalation required.")

        return state

    state["escalation_summary"] = f"""
========== HUMAN SUPPORT SUMMARY ==========

Customer Query:
{state["user_query"]}

Detected Intent:
{state["intent"]}

AI Response:
{state["response"]}

Reason for Escalation:
The AI could not find sufficient information in the knowledge base.

Status:
Pending Human Support

==========================================
""".strip()

    print("Escalation summary created.")

    return state