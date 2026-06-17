import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

QUEUE_NAME = "documind:jobs"

while True:
    item = redis_client.brpop(QUEUE_NAME)

    _, job_id = item

    print(f"Processing Job: {job_id}")