🤖 AI Business Chatbot API

FastAPI-based AI chatbot that handles business queries and returns intelligent responses in real-time.

---

🚀 Live Demo

👉 https://your-render-link.onrender.com/docs

---

🔥 Features

- Real-time chatbot responses
- REST API using FastAPI
- Lightweight and fast backend
- Ready for deployment
- Intent-based response system (basic NLP logic)
---

🧠 Tech Stack

- Python
- FastAPI
- Uvicorn

---

⚙️ How It Works

1. User sends a query
2. Backend processes input
3. Chatbot generates response
4. Returns output via API

---

📡 API Endpoint

POST "/chat"

📥 Input

{
  "query": "Hello"
}

📤 Output

{
  "response": "Hello! How can I assist you?"
}

---

💻 Run Locally

pip install -r requirements.txt
python -m uvicorn app:app --reload

---

🌐 Deployment

This project is deployed on Render using:

uvicorn app:app --host 0.0.0.0 --port 10000

---

👨‍💻 Author

Sai Kumar
Aspiring AI/ML Engineer

---
