from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, Type, Sequence

from domain.entities import BaseEntity
from domain.types import ID_T

EN_T = TypeVar("EN_T", bound=BaseEntity)


class RepositoryBase(Generic[EN_T], ABC):
    @abstractmethod
    def get_by_id(self, entity_id: ID_T) -> Optional[EN_T]:
        raise NotImplementedError()

    @abstractmethod
    def list(self, **filters) -> Sequence[EN_T]:
        raise NotImplementedError()

    @abstractmethod
    def add(self, entity: EN_T) -> EN_T:
        raise NotImplementedError()

    @abstractmethod
    def update(self, entity: EN_T) -> EN_T:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, entity_id: ID_T) -> None:
        raise NotImplementedError()
