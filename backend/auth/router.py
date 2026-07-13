from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from models import User

from sqlalchemy.orm import Session

from database import SessionLocal

from auth.schemas import (
    RegisterRequest,
    UserResponse,
    LoginRequest,
    TokenResponse,
)

from auth.service import create_user, login_user
from auth.dependencies import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

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

@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):

    try:
        return login_user(
            db,
            form_data.username, 
            form_data.password,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )

@router.get(
    "/me",
    response_model=UserResponse
)
def me(

    current_user: User = Depends(
        get_current_user
    )

):

    return current_user