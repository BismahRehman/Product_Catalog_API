
from app.models.product import Product
from fastapi import HTTPException

def create_product(product,db):
    existing_product = db.query(Product).filter(Product.name == product.name).first()
    if existing_product:
        raise HTTPException(status_code=400, detail="Product with this name already exists")

    product = Product(name=product.name, description=product.description, category_id=product.category_id,
                      price=product.price)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def update_product(product_id,product,db):
    existing_product = db.query(Product).filter(Product.id == product_id).first()
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")

    # update fields from Pydantic model

    existing_product.name = product.name
    existing_product.price = product.price
    existing_product.category_id = product.category_id
    if product.description:
        existing_product.description = product.description
    db.commit()
    db.refresh(existing_product)
    return existing_product


def delete_product(product_id,db):
    existing_product = db.query(Product).filter(Product.id == product_id).first()
    if not existing_product:
        raise HTTPException(status_code=400, detail="Product with this id does not exist")
    db.delete(existing_product)
    db.commit()
    return existing_product


def list_products(db):
    products = db.query(Product).all()
    return products


def get_product(product_id,db):
    existing_product = db.query(Product).filter(Product.id == product_id).first()
    if not existing_product:
        raise HTTPException(status_code=400, detail="Product with this id does not exist")
    return existing_product