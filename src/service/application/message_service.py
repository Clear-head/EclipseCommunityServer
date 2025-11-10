from datetime import datetime

from Tools.demo.mcast import receiver
from pydantic import BaseModel

from src.common.dto.message_dto import RequestSendMessage, ResponseReceiveMessage, ResponseReceiveMessageList, \
    MessageDto
from src.common.utils.logger.custom_logger import get_logger
from src.domain.entity.message_entity import MessageEntity
from src.domain.repository.message_repository import MessageRepository
from src.domain.repository.users_repository import UserRepository


class MessageService:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.user_repo = UserRepository()
        self.message_repo = MessageRepository()


    #   메시지 보내기
    async def send_message(self, sender_id: str, dto: RequestSendMessage):
        try:
            self.logger.info(f"sending message with {sender_id} to {dto.receiver_id}")

            await self.message_repo.insert(
                MessageEntity(
                    send_at=datetime.now(),
                    sender=sender_id,
                    body=dto.message,
                    receiver=dto.receiver_id
                )
            )

            return True

        except Exception as e:
            self.logger.error(e)
            return False


    #   채팅창 삭제
    async def delete_message(self, sender_id: str, dto: MessageDto):
        pass



    #   채팅 방 조회
    async def get_message_list(self, user_id: str):
        try:
            self.logger.info(f"getting messages for user {user_id}")
            result = await self.message_repo.select(receiver=user_id, columns=["sender", "create_at"])
            result = sorted(result, key=lambda r: r["create_at"], reverse=True)

            return ResponseReceiveMessageList(
                received_messages=result
            )

        except Exception as e:
            self.logger.error(e)
            raise FileNotFoundError from e


    #   채팅방 들어가서
    async def get_message(self, user_id: str, sender_id: str):

        try:
            self.logger.info(f"getting message for user {user_id} with {sender_id}")

            ans = []
            result = await self.message_repo.select(sender=[user_id, sender_id], receiver=[user_id, sender_id])

            for i in result:
                ans.append(
                    MessageDto(
                        create_at=i.send_at,
                        message=i.body,
                        send_receive= True if i.sender == user_id else False,
                    )
                )

            return ResponseReceiveMessage(messages=sorted(ans, key=lambda r: r["create_at"], reverse=True))

        except Exception as e:
            self.logger.error(e)
            raise FileNotFoundError from e