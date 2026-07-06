from graph.state import AgentState


def support_agent(state: AgentState):

    state["resolved"] = True

    print("\nSupport Agent")
    print("Issue Resolved")

    return state