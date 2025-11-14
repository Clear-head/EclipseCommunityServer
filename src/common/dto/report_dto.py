from typing import Optional

from pydantic import BaseModel


class RequestReportDto(BaseModel):
    reported_user: str
    type: int                       #   0 사용자 신고 1 게시글 2 댓글
    cause_id: Optional[str]                   #   사용자 id, 게시글 id, 댓글 id
    cause: str


class ResponseReportDto(BaseModel):
    with_reported_user: str