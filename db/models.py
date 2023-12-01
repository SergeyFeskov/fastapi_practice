import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from uuid import uuid4


BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = "user"

    id = sa.Column(sa.UUID(as_uuid=True), primary_key=True, default=uuid4())
    email = sa.Column(sa.String, unique=True, nullable=False)
    password_hash = sa.Column(sa.String, nullable=False)

    first_name = sa.Column(sa.String)
    last_name = sa.Column(sa.String)
    is_active = sa.Column(sa.Boolean, default=True)
