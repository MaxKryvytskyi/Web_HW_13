from fastapi import Depends
from sqlalchemy import select, or_
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import User
from src.schemas.user import UserSchema


async def get_user_by_email(email: str, db: Session = Depends(get_db)):
    stmt = select(User).filter_by(email=email)
    user = db.execute(stmt)
    user = user.scalar_one_or_none()
    return user

async def get_user_by_username(username: str, db: Session = Depends(get_db)):
    stmt = select(User).filter_by(username=username)
    user = db.execute(stmt)
    user = user.scalar_one_or_none()
    return user


async def create_user(body: UserSchema, db: Session = Depends(get_db)):
    new_user = User(**body.model_dump())
    new_user.avatar = "https://www.rpnation.com/gallery/250-x-250-placeholder.30091/full?d=1504582354"
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_token(user: User, token: str | None, db: Session):
    user.refresh_token = token
    db.commit()

async def confirmed_email(email: str, db: Session) -> None:
    user = await get_user_by_email(email, db)
    user.confirmed = True
    db.commit()

async def update_avatar(email, url: str, db: Session) -> User:
    user = await get_user_by_email(email, db)
    user.avatar = url
    db.commit()
    return user
