from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import uvicorn

app = FastAPI()

origins = ["http://127.0.0.1:5500", "http://3.224.62.21:8200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class Message(BaseModel):
    name: str
    content: str
    timestamp: datetime = None  # timestamp 필드를 선택적으로 만듦

guestbook = []

@app.post("/guestbook/")
async def add_message(message: Message) -> dict:
    # 현재 시간 기록
    timestamp = datetime.now()
    # 새로운 항목 추가
    new_message = {"name": message.name, "content": message.content, "timestamp": timestamp}
    guestbook.append(new_message)
    return new_message  # 새로운 항목 반환

@app.get("/guestbook/")
async def get_guestbook() -> list:
    return guestbook

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)