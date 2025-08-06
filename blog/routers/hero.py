from fastapi import APIRouter

from blog import schemas
from .. import models, database
from fastapi import  HTTPException, Query
from sqlmodel import select
from ..repository import hero
from typing import Annotated
from fastapi import  HTTPException, Query



router = APIRouter(
    prefix="/heroes",
    tags=['heroes'])


@router.post("/", response_model=models.HeroPublic, status_code=201, )
def create_hero(hero: schemas.Hero, session: database.SessionDep):
    print("🐍 File: routers/hero.py | Line: 18 | undefined ~ hero", type(hero))
    return hero.create(hero, session)


@router.get("/", response_model=list[models.HeroPublic])
def read_heroes(
    session: database.SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    print("*****************************")
    hero.read_heroes(session, offset, limit)


@router.get("/{hero_id}", response_model=models.HeroPublic)
def read_hero(hero_id: int, session: database.SessionDep):
    hero = session.get(models.Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@router.patch("/{hero_id}", response_model=models.HeroPublic, status_code=201)
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


@router.delete("/{hero_id}")
def delete_hero(hero_id: int, session: database.SessionDep):
    hero = session.get(models.Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}
