from fastapi import FastAPI, Request
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    return {"status": "alive"}

@app.post("/webhook")
async def process_webhook(request: Request):
    data = await request.json()
    logging.info(f"📨 Новое сообщение: {data}")
    return {"ok": True}

