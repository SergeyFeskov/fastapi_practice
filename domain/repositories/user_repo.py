from abc import abstractmethod
from typing import Optional
from uuid import UUID

from .base_repo import RepositoryBase
from domain.entities import User


class UserRepositoryBase(RepositoryBase[User]):
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        raise NotImplementedError()
