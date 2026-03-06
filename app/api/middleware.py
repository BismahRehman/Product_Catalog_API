import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class ResponseTimeMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        start_time = time.time()

        print("Middleware executed")

        response = await call_next(request)

        process_time = time.time() - start_time

        print(f"Request: {request.url} | Time: {process_time}")

        response.headers["X-Process-Time"] = str(process_time)

        return response