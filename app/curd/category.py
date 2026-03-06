from fastapi import HTTPException

from app.models.category import Category

def create_category(category_data,db):
    existing_category = db.query(Category).filter_by(name=category_data.name).first()
    if existing_category:
        raise HTTPException(status_code=400, detail="Category already exists")

    category = Category(name=category_data.name, description=category_data.description)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def update_category(category_id,category_data ,db):
    existing_category = db.query(Category).filter_by(id=category_id).first()
    if not existing_category:
        raise HTTPException(status_code=400, detail="Category does not exist")

    existing_category.name = category_data.name
    existing_category.description = category_data.description
    db.add(existing_category)
    db.commit()
    db.refresh(existing_category)
    return existing_category


def delete_category(category_id,db):
    existing_category = db.query(Category).filter_by(id=category_id).first()
    if not existing_category:
        raise HTTPException(status_code=400, detail="Category does not exist")

    db.delete(existing_category)
    db.commit()
    return existing_category


def list_categories(db):
    categories = db.query(Category).all()
    return categories


def get_categories(category_id,db):
    category = db.query(Category).filter_by(id=category_id).first()
    if not category:
        raise HTTPException(status_code=400, detail="Category does not exist")
    return category

def product_categories(category_id,db):
    existing_category = db.query(Category).filter_by(id=category_id).first()
    if not existing_category:
        raise HTTPException(status_code=400, detail="Category does not exist")

    return existing_category.products