from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Message(BaseModel):
    name: str
    content: str

guestbook = []

@app.post("/guestbook/")
async def add_message(message: Message) -> dict:
    # 현재 시간 기록
    timestamp = datetime.now()
    # 새로운 항목 추가
    guestbook.append({"name": message.name, "content": message.content, "timestamp": timestamp})
    return {"message": "Message added successfully"}

@app.get("/guestbook/")
async def get_guestbook() -> dict:
    return guestbook

