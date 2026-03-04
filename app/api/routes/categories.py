from fastapi import APIRouter
from app.schemas.category import Category
from app.curd.category import create_category, update_category, delete_category,get_categories,list_categories
from app.api.deps import get_db
from fastapi.params import Depends

router = APIRouter(prefix= "/categories",tags=["categories"])

@router.get("/categories")
def categories():
    categories = list_categories()


    return

@router.get("/categories/{category_id}")
def categories_by_id(category_id:int):
    category= get_categories(category_id)
    return {"message":"You get one categories"}


@router.post("/categories")
def add_categories(category_data:Category ,db=Depends(get_db)):
    category = create_category(category_data)
    return {"message":"You can add categories"}

@router.put("/categories/{category_id}")
def update_categories(category_id:int,category_data:Category ):
    category = update_category(category_id, category_data)
    return {"message":"You can update categories"}

@router.delete("/categories/{category_id}")
def delete_categories(category_id:int):
    category= delete_category(category_id)
    return {"message":"You can delete categories"}