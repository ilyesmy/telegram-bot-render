from flask import Flask, request
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

@app.route('/webhook', methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text == "/start":
            send_message(chat_id, "✅ Hello! Bot is now connected. Send /btc for analysis.")
        elif text == "/btc":
            send_message(chat_id, "📊 BTC Analysis:\nPrice: $59,500\nSupport: $58,000\nResistance: $60,200")
    return "ok"

def send_message(chat_id, text):
    requests.post(URL, json={"chat_id": chat_id, "text": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
