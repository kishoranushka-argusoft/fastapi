from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def home():
    return {'data':{'name':'Home page'}}
    


@app.get('/about')
def about():
    return {'data':{'name':'About page'}}

@app.get('/blog')
def blog(limit=10, published:bool = True, sort:Optional[str] = None):
    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit} blogs from the db'}
    return {'data':'blog page'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}




@app.get('/blog/{id}')
def blog(id :int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data':f'{limit} comments from the list'}


class Blog(BaseModel):
    title: str
    body:str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request:Blog):
    return {'data':f"blog is created with title as {request.title} and"}
