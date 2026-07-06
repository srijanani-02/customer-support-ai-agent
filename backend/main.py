from fastapi import FastAPI

app = FastAPI(title="Customer Support AI Agent API")

@app.get("/")
def home():
    return {
        "message": "Customer Support AI Agent Backend Running 🚀"
    }