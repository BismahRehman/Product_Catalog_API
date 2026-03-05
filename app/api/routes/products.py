from typing import List

from fastapi import APIRouter

from app.api.deps import get_db, get_current_user
from fastapi.params import Depends
from app.curd.product import create_product,update_product,delete_product,get_product,list_products
from app.schemas.product import ProductSchema, ProductResponse


router = APIRouter(prefix="/products",tags=["products"])

@router.post("/product", response_model=ProductResponse)
def create_product(product: ProductSchema, db = Depends(get_db),current_user: str = Depends(get_current_user)):
    product=create_product(product,db)
    return product


@router.put("/products{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductSchema, db = Depends(get_db),current_user: str = Depends(get_current_user)):
    product=update_product(product_id,product,db)
    return product



@router.get("/products", response_model=List[ProductResponse])
def get_products(db = Depends(get_db)):
    products=list_products(db)
    return products


@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int , db= Depends(get_db) ):
    product=get_product(product_id,db)
    return product



@router.delete("/products/{product_id}",response_model=ProductResponse)
def delete_product(product_id: int, db = Depends(get_db),current_user: str = Depends(get_current_user)):
    product=delete_product(product_id,db)
    return product
