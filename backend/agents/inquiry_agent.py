from graph.state import AgentState


def inquiry_agent(state: AgentState):

    query = state["user_query"].lower()

    if "password" in query:
        state["intent"] = "Password Reset"

    elif "payment" in query:
        state["intent"] = "Payment Issue"

    elif "refund" in query:
        state["intent"] = "Refund"

    elif "install" in query:
        state["intent"] = "Installation"

    else:
        state["intent"] = "General Support"

    print("\nInquiry Agent")
    print("Intent:", state["intent"])

    return state