from datetime import datetime

from src.common.dto.report_dto import RequestReportDto, ResponseReportDto
from src.common.utils.logger.custom_logger import get_logger
from src.domain.entity.report_entity import ReportEntity
from src.domain.repository.report_repository import ReportRepository


class ReportService:
    def __init__(self):
        self.logger = get_logger(__name__)
        self.repo = ReportRepository()


    async def report_user(self, dto: RequestReportDto, user_id: str):
        try:
            self.logger.info(f"Report for {user_id}")
            print(dto)

            entity = ReportEntity(
                reporter=user_id,
                user_id=dto.reported_user,
                type=dto.type,
                cause_id=dto.cause_id,
                cause=dto.cause,
                reported_at=datetime.now(),
            )

            await self.repo.insert(entity)

            num = await self.repo.select(
                user_id=dto.reported_user,
                reporter=user_id,
            )

            return ResponseReportDto(
                with_reported_user=f"접수번호 : {num[0].id}\nid: {dto.reported_user}에 대한 신고가 접수되었습니다."
            )

        except Exception as e:
            self.logger.error(e)
            raise e