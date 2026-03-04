from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.api.deps import get_db
from fastapi.params import Depends
from app.curd.product import create_product,update_product,delete_product,get_product,list_products
from app.schemas.product import Product


router = APIRouter(prefix="/categories",tags=["products"])

@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    products=list_products(db)
    return {"message":"You can get products"}

@router.get("/products/{product_id}")
def get_product_by_id(product_id: int , db: Session = Depends(get_db) ):
    product= get_product_by_id(product_id,db)
    return {"message":"You can get products"}

@router.post("/products")
def create_product(product: Product, db: Session = Depends(get_db)):
    product=create_product(product,db)
    return {"message":"You can create products"}


@router.put("/products{product_id}")
def update_product(product_id:int,product: Product, db: Session = Depends(get_db)):
    product=update_product(product_id,product,db)
    return {"message":"You can update products"}

@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product=delete_product(product_id,db)
    return {"message":"You can delete products"}