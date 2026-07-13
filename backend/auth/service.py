from sqlalchemy.orm import Session

from models import User
from auth.security import hash_password
from auth.security import verify_password
from auth.jwt import create_access_token


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

def login_user(db: Session, email: str, password: str):
    user = (
        db.query(User).filter(User.email == email).first()
    )

    if not user:
        raise ValueError("Invalid Credentials.")
    
    if not verify_password(password, user.password):
        raise ValueError("Invalid Password.")

    token = create_access_token({
        "sub": user.id
    })

    return {
        "access_token": token,
        "token_type": "bearer",
    }