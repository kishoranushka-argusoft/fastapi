from blog import schemas
from .. import database, models
from typing import Annotated
from fastapi import  HTTPException, Query
from sqlmodel import select

def get_all_heroes(session: database.SessionDep,
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


def get_hero_by_id(hero_id: int, session: database.SessionDep):
    hero = session.get(models.Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

def update_hero(hero_id: int, hero: models.HeroUpdate, session: database.SessionDep):
    hero_db = session.get(models.Hero, hero_id)
    if not hero_db:
        raise HTTPException(status_code=404, detail="Hero not found")
    hero_data = hero.model_dump(exclude_unset=True)
    hero_db.sqlmodel_update(hero_data)
    session.add(hero_db)
    session.commit()
    session.refresh(hero_db)
    return hero_db

def delete_hero(hero_id: int, session: database.SessionDep):
    hero = session.get(models.Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}