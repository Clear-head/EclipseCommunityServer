from fastapi import Depends, APIRouter
from starlette.responses import JSONResponse

from src.common.utils.logger.custom_logger import get_logger
from src.service.auth.jwt import validate_jwt_token

router = APIRouter(
    prefix="/api/comunity",
    dependencies=[Depends(validate_jwt_token)]
)
logger = get_logger(__name__)

#   커뮤니티 글 목록 (홈)
@router.get("/home/{page}")
async def home(page: str = None, ) -> JSONResponse:
    pass


#   특정 글 읽기
@router.get("/read-post")
async def read_post():
    pass


#   글 쓰기
@router.get("/write-post")
async def write_post() -> JSONResponse:
    pass


#   댓글 쓰기
@router.get("/write-commnet/{post_id}")
async def write_comment(post_id: str):
    pass