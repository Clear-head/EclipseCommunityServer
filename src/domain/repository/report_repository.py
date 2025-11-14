from src.domain.entity.report_entity import ReportEntity
from src.domain.repository.base_repository import BaseRepository
from src.domain.table.report_table import report_table


class ReportRepository(BaseRepository):
    def __init__(self):
        super(ReportRepository, self).__init__()
        self.table = report_table
        self.entity = ReportEntity

    async def insert(self, item):
        return await super().insert(item)

    async def select(self, **filters):
        return await super().select(**filters)

    async def update(self, item_id, item):
        return await super().update(item_id, item)

    async def delete(self, **filters):
        return await super().delete(**filters)