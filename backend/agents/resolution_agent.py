from graph.state import AgentState


def resolution_agent(state: AgentState):

    state["escalation_summary"] = (
        f"Customer Issue: {state['user_query']}\n"
        f"Detected Intent: {state['intent']}"
    )

    print("\nResolution Agent")

    return state