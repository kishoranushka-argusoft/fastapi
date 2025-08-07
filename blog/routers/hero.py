from fastapi import APIRouter, Depends
from blog import schemas
from .. import models, database, oauth2
from fastapi import  HTTPException, Query
from sqlmodel import select
from ..repository import hero
from typing import Annotated
from fastapi import  HTTPException, Query


router = APIRouter(
    prefix="/heroes",
    tags=['heroes'])


@router.post("/", response_model=models.HeroPublic, status_code=201 )
def create_hero(hero_req: models.HeroCreate, session: database.SessionDep, current_user: models.User = Depends(oauth2.get_current_user)):
    print("🐍 File: routers/hero.py | Line: 18 | undefined ~ hero", type(hero))
    return hero.create(hero_req, session)


@router.get("/",response_model=list[models.HeroPublic])
def read_heroes(session:database.SessionDep, offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100, current_user: models.User = Depends(oauth2.get_current_user)):
    return hero.get_all_heroes(session, offset, limit)


@router.get("/{hero_id}", response_model=models.HeroPublic)
def read_hero(hero_id: int, session: database.SessionDep, current_user: models.User = Depends(oauth2.get_current_user)):
    return hero.get_hero_by_id(hero_id, session)


@router.patch("/{hero_id}", response_model=models.HeroPublic, status_code=201,)
def update_hero(hero_id: int, hero_req: models.HeroUpdate, session: database.SessionDep,current_user: models.User = Depends(oauth2.get_current_user)):
    return hero.update_hero(hero_id,hero_req, session)


@router.delete("/{hero_id}")
def delete_hero(hero_id: int, session: database.SessionDep,current_user: models.User = Depends(oauth2.get_current_user)):
    return hero.delete_hero(hero_id, session)