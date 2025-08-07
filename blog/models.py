from typing import Optional
from sqlmodel import Field, SQLModel, Relationship, ForeignKey
from . import schemas
# from pydantic import BaseModel

class Hero(schemas.Hero, table=True):
    id: int | None = Field(default=None, primary_key=True)
    secret_name: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id") # Foreign key
    user: Optional["User"] = Relationship(back_populates="hero")
    

class HeroPublic(schemas.Hero):
    id: int
    user: Optional["User"]


class HeroCreate(schemas.Hero):
    secret_name: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")


class HeroUpdate(schemas.Hero):
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None



class User(schemas.Hero, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(min_length=1, default=None, unique=True)
    password: str = Field(min_length=1)
    hero: list[Hero] = Relationship(back_populates="user") # Relationship attribute

class UserPublic(schemas.Hero):
    id: int
    email: str 
    hero: list[Hero]


class UserCreate(schemas.Hero):
    email: str 
    password: str
    

