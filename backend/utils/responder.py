def generate_response(intent, tone):

    if intent == "complaint":
        return "We sincerely apologize for the inconvenience. We are working on resolving your issue."

    elif intent == "meeting":
        return "Sure, I would be happy to schedule a meeting. Please let me know a suitable time."

    elif intent == "job":
        return "Thank you for your interest. We will review your application and get back to you soon."

    elif intent == "gratitude":
        return "You're welcome! Glad I could help."

    elif intent == "urgent":
        return "We have received your urgent request and will respond as soon as possible."

    return "Thank you for your email."