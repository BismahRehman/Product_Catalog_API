from fastapi import HTTPException
from starlette import status

from app.models.user import User
from app.schemas.user import  UserLogin
from app.curd.auth import create_access_token


from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    return password_context.hash(password)

def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)

def create_user(user, db):
    existing_user = db.query(User).filter_by(username=user.username).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="User already exists")

    existing_email = db.query(User).filter_by(email=user.email).first()
    if existing_email:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="email already exists")

    hashed_password = hash_password(user.password)

    user = User(username=user.username, email=user.email, hash_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    response= db.query(User).filter_by(username=user.username).first()
    return response


# def login_user(user: UserLogin, db, form_data):

def login_user( form_data, db):
     existing_user= db.query(User).filter_by(username=form_data.username).first()

     if not existing_user :
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User not found")

     if not verify_password(form_data.password, existing_user.hash_password):
         raise  HTTPException (status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect password for user ")

     token = create_access_token({"sub": form_data.username})

     return {"access_token": token, "token_type": "bearer"}

def update_user(user: UserLogin, db):

    existing_user = db.query(User).filter_by(username=user.username,email = user.email).first()
    if not existing_user :
        raise  HTTPException (status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid username or password")

    if not verify_password(user.password, existing_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password for user ")

    return user









