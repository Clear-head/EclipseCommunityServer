from datetime import datetime
from typing import List

from pydantic import BaseModel

from src.common.dto.comment_dto import Comment


class Post(BaseModel):
    title: str
    body: str
    user_nickname: str
    merge_history_name: str
    post_id: int
    uploaded_at: datetime


class ResponsePostList(BaseModel):
    posts: List[Post]


class ResponsePostDetail(BaseModel):
    title: str
    body: str
    user_nickname: str
    user_id: str
    comments: List[Comment]
    create_at: datetime


class RequestWritePost(BaseModel):
    title: str
    body: str
    merge_history_id: str


class RequestDeletePost(BaseModel):
    post_id: int