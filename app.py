from flask import Flask, request, jsonify, render_template
import os
import openai

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "")

    # If OpenAI key missing or not working, show fallback reply
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Darling — a friendly chatbot."},
                {"role": "user", "content": msg},
            ]
        )
        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "Darling here 💜 — my brain (OpenAI) isn't responding, but I'm here with you!"})

if __name__ == "__main__":
    app.run()
