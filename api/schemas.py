from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CustomBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class UserBase(CustomBase):
    pass


class UserGet(UserBase):
    id: UUID
    email: str
    first_name: Optional[str]
    last_name: Optional[str]


class CreateUserRequest(UserBase):
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class CreateUserResponse(UserGet):
    pass


class GetUserResponse(UserGet):
    pass


class DeleteUserResponse(UserBase):
    id: UUID
