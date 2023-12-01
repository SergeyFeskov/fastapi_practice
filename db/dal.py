from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa

from db.models import User


class UserDAO:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(
        self, first_name: str, last_name: str, email: str, password_hash: str
    ) -> User:
        new_user = User(
            email=email,
            password_hash=password_hash,
            first_name=first_name,
            last_name=last_name,
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user

    async def get_user_by_id(self, user_id: UUID) -> User | None:
        query = sa.select(User).where(User.id == user_id)
        user = await self.db_session.scalar(query)
        return user

    async def get_user_by_email(self, email: str) -> User | None:
        query = sa.select(User).filter_by(email=email)
        user = await self.db_session.scalar(query)
        return user

    async def deactivate_user(self, user: User):
        user.is_active = False
        self.db_session.add(user)
        await self.db_session.flush()
