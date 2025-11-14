from datetime import datetime
from typing import Optional

from src.domain.entity.base_entity import BaseEntity


class PostEntity(BaseEntity):
    id: Optional[int] = None
    title: str
    body: str
    user_id: str
    create_at: datetime
    merge_history_id: str