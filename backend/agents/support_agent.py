from graph.state import AgentState


def support_agent(state: AgentState):

    print("\n========== Support Agent ==========")

    response = state["response"].lower()

    state["resolved"] = False
    state["escalation_required"] = False
    state["show_quick_actions"] = False
    state["awaiting_additional_help"] = False

    # Inquiry Agent requested more information
    if state["needs_more_info"]:

        print("Waiting for customer to provide more information.")

        return state

    # AI couldn't answer from the knowledge base
    if (
        "couldn't find this information" in response
        or "couldn't find any relevant information" in response
    ):

        state["resolved"] = False
        state["escalation_required"] = True
        state["show_quick_actions"] = False
        state["awaiting_additional_help"] = False

        state["response"] = (
            "I'm sorry, but I couldn't find the required information in our knowledge base.\n\n"
            "Your request will be forwarded to our human support team for further assistance."
        )

        print("Escalating to Resolution Agent.")

        return state

    # AI successfully answered
    state["resolved"] = True

    # Wait for the user's "yes" or "no"
    state["awaiting_additional_help"] = True

    # Don't show quick actions yet
    state["show_quick_actions"] = False

    state["response"] += (
        "\n\n"
        "✅ I hope this resolved your issue.\n\n"
        "Is there anything else I can help you with?"
    )

    print("Issue handled successfully.")

    return state