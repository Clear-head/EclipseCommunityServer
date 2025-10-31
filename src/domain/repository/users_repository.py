from src.domain.entity.user_entity import UserEntity
from src.domain.repository.base_repository import BaseRepository
from src.domain.table.users_table import users_table


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.table = users_table
        self.entity = UserEntity

    async def insert(self, item):
        return await super().insert(item)

    async def select(self, **filters):
        return await super().select(**filters)

    async def update(self, item_id, item):
        return await super().update(item_id, item)

    async def delete(self, **filters):
        return await super().delete(**filters)
