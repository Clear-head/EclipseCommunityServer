from datetime import datetime

from src.common.dto.comment_dto import RequestDeleteComment
from src.common.dto.post_dto import Post, ResponsePostList, Comment, ResponsePostDetail, RequestWritePost, \
    RequestDeletePost
from src.common.utils.logger.custom_logger import get_logger
from src.domain.entity.comment_entity import CommentEntity
from src.domain.entity.post_entity import PostEntity
from src.domain.repository.comment_repository import CommentRepository
from src.domain.repository.merge_history_repository import MergeHistoryRepository
from src.domain.repository.post_repository import PostRepository
from src.domain.repository.user_history_repository import UserHistoryRepository
from src.domain.repository.users_repository import UserRepository


class NoticeBoard:
    def __init__(self):
        self.post_repo = PostRepository()
        self.comment_repo = CommentRepository()
        self.merge_history_repo = MergeHistoryRepository()
        self.user_history_repo = UserHistoryRepository()
        self.user_repo = UserRepository()
        self.logger = get_logger(__name__)


    #   게시글 작성
    async def write_post(self, user_id, dto: RequestWritePost):
        try:
            self.logger.info(f"write post: {user_id}")
            post = PostEntity(
                title=dto.title,
                body=dto.body,
                create_at=datetime.now(),
                merge_history_id=dto.merge_history_id,
                user_id=user_id
            )

            await self.post_repo.insert(post)

            return "success"
        except Exception as e:
            self.logger.error(e)


    #   글 목록 보기
    async def view_post_list(self, page):
        try:
            self.logger.info(f"view post list: {page}")

            result = []

            posts = await self.post_repo.select_root(page = page)
            self.logger.info(f"view post: {posts}")
            if posts:
                for post in posts:
                    user = (await self.user_repo.select(user_id = post.user_id))[0]
                    self.logger.info(f"view post user name : {post.user_id}")

                    m_hist = (await self.merge_history_repo.select(id = post.merge_history_id))[0]
                    self.logger.info(f"view post merge history id : {m_hist.categories_name}")

                    result.append(
                        Post(
                            post_id = post.id,
                            title = post.title,
                            body = post.body,
                            user_nickname = user.nickname,
                            merge_history_name = m_hist.categories_name,
                            uploaded_at = post.create_at
                        )
                    )

            return ResponsePostList(posts=result)
        except Exception as e:
            self.logger.error(e)
            return ResponsePostList(posts=[])


    #   글 디테일
    async def view_post_detail(self, post_id):
        try:
            self.logger.info(f"view post detail: {post_id}")

            comments = []
            result = (await self.post_repo.select(id = post_id))[0]
            comment_selected = await self.comment_repo.select(post_id = post_id, order = 'create_at')

            for i in comment_selected:
                nick_name = (await self.user_repo.select(id = i.user_id))[0].nickname
                comments.append(
                    Comment(
                        user_id = i.user_id,
                        user_nickname = nick_name,
                        create_at=i.create_at,
                        body=i.body,
                    )
                )

            return ResponsePostDetail(
                title=result.title,
                body=result.body,
                comments=comments,
                create_at=result.create_at,
                user_id=result.user_id,
                user_nickname=(await self.user_repo.select(id = result.user_id))[0].nickname
            )
        except Exception as e:
            self.logger.error(e)


    #   글 삭제
    async def delete_post(self, user_id: str, dto: RequestDeletePost):
        try:
            self.logger.info(f"delete post: {user_id}")
            if await self.user_repo.select(id=user_id):
                await self.post_repo.delete(post_id = dto.post_id)

            return "success"
        except Exception as e:
            self.logger.error(e)


    #   댓글 작성
    async def write_comment(self, user_id, dto):
        try:
            self.logger.info(f"write comment: {user_id}")

            comment = CommentEntity(
                user_id=user_id,
                body=dto.body,
                create_at=datetime.now(),
                post_id=dto.post_id,
            )

            await self.comment_repo.insert(comment)

            return "success"

        except Exception as e:
            self.logger.error(e)


    #   댓글 삭제
    async def delete_comment(self, user_id: str, dto: RequestDeleteComment):
        try:
            self.logger.info(f"delete comment: {user_id}")
            if await self.user_repo.select(id=user_id):
                await self.comment_repo.delete(post_id = dto.post_id, comment_id = dto.comment_id)
            return "success"

        except Exception as e:
            self.logger.error(e)