from graph.state import AgentState


def conversation_agent(state: AgentState):

    print("\n========== Conversation Agent ==========")

    query = state["user_query"].strip().lower()

    # Remove common punctuation
    query = (
        query.replace("!", "")
             .replace(".", "")
             .replace(",", "")
             .replace("?", "")
    )

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
                "What else can I help you with today?"
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
    # Greetings
    # -------------------------------------------------

    if query.startswith(("hi", "hii", "hiii")):

        state["response"] = "Hello! 👋 How can I assist you today?"

    elif query.startswith(("hey", "heyy", "heyyy")):

        state["response"] = "Hi! 👋 How can I help you today?"

    elif query.startswith("hello"):

        state["response"] = "Hello! 👋 How can I assist you today?"

    elif query.startswith(("gm", "good morning")):

        state["response"] = "Good morning! ☀️ How can I help you today?"

    elif query.startswith("good afternoon"):

        state["response"] = "Good afternoon! 😊 How can I help you today?"

    elif query.startswith(("ge", "good evening")):

        state["response"] = "Good evening! 🌙 How can I help you today?"

    elif query.startswith(("thanks", "thank")):

        state["response"] = "You're welcome! 😊"

    elif query.startswith(("bye", "byee", "byeee")):

        state["response"] = (
            "Thank you for contacting SmartAssist.\n"
            "Have a wonderful day! 👋"
        )

    else:

        state["conversation_status"] = "ACTIVE"

        print("Forwarding to Inquiry Agent.")

        return state

    # -------------------------------------------------
    # Conversation handled
    # -------------------------------------------------

    state["resolved"] = True
    state["needs_more_info"] = False
    state["show_quick_actions"] = False
    state["awaiting_additional_help"] = False

    state["intent"] = "Conversation"
    state["conversation_status"] = "COMPLETED"
    state["escalation_required"] = False

    print("Handled by Conversation Agent.")

    return state