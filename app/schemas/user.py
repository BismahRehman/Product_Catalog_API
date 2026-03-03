from datetime import datetime

from fastapi import HTTPException
from pydantic import Field, EmailStr, field_validator
from pydantic_settings import BaseSettings
from typing import  Annotated



class UserRegister(BaseSettings):
    username: Annotated[str , Field(... , description= "Enter Username",)]
    email: Annotated[ EmailStr ,Field(... , description= "Enter Email")]
    password: Annotated[ str , Field( ... , description= "Enter password", min_length=8, max_length=15)]

    class Config:
        from_attributes = True


class UserLogin(BaseSettings):
    username: Annotated[str , Field(... , description= "Enter Username",)]
    email:  Annotated[ EmailStr ,Field(... , description= "Enter Email")]
    password: Annotated[ str , Field( ... , description= "Enter password", min_length=8, max_length=15)]


    class Config:
        from_attributes = True


class UserResponse(BaseSettings):
    id : int
    username : str
    email : EmailStr
    created_at : datetime
    updated_at : datetime









