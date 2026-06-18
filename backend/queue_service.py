import redis
import os
import json

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

redis_client = redis.Redis(
    host = REDIS_HOST,
    port = REDIS_PORT,
    decode_responses = True,
)

print("Redis Ping:", redis_client.ping())

QUEUE_NAME = "documind:jobs"


def enqueue_job(job):
    redis_client.lpush(
        QUEUE_NAME,
        json.dumps(job)
    )