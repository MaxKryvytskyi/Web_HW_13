import redis
import json
import uvicorn
from fastapi import FastAPI
from time import time

app = FastAPI()
# Connecting to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

database = {
    "10": 10,
    "11": 11,
    "12": 12
}


@app.get("/user/{email}")
def read_user(email: int):
    start = time()
    user = r.get(str(email))
    if user is None:
        user = fetch_user_from_db(email)
        r.set(str(email), json.dumps(user))
        r.expire(str(email), 3600)
        end = time()
        print(end - start)
        return user
    end = time()
    print(end - start)
    return json.loads(user)


def fetch_user_from_db(email: int):
    data = database.get(str(email), None)
    print(data)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


    