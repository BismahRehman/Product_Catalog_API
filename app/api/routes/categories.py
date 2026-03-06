from typing import List
from fastapi.encoders import jsonable_encoder
from app.api.cache import get_cache, set_cache, delete_cache
from app.schemas.category import CategorySchema, CategoriesResponse
from app.curd.category import create_category, update_category, delete_category, get_categories, list_categories, \
    product_categories
from app.api.deps import get_db, get_current_user
from fastapi.params import Depends
from fastapi import APIRouter
from app.schemas.product import ProductResponse

router = APIRouter(prefix= "/category",tags=["categories"])

@router.post("/categories",response_model=CategoriesResponse)
async def add_categories_root(category_data:CategorySchema ,db=Depends(get_db),current_user: str = Depends(get_current_user)):
   category = create_category(category_data,db)
   await delete_cache("categories:list")
   return category

@router.put("/categories/{category_id}",response_model=CategoriesResponse)
async def update_categories_root(category_id:int,category_data:CategorySchema , db=Depends(get_db),current_user: str = Depends(get_current_user)):
   category = update_category(category_data,category_id,db)
   await delete_cache("categories:list")
   await delete_cache(f"categories:{category_id}")
   await delete_cache(f"categories:{category_id}:products")
   return category

@router.get("/categories",response_model=List[CategoriesResponse])
async def all_categories(db=Depends(get_db)):
    cache_key = "categories:list"
    cached = await get_cache(cache_key)
    if cached:
        return cached
    categories = list_categories(db)
    categories_data = jsonable_encoder([CategoriesResponse.from_orm(c) for c in categories])
    await set_cache(cache_key,categories_data, expire=60)
    return categories_data

@router.get("/categories/{category_id}",response_model=CategoriesResponse)
async def categories_by_id(category_id:int,db=Depends(get_db)):
    cache_key = f"categories:{category_id}"
    cached = await get_cache(cache_key)
    if cached:
        return cached
    category =  get_categories(category_id,db)
    category_data = jsonable_encoder(CategoriesResponse.from_orm(category))
    await set_cache(cache_key, category_data, expire=60)
    return  category_data


@router.delete("/categories/{category_id}",response_model=CategoriesResponse)
async def delete_categories_root(category_id:int,db=Depends(get_db),current_user: str = Depends(get_current_user)):
    category = delete_category(category_id,db)
    await delete_cache("categories:list")
    await delete_cache(f"categories:{category_id}")
    await delete_cache(f"categories:{category_id}:products")
    return category


@router.get("/categories/{category_id}/products",response_model=List[ProductResponse])
async def product(category_id:int,db=Depends(get_db)):
    cache_key = f"categories:{category_id}:products"
    cached = await get_cache(cache_key)
    if cached:
        return cached
    products=product_categories(category_id, db)
    products_data = [ProductResponse.from_orm(product) for product in products]
    category_data = jsonable_encoder(products_data)
    await set_cache(cache_key, category_data, expire=60)

    return category_data

