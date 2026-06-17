import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

redis_client = redis.Redis(
    host = REDIS_HOST,
    port = REDIS_PORT,
    decode_responses = True,
)

print("Redis Ping:", redis_client.ping())

QUEUE_NAME = "documind:jobs"


def enqueue_job(job_id: str):
    print(f"Adding job to Redis: {job_id}")

    redis_client.lpush(QUEUE_NAME, job_id)

    print("Job added successfully")
    print("Queue length:", redis_client.llen(QUEUE_NAME))