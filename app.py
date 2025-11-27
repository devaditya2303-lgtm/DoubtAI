from flask import Flask, request, jsonify, render_template
import os
import openai

app = Flask(__name__)

# Get API key safely from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    # If OpenAI key missing or fails, use fallback reply.
    if not OPENAI_API_KEY:
        return jsonify({"reply": "Darling here 💜 — I can't reach my brain (OpenAI) right now, but I'm with you!"})

    try:
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Darling — a friendly chatbot."},
                {"role": "user", "content": user_msg}
            ]
        )
        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except Exception as e:
        # Fallback message if API errors
        return jsonify({"reply": "Darling 💜: Something went wrong with my brain. But I’m still here to chat!"})

if __name__ == "__main__":
    app.run()
