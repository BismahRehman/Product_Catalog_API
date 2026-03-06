from typing import List

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.api.cache import get_cache, set_cache, delete_cache
from app.api.deps import get_db, get_current_user
from fastapi.params import Depends
from app.curd.product import create_product,update_product,delete_product,get_product,list_products
from app.schemas.product import ProductSchema, ProductResponse


router = APIRouter(prefix="/products",tags=["products"])

@router.post("/product", response_model=ProductResponse)
async def  create_product_root(product: ProductSchema, db = Depends(get_db),current_user: str = Depends(get_current_user)):
    product=create_product(product,db)
    # invalidate cache
    await delete_cache("product")
    return product


@router.put("/products/{product_id}", response_model=ProductResponse)
async def update_product_root(product_id: int, product: ProductSchema, db = Depends(get_db),current_user: str = Depends(get_current_user)):
    product=update_product(product_id,product,db)
    await delete_cache("product")
    await delete_cache(f"product:{product_id}")
    return product



@router.get("/products", response_model=List[ProductResponse])
async  def get_products(db = Depends(get_db)):
    cache_key = "product:List"
    cached = await get_cache(cache_key)
    if cached:
        return  cached
    products=list_products(db)
    # Convert all products to dicts
    products_data = jsonable_encoder([ProductResponse.from_orm(p) for p in products])
    await set_cache(cache_key, products_data, expire=60)
    return products_data


@router.get("/products/{product_id}", response_model=ProductResponse)
async def get_product_by_id(product_id: int , db= Depends(get_db) ):
    cache_key = f"product:{product_id}"
    cached = await get_cache(cache_key)

    if cached:
        return  cached
    product=get_product(product_id,db)
    product_data = jsonable_encoder(ProductResponse.from_orm(product))

    await set_cache(cache_key, product_data, expire=60)
    return product_data


@router.delete("/products/{product_id}",response_model=ProductResponse)
async def delete_product_root(product_id: int, db = Depends(get_db),current_user: str = Depends(get_current_user)):
    product=delete_product(product_id,db)
    await delete_cache("product")
    await delete_cache(f"product:{product_id}")

    return product
