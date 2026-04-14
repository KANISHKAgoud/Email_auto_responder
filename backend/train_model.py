import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Sample dataset (you can expand later)
data = {
    "email": [
        "I am very unhappy with your service",
        "Can we schedule a meeting tomorrow?",
        "I want to apply for the job",
        "Thanks for your help",
        "This is urgent, please respond quickly"
    ],
    "intent": [
        "complaint",
        "meeting",
        "job",
        "gratitude",
        "urgent"
    ],
    "tone": [
        "angry",
        "formal",
        "formal",
        "friendly",
        "urgent"
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["email"])

# Intent model
intent_model = LogisticRegression()
intent_model.fit(X, df["intent"])

# Tone model
tone_model = LogisticRegression()
tone_model.fit(X, df["tone"])

# Save models
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))
pickle.dump(intent_model, open("model/intent_model.pkl", "wb"))
pickle.dump(tone_model, open("model/tone_model.pkl", "wb"))

print("Models trained and saved!")