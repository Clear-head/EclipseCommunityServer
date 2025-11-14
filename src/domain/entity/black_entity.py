from datetime import datetime
from typing import Optional

from src.domain.entity.base_entity import BaseEntity


class BlackEntity(BaseEntity):
    id: Optional[int] = None
    user_id: str
    phone: str
    email: str
    sanction: str
    period: datetime
    started_at: datetime