from flask import Flask, request
import telegram
import os

app = Flask(__name__)

# Получаем токен Telegram из переменных окружения
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telegram.Bot(token=TOKEN)

# 👉 ОБЯЗАТЕЛЬНЫЙ маршрут для Render проверки
@app.route("/", methods=["GET"])
def home():
    return "Bot is alive"

# 👉 Обработка Telegram webhook
@app.route(f"/{TOKEN}", methods=["POST"])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    message_text = update.message.text

    # Ответ
    bot.send_message(chat_id=chat_id, text="Вы написали: " + message_text)
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
