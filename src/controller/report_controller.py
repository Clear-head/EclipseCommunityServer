from fastapi import APIRouter, Depends

from src.common.dto.report_dto import RequestReportDto
from src.common.utils.logger.custom_logger import get_logger
from src.service.application.report_service import ReportService
from src.service.auth.jwt import get_jwt_user_id

router = APIRouter(
    prefix="/api/report"
)
logger = get_logger(__name__)


@router.post("/")
async def report(dto: RequestReportDto, user_id: str = Depends(get_jwt_user_id)):
    await ReportService().report_user(dto, user_id)