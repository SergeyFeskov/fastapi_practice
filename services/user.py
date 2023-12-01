from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas import CreateUserRequest
from db.dal import UserDAO
from db.models import User
from services.crypto import hash_password
from services.exceptions import ResourceAlreadyExists, ResourceNotFound


class UserService:
    @staticmethod
    async def create_user(
        user_scheme: CreateUserRequest, session: AsyncSession
    ) -> User:
        async with session.begin():
            user_dao = UserDAO(session)
            user = await user_dao.get_user_by_email(user_scheme.email)
            if user is not None:
                raise ResourceAlreadyExists(
                    "User with such email already exists"
                )
            password_hash = hash_password(user_scheme.password)
            user = await user_dao.create_user(
                first_name=user_scheme.first_name,
                last_name=user_scheme.last_name,
                email=user_scheme.email,
                password_hash=password_hash,
            )
        return user

    @staticmethod
    async def get_user(user_id: UUID, session: AsyncSession) -> User:
        async with session.begin():
            user_dao = UserDAO(session)
            user = await user_dao.get_user_by_id(user_id)
            if user is None:
                raise ResourceNotFound()
            return user

    @staticmethod
    async def delete_user(user_id: UUID, session: AsyncSession) -> User:
        async with session.begin():
            user_dao = UserDAO(session)
            user = await user_dao.get_user_by_id(user_id)
            if user is None:
                raise ResourceNotFound()
            await user_dao.deactivate_user(user)
            return user
