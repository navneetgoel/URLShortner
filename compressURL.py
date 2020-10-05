import redis
import base64
import hashlib
# import config
import sys

class compressURL:
    def __init__(self):
        # self.redis = redis.StrictRedis(host=config.REDIS_HOST,port=config.REDIS_PORT,db=config.REDIS_DB)
        pass

    def shrinkURL(self, url):
        print(url)
        m = hashlib.md5()
        m.update(url)
        m.digest
        print(m)
        # print(md5.new(URL).digest())
        # return base64.b64encode(md5.new(url).digest()[-4:]).replace('=','').replace('/','_')



def main():
    obj = compressURL()
    print("Hello")
    print(obj.shrinkURL("http://www.google.com"))

if __name__ == "__main__":
    main()