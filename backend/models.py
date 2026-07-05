from sqlalchemy import Column, String, DateTime
from sqlalchemy import Text
from sqlalchemy.sql import func

from database import Base

import uuid


class Job(Base):

    __tablename__ = "jobs"

    id = Column(
        String,
        primary_key=True
    )

    repo_url = Column(
        Text,
        nullable=False
    )

    status = Column(
        String,
        nullable=False,
        default="queued"
    )

    readme_path = Column(
        Text,
        nullable=True
    )

class User(Base):
    __tablename__ = "users"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )