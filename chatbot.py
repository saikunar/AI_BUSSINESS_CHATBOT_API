def get_response(query):
    query = query.lower()

    if "price" in query:
        return "Our pricing starts from $10/month."

    elif "service" in query:
        return "We offer AI chatbot solutions for businesses."

    elif "hello" in query:
        return "Hello! How can I help you?"

    else:
        return "Sorry, I didn't understand. Can you rephrase?"