from sqlalchemy import desc

from src.config.maria_engine import get_engine
from src.domain.entity.post_entity import PostEntity
from src.domain.repository.base_repository import BaseRepository
from src.domain.table.posts_table import posts_table


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

    async def select_root(self, page):
        try:
            engine = await get_engine()
            page -= 1

            async with engine.begin() as conn:
                stmt = self.table.select().offset(page*10).limit(10).order_by(desc(self.table.c.create_at))
                result = await conn.execute(stmt)

            return [self.entity(**i) for i in result.mappings()]

        except Exception as e:
            self.logger.error(f"insert error: {e}")
            raise e