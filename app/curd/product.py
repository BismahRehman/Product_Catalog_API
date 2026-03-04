
from app.models.product import Product
from fastapi import HTTPException

def create_product(product,db):
    existing_product = db.query(Product).filter(name= product.name).first()
    if existing_product:
        raise HTTPException(status_code=400, detail="Product with this id already exists")

    product = Product(name=product.name,description=product.description,category_id=product.category_id,price=product.price)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def update_product(product_id,product,db):
    existing_product = db.query(Product).filter(name= product.name).first()
    if not existing_product:
        raise HTTPException(status_code=400, detail="Product with this id does not exist")
    if product.name :
        product.name = product.name
    if product.description :
         product.description = product.description
    if product.category_id :
         product.category_id = product.category_id
    if product.price :
           product.price = product.price
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def delete_product(product_id,db):
    existing_product = db.query(Product).filter(id= product_id).first()
    if not existing_product:
        raise HTTPException(status_code=400, detail="Product with this id does not exist")
    db.delete(existing_product)
    db.commit()
    db.refresh(existing_product)
    return existing_product


def list_products(db):
    products = db.query(Product).all()
    return products


def get_product(product_id,db):
    existing_product = db.query(Product).filter(id= product_id).first()
    if not existing_product:
        raise HTTPException(status_code=400, detail="Product with this id does not exist")
    return existing_product
