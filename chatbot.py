from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Predefined business Q&A
questions = [
    "hello",
    "what is your pricing",
    "what services do you offer",
    "how to contact support",
    "tell me about your company"
]

answers = [
    "Hello! How can I assist you today?",
    "Our pricing starts at $10/month depending on your needs.",
    "We provide AI solutions, automation tools, and analytics services.",
    "You can contact us at support@company.com",
    "We are an AI-driven company helping businesses automate processes."
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def get_response(query: str):
    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, X)
    index = similarity.argmax()

    if similarity[0][index] < 0.3:
        return "I'm not sure. Can you rephrase your question?"
    
    return answers[index]
