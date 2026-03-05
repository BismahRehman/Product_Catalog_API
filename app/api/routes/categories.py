from typing import List

from app.schemas.category import CategorySchema, CategoriesResponse
from app.curd.category import create_category, update_category, delete_category, get_categories, list_categories, \
    product_categories
from app.api.deps import get_db
from fastapi.params import Depends
from fastapi import APIRouter, HTTPException
from app.models.category import Category
from app.schemas.product import ProductResponse

router = APIRouter(prefix= "/category",tags=["categories"])


@router.post("/categories",response_model=CategoriesResponse)
def add_categories(category_data:CategorySchema ,db=Depends(get_db)):
   category = create_category(category_data,db)
   return category


@router.put("/categories/{category_id}",response_model=CategoriesResponse)
def update_categories(category_id:int,category_data:CategorySchema , db=Depends(get_db)):
   category = update_category(category_data,category_id,db)
   return category


@router.get("/categories",response_model=List[CategoriesResponse])
def categories(db=Depends(get_db)):
    categories= list_categories(db)
    return categories


@router.get("/categories/{category_id}",response_model=CategoriesResponse)
def categories_by_id(category_id:int,db=Depends(get_db)):
    category =  get_categories(category_id,db)
    return category


@router.delete("/categories/{category_id}",response_model=CategoriesResponse)
def delete_categories(category_id:int,db=Depends(get_db)):
    category = delete_category(category_id,db)
    return category


@router.get("/categories/{category_id}/products",response_model=List[CategoriesResponse])
def products(category_id:int,db=Depends(get_db)):
    products=product_categories(category_id, db)
    return products

