from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


#   채팅 보내기 요청
class RequestSendMessage(BaseModel):
    receiver_id: str
    message: str


#   채팅방 리스트 응답
class SendMessage(BaseModel):
    sender: str
    create_at: datetime
    last_message: str


class ResponseReceiveMessageList(BaseModel):
    chat_rooms: List[SendMessage]


#   채팅방 디테일 요청
class RequestReceiveMessage(BaseModel):
    sender_id: str


#   채팅방 디테일 응답
class MessageDto(BaseModel):
    send_receive: bool      #   true 면 내가 보낸거, false 면 상대가 보낸거
    message: str
    send_at: datetime


class ResponseReceiveMessage(BaseModel):
    messages: List[MessageDto]