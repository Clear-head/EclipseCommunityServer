from datetime import datetime

from src.common.utils.uuid_maker import generate_uuid
from src.domain.entity.base_entity import BaseEntity


class MergeHistoryEntity(BaseEntity):
    id: str
    user_id: str
    template_type: str
    categories_name: str
    visited_at: datetime

    @classmethod
    def from_dto(cls, user_id, template_type, categories_name, visited_at=None, id=None):
        return cls(
            id=id if id is not None else generate_uuid(),
            user_id=user_id,
            visited_at=None if visited_at else datetime.now(),
            categories_name=categories_name,
            template_type=template_type
        )