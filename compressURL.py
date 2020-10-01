import redis
import base64
import hashlib
import config
import sys

class compressURL:
    def __init__(self):
        self.redis = redis.StrictRedis(host=config.REDIS_HOST,port=config.REDIS_PORT,db=config.REDIS_DB)