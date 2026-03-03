from datetime import datetime

from pydantic_settings import BaseSettings
from pydantic import  Field
from typing import Optional,Annotated

class Category(BaseSettings):
    name: Annotated[str, Field(... , description="Enter Category Name",  min_length=5, max_length=20)]
    description: Annotated[Optional[str], Field(... , description="Enter Category Description", min_length=20, max_length=50)]
    class Config:
        from_attributes = True

class CategoriesResponse(BaseSettings):
    id: int
    name: str
    description: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
