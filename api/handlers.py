from uuid import UUID
from http import client

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api import schemas
from db.session import get_db
from services.user import UserService
from services.exceptions import ResourceAlreadyExists, ResourceNotFound

user_router = APIRouter()


@user_router.post("/signup")
async def create_user(
        user: schemas.CreateUserRequest, db: AsyncSession = Depends(get_db)
) -> schemas.CreateUserResponse:
    try:
        return await UserService.create_user(user, db)
    except ResourceAlreadyExists:
        raise HTTPException(
            status_code=client.CONFLICT,
            detail="User with such email already exists"
        )


@user_router.get("/{user_id}")
async def get_user(
        user_id: UUID, db: AsyncSession = Depends(get_db)
) -> schemas.GetUserResponse:
    try:
        return await UserService.get_user(user_id, db)
    except ResourceNotFound:
        raise HTTPException(status_code=client.NOT_FOUND,
                            detail="User doesn't exists")


@user_router.delete("/{user_id}")
async def delete_user(
        user_id: UUID, db: AsyncSession = Depends(get_db)
) -> schemas.DeleteUserResponse:
    try:
        return await UserService.delete_user(user_id, db)
    except ResourceNotFound:
        raise HTTPException(status_code=client.NOT_FOUND,
                            detail="User doesn't exists")
