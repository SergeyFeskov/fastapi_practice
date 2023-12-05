from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa

from .base_repo import SQLARepositoryBase
from domain.entities import User
from domain.repositories import UserRepositoryBase


class UserSQLARepository(SQLARepositoryBase[User], UserRepositoryBase):
    def __init__(self, session: AsyncSession):
        super().__init__(session, User)

    async def get_by_email(self, email: str) -> Optional[User]:
        query = sa.select(User).filter_by(email=email)
        return await self._session.scalar(query)
