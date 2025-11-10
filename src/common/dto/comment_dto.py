from datetime import datetime

from pydantic import BaseModel


class RequestWriteComment(BaseModel):
    post_id: int
    body: str


class Comment(BaseModel):
    user_id: str
    user_nickname: str
    create_at: datetime
    body: str

class RequestDeleteComment(BaseModel):
    post_id: int
    comment_id: int