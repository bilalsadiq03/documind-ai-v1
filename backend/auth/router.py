from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database import SessionLocal

from auth.schemas import (
    RegisterRequest,
    UserResponse,
)

from auth.service import create_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.post(
    "/register",
    response_model=UserResponse,
)
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    try:
        return create_user(
            db=db,
            name=request.name,
            email=request.email,
            password=request.password
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
