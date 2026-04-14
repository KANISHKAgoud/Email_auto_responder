import pickle
from utils.preprocess import clean_text

vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))
intent_model = pickle.load(open("model/intent_model.pkl", "rb"))
tone_model = pickle.load(open("model/tone_model.pkl", "rb"))

def predict(email):
    cleaned = clean_text(email)
    vect = vectorizer.transform([cleaned])

    intent = intent_model.predict(vect)[0]
    tone = tone_model.predict(vect)[0]

    return intent, tone