from flask import Flask, render_template, request, jsonify
from gemini_api import ask_gemini
 
app = Flask(__name__)
 
# Chat UI
@app.route("/")
def home():
    return render_template("gemini_app.html")
 
# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_reply = ask_gemini(user_message)
    return jsonify({"reply": bot_reply})
 
if __name__ == "__main__":
    app.run(debug=True)
