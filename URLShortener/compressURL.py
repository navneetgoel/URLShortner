import redis
import base64
import hashlib
from . import config
import sys

class compressURL:
    def __init__(self):
        self.redis = redis.StrictRedis(host=config.REDIS_HOST,port=config.REDIS_PORT,db=config.REDIS_DB)

    def shrinkURL(self, url):
        print(url)
        m = hashlib.md5(str(url).encode('utf-8'))
        m.digest()[-4:]
        return m
    
    def Shorten(self, url):
        code = self.shrinkURL(url)

        try:
            self.redis.set(config.REDIS_PREFIX + code,  url)
            return {'success':True, 'url':url, 'code':code, 'shorturl':config.URL_PREFIX + code}
        except:
            return {'success':False}
    
    def lookup(self, code):
        try:
            return self.redis.get(config.REDIS_PREFIX + code)
        except:
            return None