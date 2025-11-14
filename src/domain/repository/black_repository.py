from src.domain.entity.black_entity import BlackEntity
from src.domain.repository.base_repository import BaseRepository
from src.domain.table.black_table import black_table


class BlackRepository(BaseRepository):
    def __init__(self):
        super(BlackRepository, self).__init__()
        self.table = black_table
        self.entity = BlackEntity

    async def insert(self, item):
        return await super().insert(item)

    async def select(self, **filters):
        return await super().select(**filters)

    async def update(self, item_id, item):
        return await super().update(item_id, item)

    async def delete(self, **filters):
        return await super().delete(**filters)
