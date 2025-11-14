from datetime import datetime
from typing import Optional

from src.domain.entity.base_entity import BaseEntity


class ReportEntity(BaseEntity):
    id: Optional[int] = None
    user_id: str
    type: int
    cause_id: Optional[str]
    cause: str
    reporter: str
    reported_at: datetime
    is_processed : bool