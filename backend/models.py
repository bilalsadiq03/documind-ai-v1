from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text

from database import Base


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
        nullable=False
    )

    readme_path = Column(
        Text,
        nullable=True
    )