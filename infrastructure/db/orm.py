from uuid import uuid4

from sqlalchemy.orm import registry
import sqlalchemy as sa

from domain.entities import User

mapper_registry = registry()

user_table = sa.Table(
    "user",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, default=uuid4()),
    sa.Column("email", sa.String, unique=True, nullable=False),
    sa.Column("password_hash", sa.String, nullable=False),
    sa.Column("first_name", sa.String),
    sa.Column("last_name", sa.String),
    sa.Column("is_active", sa.Boolean, default=True)
)


def start_mapping():
    mapper_registry.map_imperatively(User, user_table)
