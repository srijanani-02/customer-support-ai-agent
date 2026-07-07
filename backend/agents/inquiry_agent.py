from graph.state import AgentState


def inquiry_agent(state: AgentState):

    print("\n========== Inquiry Agent ==========")

    query = state["user_query"].strip().lower()

    state["needs_more_info"] = False
    state["follow_up_question"] = ""

    # ---------------- Password ----------------

    if "password" in query:

        state["intent"] = "Password Reset"

        if len(query.split()) <= 2:

            state["needs_more_info"] = True

            state["follow_up_question"] = (
                "Could you please describe your password issue?\n"
                "For example, are you trying to reset, recover, or change your password?"
            )

    # ---------------- Refund ----------------

    elif "refund" in query:

        state["intent"] = "Refund Request"

        if len(query.split()) <= 2:

            state["needs_more_info"] = True

            state["follow_up_question"] = (
                "Could you provide more details about your refund request?"
            )

    # ---------------- Order ----------------

    elif "order" in query:

        state["intent"] = "Order Tracking"

        if len(query.split()) <= 2:

            state["needs_more_info"] = True

            state["follow_up_question"] = (
                "Could you provide your Order ID so I can help you track your order?"
            )

    # ---------------- Payment ----------------

    elif "payment" in query:

        state["intent"] = "Payment Issue"

        if len(query.split()) <= 2:

            state["needs_more_info"] = True

            state["follow_up_question"] = (
                "Could you explain the payment issue you're facing?"
            )

    # ---------------- Installation ----------------

    elif "install" in query:

        state["intent"] = "Installation"

        if len(query.split()) <= 2:

            state["needs_more_info"] = True

            state["follow_up_question"] = (
                "Could you describe your installation problem?"
            )

    # ---------------- Technical ----------------

    elif any(word in query for word in [
        "error",
        "issue",
        "problem",
        "bug",
        "technical"
    ]):

        state["intent"] = "Technical Support"

    # ---------------- General ----------------

    else:

        state["intent"] = "General Support"

    print("Intent :", state["intent"])

    if state["needs_more_info"]:

        state["response"] = state["follow_up_question"]

        print("Need more information from customer.")

    else:

        print("Enough information received.")

    return state