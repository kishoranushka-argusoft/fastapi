from . import database
from fastapi import Depends, FastAPI
from sqlmodel import SQLModel
from .routers import user, hero, authentication

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users.",
    },
    {
        "name": "heroes",
        "description": "Manage Heores. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://anushkakishor.tech/",
        },
    },
]


app = FastAPI(openapi_tags=tags_metadata)
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(hero.router)



def create_db_and_tables():
    SQLModel.metadata.create_all(database.engine)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()









