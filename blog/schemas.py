from sqlmodel import Field, SQLModel


# class Hero(BaseModel):
#     name: str 
    # age: int 

class Hero(SQLModel):
    name: str = Field(..., min_length=1, nullable=False)
    age: int | None = Field(default=None, index=True)


class Login(SQLModel):
    email: str
    password: str


class Token(SQLModel):
    access_token: str
    token_type: str


class TokenData(SQLModel):
    email: str | None = None