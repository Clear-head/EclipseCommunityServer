from src.domain.entity.comment_entity import CommentEntity
from src.domain.repository.base_repository import BaseRepository
from src.domain.table import comment_table


class CommentRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.table = comment_table
        self.entity = CommentEntity


    async def insert(self, item):
        return await super().insert(item)

    async def select(self, **filters):
        return await super().select(**filters)

    async def update(self, item_id, item):
        return await super().update(item_id, item)

    async def delete(self, **filters):
        return await super().delete(**filters)