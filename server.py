import os
from flask import Flask, request
import telegram

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_API_KEY")
bot = telegram.Bot(token=TOKEN)

@app.route("/", methods=["GET"])
def index():
    return "Bot is alive"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message_text = update.message.text
    bot.send_message(chat_id=chat_id, text="Вы написали: " + message_text)
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
