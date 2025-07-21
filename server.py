import os
from fastapi import FastAPI, Request
import uvicorn
import telegram
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware (если используешь фронтенд)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Получаем переменные окружения
TELEGRAM_TOKEN = os.environ["TELEGRAM_API_KEY"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
USER_ID = os.environ["USER_ID"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
OPENAI_BASE_URL = os.environ["OPENAI_BASE_URL"]
OPENAI_MODEL = os.environ["OPENAI_MODEL"]

bot = telegram.Bot(token=TELEGRAM_TOKEN)

@app.post("/")
async def root(request: Request):
    data = await request.json()
    user_input = data.get("message", "")

    if str(data.get("user_id")) != str(USER_ID):
        return {"error": "Unauthorized"}

    # Здесь должен быть запрос к OpenAI
    response = f"Echo: {user_input}"  # Вставь реальный вызов OpenAI API

    bot.send_message(chat_id=CHAT_ID, text=response)
    return {"status": "ok", "message": response}
import uvicorn
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=port)



