from langgraph.graph import StateGraph, START, END

from graph.state import AgentState

from agents.conversation_agent import conversation_agent
from agents.inquiry_agent import inquiry_agent
from agents.knowledge_agent import knowledge_agent
from agents.support_agent import support_agent
from agents.resolution_agent import resolution_agent


# --------------------------------------------------
# Routing after Conversation Agent
# --------------------------------------------------

def conversation_router(state: AgentState):

    if state["intent"] == "Conversation":
        return END

    return "inquiry"


# --------------------------------------------------
# Routing after Inquiry Agent
# --------------------------------------------------

def inquiry_router(state: AgentState):

    if state["needs_more_info"]:
        return END

    return "knowledge"


# --------------------------------------------------
# Routing after Support Agent
# --------------------------------------------------

def support_router(state: AgentState):

    if state["escalation_required"]:
        return "resolution"

    return END


# --------------------------------------------------
# Build Workflow
# --------------------------------------------------

builder = StateGraph(AgentState)

builder.add_node(
    "conversation",
    conversation_agent
)

builder.add_node(
    "inquiry",
    inquiry_agent
)

builder.add_node(
    "knowledge",
    knowledge_agent
)

builder.add_node(
    "support",
    support_agent
)

builder.add_node(
    "resolution",
    resolution_agent
)

# ---------------- START ----------------

builder.add_edge(
    START,
    "conversation"
)

# ---------------- Conversation ----------------

builder.add_conditional_edges(

    "conversation",

    conversation_router,

    {

        "inquiry": "inquiry",

        END: END

    }

)

# ---------------- Inquiry ----------------

builder.add_conditional_edges(

    "inquiry",

    inquiry_router,

    {

        "knowledge": "knowledge",

        END: END

    }

)

# ---------------- Knowledge ----------------

builder.add_edge(

    "knowledge",

    "support"

)

# ---------------- Support ----------------

builder.add_conditional_edges(

    "support",

    support_router,

    {

        "resolution": "resolution",

        END: END

    }

)

# ---------------- Resolution ----------------

builder.add_edge(

    "resolution",

    END

)

workflow = builder.compile()