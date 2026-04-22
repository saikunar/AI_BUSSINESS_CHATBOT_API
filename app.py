from fastapi import FastAPI
from chatbot import get_response

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Business Chatbot API"}

@app.post("/chat")
def chat(data: dict):
    query = data.get("query")
    response = get_response(query)

    return {
        "query": query,
        "response": response,
        "status": "success"
    }
