from src.domain.entity.user_history_entity import UserHistoryEntity
from src.domain.repository.base_repository import BaseRepository
from src.domain.table.user_history_table import user_history_table


class UserHistoryRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.table = user_history_table
        self.entity = UserHistoryEntity

    async def insert(self, item):
        return await super().insert(item)

    async def select(self, **filters):
        return await super().select(**filters)

    async def update(self, item_id, item):
        return await super().update(item_id, item)

    async def delete(self, **filters):
        return await super().delete(**filters)
