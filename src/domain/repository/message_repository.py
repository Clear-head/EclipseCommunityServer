from sqlalchemy import case, select, func

from src.config.maria_engine import get_engine
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

    async def get_latest_messages_by_sender(self, user_id):

        try:
            engine = await get_engine()
            async with engine.begin() as conn:
                # 상대방 계산
                counterpart = case(
                    (self.table.c.sender == user_id, self.table.c.receiver),
                    else_=self.table.c.sender
                )

                ranked_messages = (
                    select(
                        self.table.c.sender,
                        self.table.c.receiver,
                        self.table.c.send_at,
                        self.table.c.body,
                        counterpart.label('counterpart'),
                        func.row_number()
                        .over(
                            partition_by=counterpart,
                            order_by=self.table.c.send_at.desc()
                        )
                        .label('rn')
                    )
                    .where(
                        (self.table.c.sender == user_id) |
                        (self.table.c.receiver == user_id)
                    )
                    .subquery('RankedMessages')
                )

                # 메인 쿼리
                query = (
                    select(
                        ranked_messages.c.counterpart,
                        ranked_messages.c.body,
                        ranked_messages.c.send_at
                    )
                    .where(ranked_messages.c.rn == 1)
                    .order_by(ranked_messages.c.send_at.desc())
                )

                result = await conn.execute(query)
                results = result.fetchall()

            return results

        except Exception as e:
            self.logger.error(f"get_latest_messages_by_sender error: {e}")
            raise e