from fastapi import APIRouter

router = APIRouter(prefix= "/categories")

@router.get("/categories")
def categories():
    return {"message":"You get all categories"}

@router.get("/categories/{category_id}")
def categories_by_id():
    return {"message":"You get one categories"}


@router.post("/categories")
def add_categories():
    return {"message":"You can add categories"}

@router.put("/categories/{category_id}")
def update_categories():
    return {"message":"You can update categories"}

@router.delete("/categories/{category_id}")
def delete_categories():
    return {"message":"You can delete categories"}