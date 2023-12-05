from typing import Type, Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa
from sqlalchemy import Select
from domain.repositories.base_repo import RepositoryBase, EN_T
from domain.types import ID_T


class SQLARepositoryBase(RepositoryBase[EN_T]):
    """Generic SQLAlchemy 2 (async) Repository."""
    __slots__ = ("_session", "_model_cls")

    def __init__(self, session: AsyncSession, entity_cls: Type[EN_T]) -> None:
        """Creates a new repository instance.

        Args:
            session (AsyncSession): SQLAlchemy async session.
            entity_cls (Type[EN_T]): domain entity class type.
        """
        self._session = session
        self._model_cls = entity_cls

    def _construct_get_query(self, entity_id: ID_T) -> Select:
        """Creates a SELECT query for retrieving a single record.

        Args:
            entity_id (Type[EN_T.id]):  Entity id.

        Returns:
            Select: SELECT query.
        """
        query = sa.select(self._model_cls).filter_by(id=entity_id)
        return query

    async def get_by_id(self, entity_id: ID_T) -> Optional[EN_T]:
        query = self._construct_get_query(entity_id)
        return await self._session.scalar(query)

    def _construct_list_query(self, **filters) -> Select:
        """Creates a SELECT query for retrieving a multiple records.

        Raises:
            ValueError: Invalid column name.

        Returns:
            Select: SELECT query.
        """
        for c, v in filters.items():
            if not hasattr(self._model_cls, c):
                raise ValueError(f"Invalid column name {c}")

        query = sa.select(self._model_cls).filter_by(**filters)
        return query

    async def list(self, **filters) -> Sequence[EN_T]:
        query = self._construct_list_query(**filters)
        return (await self._session.scalars(query)).all()

    async def add(self, entity: EN_T) -> EN_T:
        self._session.add(entity)
        await self._session.flush()
        await self._session.refresh(entity)
        return entity

    async def update(self, entity: EN_T) -> EN_T:
        self._session.add(entity)
        await self._session.flush()
        await self._session.refresh(entity)
        return entity

    async def delete(self, entity_id: ID_T) -> None:
        entity = await self.get_by_id(entity_id)
        if entity is not None:
            await self._session.delete(entity)
            await self._session.flush()
