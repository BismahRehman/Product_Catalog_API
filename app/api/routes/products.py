from typing import List

from fastapi import APIRouter, HTTPException

from app.api.deps import get_db
from fastapi.params import Depends
from app.curd.product import create_product,update_product,delete_product,get_product,list_products
from app.schemas.product import ProductSchema, ProductResponse
from app.models.product import Product

router = APIRouter(prefix="/products",tags=["products"])

@router.post("/product", response_model=ProductResponse)
def create_product(product: ProductSchema, db = Depends(get_db)):
    product=create_product(product,db)
    return product


@router.put("/products{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductSchema, db = Depends(get_db)):
    product=update_product(product_id,product,db)
    return product



@router.get("/products", response_model=List[ProductResponse])
def get_products(db = Depends(get_db)):
    products=get_products(db)
    return products


@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int , db= Depends(get_db) ):
    product=get_product(product_id,db)
    return product



@router.delete("/products/{product_id}",response_model=ProductResponse)
def delete_product(product_id: int, db = Depends(get_db)):
    product=delete_product(product_id,db)
    return product
