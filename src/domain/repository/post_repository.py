from src.domain.repository.base_repository import BaseRepository
from src.domain.table.posts_table import posts_table
from src.domain.entity.post_entity import PostEntity


class PostRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.table = posts_table
        self.entity = PostEntity


    async def insert(self, item):
        return await super().insert(item)

    async def select(self, **filters):
        return await super().select(**filters)

    async def update(self, item_id, item):
        return await super().update(item_id, item)

    async def delete(self, **filters):
        return await super().delete(**filters)