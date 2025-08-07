from fastapi import APIRouter
from .. import schemas, database, models, hashing
from fastapi import  HTTPException, status, Depends
from datetime import timedelta
from .. import token
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=['Authentication'])

@router.post("/login")
def login(req: Annotated[OAuth2PasswordRequestForm, Depends()], session: database.SessionDep):
    user = session.query(models.User).filter(models.User.email == req.username).first()
    print("🐍🐍🐍 File: routers/authentication.py | Line: 13 | logig ~ user",user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials!")
    
    if not hashing.verify_password(req.password , user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password!")
    
    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token":access_token, "token_type":"bearer"}