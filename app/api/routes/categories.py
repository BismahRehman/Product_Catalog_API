from typing import List

from fastapi_cache.decorator import cache

from app.schemas.category import CategorySchema, CategoriesResponse
from app.curd.category import create_category, update_category, delete_category, get_categories, list_categories, \
    product_categories
from app.api.deps import get_db, get_current_user
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from app.models.category import Category
from app.schemas.product import ProductResponse

router = APIRouter(prefix= "/category",tags=["categories"])


@router.post("/categories",response_model=CategoriesResponse)
def add_categories(category_data:CategorySchema ,db=Depends(get_db),current_user: str = Depends(get_current_user)):
   category = create_category(category_data,db)
   return category


@router.put("/categories/{category_id}",response_model=CategoriesResponse)
def update_categories(category_id:int,category_data:CategorySchema , db=Depends(get_db),current_user: str = Depends(get_current_user)):
   category = update_category(category_data,category_id,db)
   return category


@router.get("/categories",response_model=List[CategoriesResponse])
@cache(expire=20)
def categories(db=Depends(get_db)):
    categories= list_categories(db)
    return categories


@router.get("/categories/{category_id}",response_model=CategoriesResponse)
@cache(expire=600)
def categories_by_id(category_id:int,db=Depends(get_db)):
    category =  get_categories(category_id,db)
    return category


@router.delete("/categories/{category_id}",response_model=CategoriesResponse)
def delete_categories(category_id:int,db=Depends(get_db),current_user: str = Depends(get_current_user)):
    category = delete_category(category_id,db)
    return category


@router.get("/categories/{category_id}/products",response_model=List[CategoriesResponse])
@cache(expire=600)
def products(category_id:int,db=Depends(get_db)):
    products=product_categories(category_id, db)
    return products

