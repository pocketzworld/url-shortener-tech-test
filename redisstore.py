# stores in Redis
import redis

class RedisStore:

    store: redis.Redis

    CONST_REDIS_SERVER = 'host.docker.internal'  # localhost or host.docker.internal
    CONST_REDIS_PORT = 6379

    CONST_FIRST_ID = 3844 # 62^2
    CONST_INDEX = "index"

    def __init__(self):
        self.store = redis.Redis(host=self.CONST_REDIS_SERVER, port=self.CONST_REDIS_PORT, db=0, decode_responses=True)
        ix = self.store.get(self.CONST_INDEX)
        if ix == None:
            self.store.set(self.CONST_INDEX, self.CONST_FIRST_ID)

    def insert(self, url) -> int:
        id = self.store.incr(self.CONST_INDEX) # get next id
        self.store.set(id, url)
        return id

    def get(self, id: int) -> str:
        url = self.store.get(id)
        return url


