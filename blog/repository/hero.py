from blog import schemas
from .. import database, models
from typing import Annotated
from fastapi import  HTTPException, Query
from sqlmodel import select

def read_heroes(session: database.SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,):
    heroes = session.exec(select(models.Hero).offset(offset).limit(limit)).all()
    print("----------------------------------",heroes)
    return heroes


def create(hero: schemas.Hero, session: database.SessionDep):
    db_hero = models.Hero.model_validate(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero



