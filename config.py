from pydantic import AnyUrl
from pydantic_settings import BaseSettings
from starlette.datastructures import URL


class Settings(BaseSettings):
    DATABASE_URI: str
    SECRET_KEY : str  # Use env variable in production
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    REDIS_URL : str


    class Config:
        env_file = ".env"

settings = Settings()




