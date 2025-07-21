import os
import asyncio
from fastapi import FastAPI, Request
import telegram
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Разрешаем CORS (на всякий случай)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Переменные окружения
TELEGRAM_TOKEN = os.environ["TELEGRAM_API_KEY"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
USER_ID = os.environ["USER_ID"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
OPENAI_BASE_URL = os.environ["OPENAI_BASE_URL"]
OPENAI_MODEL = os.environ["OPENAI_MODEL"]

bot = telegram.Bot(token=TELEGRAM_TOKEN)

@app.post("/")
async def handle(request: Request):
    data = await request.json()

    # Проверка наличия сообщения
    message = data.get("message")
    if not message:
        return {"status": "no message in request"}

    text = message.get("text", "")
    sender_id = message.get("from", {}).get("id")

    # Проверка ID пользователя
    if str(sender_id) != str(USER_ID):
        return {"status": "unauthorized"}

    # Генерация ответа (заглушка, пока нет OpenAI-запроса)
    response = f"Вы сказали: {text}"

    # Отправка сообщения через Telegram API в фоне
    await asyncio.to_thread(bot.send_message, CHAT_ID, response)

    return {"status": "ok"}


