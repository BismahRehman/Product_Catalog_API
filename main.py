from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
from starlette.requests import Request

from app.api.middleware import ResponseTimeMiddleware
from app.api.routes import  auth_router,product_router,category_router
from app.api.cache import init_cache



app = FastAPI(title="my Fast API")


app.add_middleware(ResponseTimeMiddleware)

@app.on_event("startup")
async def startup():
    await init_cache()


app.include_router(auth_router)
app.include_router(product_router)
app.include_router(category_router)

# Catch all Pydantic validation errors for requests
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = [
        {"field": e["loc"][-1], "message": e["msg"]}
        for e in exc.errors()
    ]
    # Raise HTTPException with 400 instead of 422
    raise HTTPException(status_code=400, detail=errors)

@app.get("/")
def welcome():
    return {"message":"welcome to My API"}
