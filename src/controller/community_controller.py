from fastapi import Depends, APIRouter, Header
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.common.dto.comment_dto import RequestWriteComment, RequestDeleteComment
from src.common.dto.post_dto import RequestWritePost, RequestDeletePost
from src.common.utils.logger.custom_logger import get_logger
from src.service.auth.jwt import validate_jwt_token, get_jwt_user_id
from src.service.application.notice_board import NoticeBoard

router = APIRouter(
    prefix="/api/community",
    dependencies=[Depends(validate_jwt_token)]
)
logger = get_logger(__name__)
notice_board = NoticeBoard()

#   커뮤니티 글 목록 (홈)
@router.get("/home/{page}")
async def home(page: int = 1) -> JSONResponse:
    return await notice_board.view_post_list(page)


#   특정 글 읽기
@router.get("/post/{post_id}")
async def read_post(post_id: int) -> JSONResponse:
    return await notice_board.view_post_detail(post_id)


@router.delete("/post")
async def delete_post(dto: RequestDeletePost, user_id:str = Depends(get_jwt_user_id)) -> JSONResponse:
    return JSONResponse(status_code=200, content=(await notice_board.delete_post(user_id, dto)))

#   글 쓰기
@router.post("/post")
async def write_post(dto: RequestWritePost, user_id:str = Depends(get_jwt_user_id)) -> JSONResponse:
    return JSONResponse(status_code=200, content=await notice_board.write_post(user_id, dto))


#   내가 쓴 게시글 보기
@router.post("/post/me")
async def read_post_search(request: Request, user_id: str = Depends(get_jwt_user_id)) -> JSONResponse:
    return await notice_board.search_post(user_id)


#   댓글 쓰기
@router.post("/comment/{post_id}")
async def write_comment(dto: RequestWriteComment, user_id:str = Depends(get_jwt_user_id)):
    return JSONResponse(status_code=200, content=await notice_board.write_comment(user_id, dto))


@router.delete("/comment")
async def delete_comment(dto: RequestDeleteComment, user_id:str = Depends(get_jwt_user_id)) -> JSONResponse:
    return JSONResponse(status_code=200, content=await notice_board.delete_comment(user_id, dto))