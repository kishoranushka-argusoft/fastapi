
from fastapi.routing import APIRouter
from .. import models, database, hashing
from typing import Annotated
from fastapi import  HTTPException, Query
from sqlmodel import select



router = APIRouter(
    prefix= "/users",
    tags=['users'])


@router.post("/", response_model=models.UserPublic, status_code=201, )
def create_user(user: models.UserCreate, session: database.SessionDep):
    # print("------------------------------------",  user)
    hash_pwd = hashing.get_password_hash(user.password)
    user.password = hash_pwd
    # print(user.password)
    # print(hashedPassword)
    db_user = models.User.model_validate(user)
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",db_user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user

@router.get("/", response_model=list[models.UserPublic])
def read_users(
    session: database.SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    users = session.exec(select(models.User).offset(offset).limit(limit)).all()
    return users


@router.get("/{user_id}", response_model=models.UserPublic)
def read_user(user_id: int, session: database.SessionDep):
    user = session.get(models.User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user