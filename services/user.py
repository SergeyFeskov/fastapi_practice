from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas import CreateUserRequest
from domain.entities import User
from services.crypto import hash_password
from services.exceptions import ResourceAlreadyExists, ResourceNotFound
from infrastructure.db.repositories import UserSQLARepository


class UserService:
    @staticmethod
    async def create_user(
            user_scheme: CreateUserRequest, session: AsyncSession
    ) -> User:
        async with session.begin():
            user_repo = UserSQLARepository(session)
            user = await user_repo.get_by_email(user_scheme.email)
            if user is not None:
                raise ResourceAlreadyExists(
                    "User with such email already exists"
                )
            password_hash = hash_password(user_scheme.password)
            user_entity = User(
                **user_scheme.model_dump(exclude="password"),
                password_hash=password_hash)
            return await user_repo.add(user_entity)

    @staticmethod
    async def get_user(user_id: UUID, session: AsyncSession) -> User:
        async with session.begin():
            user_repo = UserSQLARepository(session)
            user = await user_repo.get_by_id(user_id)
            if user is None:
                raise ResourceNotFound()
            return user

    @staticmethod
    async def delete_user(user_id: UUID, session: AsyncSession) -> User:
        async with session.begin():
            user_repo = UserSQLARepository(session)
            user = await user_repo.get_by_id(user_id)
            if user is None:
                raise ResourceNotFound()
            user.is_active = False
            await user_repo.update(user)
            return user
