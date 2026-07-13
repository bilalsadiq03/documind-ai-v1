from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

from jose import jwt

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
)
def create_access_token(data: dict):
    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update({
        "exp": expire
    })

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )