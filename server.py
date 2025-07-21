import os
import asyncio
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import telegram

app = FastAPI()

# CORS middleware
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

bot = telegram.Bot(token=TELEGRAM_TOKEN)

@app.post("/")
async def handle(request: Request):
    data = await request.json()
    message = data.get("message")
    if not message:
        return {"status": "no message in request"}

    sender_id = message.get("from", {}).get("id")
    if str(sender_id) != str(USER_ID):
        return {"status": "unauthorized"}

    text = message.get("text", "")
    response = f"Вы сказали: {text}"

    await asyncio.to_thread(bot.send_message, CHAT_ID, response)
    return {"status": "ok", "message": response}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run("server:app", host="0.0.0.0", port=port)
