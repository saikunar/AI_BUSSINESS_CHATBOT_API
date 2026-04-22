from fastapi import FastAPI
from chatbot import get_response

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Chatbot API"}

@app.post("/chat")
def chat(data: dict):
    query = data["query"]
    response = get_response(query)

    return {"response": response}