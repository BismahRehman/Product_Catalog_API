from datetime import datetime

from pydantic import  Field
from pydantic_settings import BaseSettings
from typing import Optional,Annotated


class ProductSchema(BaseSettings):
    name: Annotated[str, Field(... ,description="Enter Product name" ,min_length=5,max_length=20 )]
    description: Annotated[Optional[str], Field(default=None, description= "Enter Product Description" ,min_length=20, max_length=100)]
    category_id: Annotated[ int , Field(... , description= "Enter Product Category id ")]
    price: Annotated[float , Field(... , description= "Enter Product Price")]

    class Config:
        from_attributes = True



class ProductResponse(BaseSettings):
    id: int
    name: str
    description: Optional[str]
    category_id: int
    price: float
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


