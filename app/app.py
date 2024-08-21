import os
from typing import Any, Dict

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI
from services.email_analyzer import analyze_emails

load_dotenv()

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.route("/")
def index() -> Dict[str, str]:
    return jsonify({"message": "Yup, all working fine!"})


@app.route("/analyze_emails", methods=["POST"])
def analyze_emails_route() -> Any:
    emails = request.json
    if not emails or not isinstance(emails, list):
        return jsonify({"error": "Invalid input. Expected a list of emails."}), 400

    try:
        analyzed_emails = analyze_emails(emails, client)
        return jsonify(analyzed_emails)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        debug=os.getenv("FLASK_DEBUG", "False").lower() == "true",
    )
