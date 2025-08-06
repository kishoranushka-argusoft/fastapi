from sqlmodel import Field, SQLModel


# class Hero(BaseModel):
#     name: str 
    # age: int 

class Hero(SQLModel):
    name: str = Field(..., min_length=1, nullable=False)
    age: int | None = Field(default=None, index=True)


class Login(SQLModel):
    username: str
    password: str