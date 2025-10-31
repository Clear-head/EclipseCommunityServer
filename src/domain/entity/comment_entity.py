from datetime import datetime

from src.domain.entity.base_entity import BaseEntity


class CommentEntity(BaseEntity):
    id: str
    post_id: str
    user_id: str
    body: str
    created_at: datetime