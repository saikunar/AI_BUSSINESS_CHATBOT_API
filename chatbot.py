def get_response(query: str):
    query = query.lower()

    # Greetings
    if any(word in query for word in ["hello", "hi", "hey"]):
        return "Hello! How can I assist you today?"

    # Pricing
    elif "price" in query or "cost" in query:
        return "Our pricing starts at $10/month depending on your needs."

    # Services
    elif "service" in query:
        return "We offer AI solutions, automation tools, and data analytics services."

    # Support
    elif "support" in query or "help" in query:
        return "You can contact support at support@company.com"

    # Default
    else:
        return "I'm not sure about that. Could you please rephrase your question?"
