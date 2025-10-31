from datetime import datetime

from src.domain.entity.base_entity import BaseEntity


class MessageEntity(BaseEntity):
    sender: str
    receiver: str
    body: str
    send_at: datetime