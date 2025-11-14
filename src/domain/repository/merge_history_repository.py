from src.domain.entity.merge_history_entity import MergeHistoryEntity
from src.domain.repository.base_repository import BaseRepository
from src.domain.table.table_merge_history import merge_history_table


class MergeHistoryRepository(BaseRepository):
    def __init__(self):
        super(MergeHistoryRepository, self).__init__()
        self.table = merge_history_table
        self.entity = MergeHistoryEntity

    async def insert(self, item):
        return await super().insert(item)

    async def select(self, **filters):
        return await super().select(**filters)

    async def update(self, item_id, item):
        return await super().update(item_id, item)

    async def delete(self, **filters):
        return await super().delete(**filters)