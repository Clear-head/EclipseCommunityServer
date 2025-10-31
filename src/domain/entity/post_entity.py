from datetime import datetime

from src.domain.entity.base_entity import BaseEntity


class PostEntity(BaseEntity):
    id: int
    title: str
    body: str
    user_id: str
    created_at: datetime