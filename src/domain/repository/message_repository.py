from src.domain.entity.message_entity import MessageEntity
from src.domain.repository.base_repository import BaseRepository
from src.domain.table.message_table import message_table


class MessageRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.table = message_table
        self.entity = MessageEntity


    async def insert(self, item):
        return await super().insert(item)

    async def select(self, **filters):
        return await super().select(**filters)

    async def update(self, item_id, item):
        return await super().update(item_id, item)

    async def delete(self, **filters):
        return await super().delete(**filters)