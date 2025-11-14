from datetime import datetime
from typing import Optional

from src.domain.entity.base_entity import BaseEntity


class MessageEntity(BaseEntity):
    id: Optional[int] = None
    sender: str
    receiver: str
    body: str
    send_at: datetime