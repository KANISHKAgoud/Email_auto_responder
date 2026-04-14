from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.predictor import predict
from utils.responder import generate_response

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})   # IMPORTANT

@app.route("/predict", methods=["POST"])
def handle_email():
    data = request.get_json()

    if not data or "email" not in data:
        return jsonify({"error": "No email provided"}), 400

    email = data["email"]

    intent, tone = predict(email)
    response = generate_response(intent, tone)

    return jsonify({
        "intent": intent,
        "tone": tone,
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)