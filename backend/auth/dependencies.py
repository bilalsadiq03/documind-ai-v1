from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from database import SessionLocal
from models import User

from auth.jwt import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

    
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    user = (
        db.query(User)
        .filter(User.id == payload["sub"])
        .first()
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return user

    