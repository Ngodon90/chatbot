import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAHgj4r56eEBO5CZBsVXPStVF9MWkeFjKzcwKL4jG8AmvZAKVsHgEsFxwBZApEZCWcePZC4fT2jYstK00fGRbBbckMEVVczZAeHPyh3ZCeZA5o1mMxuqwpI0pTrFHrZBqjAQLygD6GUCZCYSJEGpZC6NO3wTwnW2tHuRb3RG8GT4UW25WW7llMqpGsT7q5YgZAg8Tgs7"
VERIFY_TOKEN = "171119090216"

@app.route("/", methods=["GET"])
def home():
    return "Chatbot Facebook đang chạy!"

# Xác thực Webhook với Facebook
@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Xác thực thất bại!", 403

# Xử lý tin nhắn từ Messenger
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if "message" in messaging_event:
                    sender_id = messaging_event["sender"]["id"]
                    message_text = messaging_event["message"]["text"]

                    # Gửi tin nhắn phản hồi
                    send_message(sender_id, f"Bạn vừa nói: {message_text}")

    return "OK", 200

# Hàm gửi tin nhắn
def send_message(recipient_id, message_text):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"
    headers = {"Content-Type": "application/json"}
    data = {"recipient": {"id": recipient_id}, "message": {"text": message_text}}
    requests.post(url, headers=headers, json=data)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
