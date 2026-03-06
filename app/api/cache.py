
import json
import redis.asyncio as redis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

redis_client = None


async def init_cache():
    global redis_client

    redis_client = redis.from_url(
        "redis://localhost:6379",
        encoding="utf8",
        decode_responses=True
    )
    FastAPICache.init(
        RedisBackend(redis_client),
        prefix="fastapi-cache"
    )


async def get_cache(key: str):
    data = await redis_client.get(key)
    if data:
        return json.loads(data)
    return None

async def set_cache(key: str, value, expire: int = 60):
    await redis_client.set(key, json.dumps(value), ex=expire)

async def delete_cache(key: str):
    await redis_client.delete(key)