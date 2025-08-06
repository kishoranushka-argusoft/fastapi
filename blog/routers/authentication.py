from fastapi import APIRouter
from .. import schemas, database, models, hashing
from fastapi import FastAPI, Depends, HTTPException, status


router = APIRouter(tags=['Authentication'])

@router.post("/login")
def login(session: database.SessionDep,user_login=schemas.Login):
    user = session.query(models.User).filter(models.User.name == user_login).first()
    if not user or not hashing.verify_password(user_login.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"}, 
        )
    return {"message": "Login successful"}