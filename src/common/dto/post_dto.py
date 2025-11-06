from pydantic import BaseModel


class RequestPost(BaseModel):
    merge_history_id: str
    title: str
    body: str