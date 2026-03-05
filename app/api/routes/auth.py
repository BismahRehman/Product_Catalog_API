from fastapi import APIRouter
from fastapi.params import Depends

from app.api.deps import get_db,get_current_user
from app.schemas.user import UserRegister, UserResponse, UserLogin
from app.curd.user import create_user,login_user

router = APIRouter(prefix="/auth",tags=["auth"])


@router.post("/register",response_model=UserResponse)
def register_user(user: UserRegister, db=Depends(get_db)):
    """ Run user registration route """
    user= create_user(user, db)
    return  user


@router.post("/login")
def login(user:UserLogin, db=Depends(get_db)):
     """ Run user login route """
     user1= login_user(user, db)

     return user1


@router.put("/update-profile")
def update_profile(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello {current_user}, you are authenticated"}
