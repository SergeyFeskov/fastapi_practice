from typing import Optional
from uuid import UUID
from dataclasses import dataclass

from .base_entity import BaseEntity


@dataclass
class User(BaseEntity):
    email: str
    password_hash: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    id: Optional[UUID] = None
    is_active: bool = True
