from sqlalchemy.orm import Session

from models import User
from auth.security import hash_password


def create_user(
    db: Session,
    name: str,
    email: str,
    password: str
):

    existing = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if existing:
        raise Exception("Email already registered")

    user = User(
        name=name,
        email=email,
        password=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user