from flask import Flask, request, jsonify, render_template
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Darling — a friendly chatbot."},
            {"role": "user", "content": msg}
        ]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()
