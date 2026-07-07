from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from graph.workflow import workflow


app = FastAPI(title="Customer Support AI Agent API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    user_query: str


@app.get("/")
def home():

    return {

        "message": "Customer Support AI Agent Backend Running 🚀"

    }


@app.post("/chat")
def chat(request: ChatRequest):

    initial_state = {

        "user_query": request.user_query,

        "conversation_status": "ACTIVE",

        "awaiting_additional_help": False,

        "intent": "",

        "needs_more_info": False,

        "follow_up_question": "",

        "retrieved_docs": [],

        "response": "",

        "resolved": False,

        "show_quick_actions": False,

        "escalation_required": False,

        "escalation_summary": ""

    }

    result = workflow.invoke(initial_state)

    return {

        "response": result["response"],

        "intent": result["intent"],

        "resolved": result["resolved"],

        "show_quick_actions": result["show_quick_actions"],

        "awaiting_additional_help": result["awaiting_additional_help"],

        "escalation_summary": result["escalation_summary"]

    }