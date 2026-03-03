from fastapi import APIRouter

router = APIRouter(prefix="/categories")

@router.get("/products")
def get_products():
    return {"message":"You can get products"}

@router.get("/products/{product_id}")
def get_product_by_id( ):
    return {"message":"You can get products"}

@router.post("/products")
def create_product():
    return {"message":"You can create products"}


@router.put("/products")
def update_product():
    return {"message":"You can update products"}

@router.delete("/products/{product_id}")
def delete_product():
    return {"message":"You can delete products"}