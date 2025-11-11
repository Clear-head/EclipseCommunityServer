from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from src.common.dto.message_dto import SendMessage, RequestSendMessage
from src.common.utils.logger.custom_logger import get_logger
from src.service.application.message_service import MessageService
from src.service.auth.jwt import validate_jwt_token, get_jwt_user_id

router = APIRouter(
    prefix="/api/message",
    dependencies=[Depends(validate_jwt_token)]
)
logger = get_logger(__name__)

message_service = MessageService()


#   채팅방 목록
@router.get("/")
async def get_message_list(user_id:str = Depends(get_jwt_user_id)):
    return await message_service.get_message_list(user_id)


#   채팅 조회
@router.get("/{sender_id}")
async def get_message_detail(sender_id: str, user_id:str = Depends(get_jwt_user_id)):
    return await message_service.get_message(user_id, sender_id)


#   채팅 보내기
@router.post("/")
async def send_message(dto: RequestSendMessage, user_id:str = Depends(get_jwt_user_id)):
    if await message_service.send_message(user_id, dto):
        return JSONResponse(status_code=200, content="success")
    else:
        return JSONResponse(status_code=400, content="error")