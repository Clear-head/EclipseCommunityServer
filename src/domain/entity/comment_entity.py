from datetime import datetime
from typing import Optional

from src.domain.entity.base_entity import BaseEntity


class CommentEntity(BaseEntity):
    id: Optional[int] = None
    post_id: int
    user_id: str
    body: str
    create_at: datetime