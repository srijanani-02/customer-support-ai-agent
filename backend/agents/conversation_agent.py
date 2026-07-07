from graph.state import AgentState


def conversation_agent(state: AgentState):

    print("\n========== Conversation Agent ==========")

    query = state["user_query"].strip().lower()

    # -------------------------------------------------
    # Waiting for user after an issue has been resolved
    # -------------------------------------------------

    if state["awaiting_additional_help"]:

        yes_words = [
            "yes",
            "yeah",
            "yep",
            "sure",
            "okay",
            "ok"
        ]

        no_words = [
            "no",
            "nope",
            "nah"
        ]

        if query in yes_words:

            state["response"] = (
                "Sure! 😊\n\n"
                "Please choose one of the support topics below."
            )

            state["show_quick_actions"] = True
            state["awaiting_additional_help"] = False

            state["intent"] = "Conversation"
            state["resolved"] = True
            state["conversation_status"] = "COMPLETED"
            state["escalation_required"] = False

            print("Showing Quick Actions.")

            return state

        elif query in no_words:

            state["response"] = (
                "You're welcome! 😊\n\n"
                "Thank you for contacting SmartAssist.\n"
                "Have a wonderful day! 👋"
            )

            state["show_quick_actions"] = False
            state["awaiting_additional_help"] = False

            state["intent"] = "Conversation"
            state["resolved"] = True
            state["conversation_status"] = "COMPLETED"
            state["escalation_required"] = False

            print("Conversation ended.")

            return state

    # -------------------------------------------------
    # Normal Greetings
    # -------------------------------------------------

    greetings = {
        "hi": "Hello! 👋 How can I assist you today?",
        "hello": "Hello! 👋 How can I assist you today?",
        "hey": "Hi! 👋 How can I help you today?",
        "good morning": "Good morning! ☀️ How can I help you today?",
        "good afternoon": "Good afternoon! 😊 How can I help you today?",
        "good evening": "Good evening! 🌙 How can I help you today?",
        "thanks": "You're welcome! 😊",
        "thank you": "You're welcome! 😊",
        "bye": "Thank you for contacting SmartAssist. Have a great day! 👋"
    }

    if query in greetings:

        state["response"] = greetings[query]

        state["resolved"] = True
        state["needs_more_info"] = False
        state["show_quick_actions"] = False
        state["awaiting_additional_help"] = False

        state["intent"] = "Conversation"
        state["conversation_status"] = "COMPLETED"
        state["escalation_required"] = False

        print("Handled by Conversation Agent.")

        return state

    # -------------------------------------------------
    # Forward to next agent
    # -------------------------------------------------

    state["conversation_status"] = "ACTIVE"

    print("Forwarding to Inquiry Agent...")

    return state