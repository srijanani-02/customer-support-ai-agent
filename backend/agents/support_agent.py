from graph.state import AgentState


def support_agent(state: AgentState):

    print("\n========== Support Agent ==========")

    response = state["response"].strip()

    state["resolved"] = False
    state["escalation_required"] = False
    state["show_quick_actions"] = False
    state["awaiting_additional_help"] = False

    # --------------------------------------------------
    # Inquiry Agent is waiting for more information
    # --------------------------------------------------

    if state["needs_more_info"]:

        print("Waiting for customer to provide more information.")

        return state

    # --------------------------------------------------
    # OpenRouter requested escalation
    # --------------------------------------------------

    if response.upper() == "ESCALATE":

        state["resolved"] = False
        state["escalation_required"] = True

        print("Escalating to Resolution Agent.")

        return state

    # --------------------------------------------------
    # Issue handled successfully
    # --------------------------------------------------

    state["resolved"] = True
    state["awaiting_additional_help"] = True
    state["show_quick_actions"] = False

    state["response"] += (

        "\n\n"

        "✅ I hope this resolved your issue.\n\n"

        "Do you need help with anything else? (Yes / No)"

    )

    print("Issue handled successfully.")

    return state