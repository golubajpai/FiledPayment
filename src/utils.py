import enum
from requests.exceptions import ConnectionError
import requests
import os 
import sys



def connection_check(f):
    def wrapper(*args):
        try:
            response=requests.post(url=os.environ.get("base_url")+"payment/")

        except ConnectionError:
            
            sys.exit("-----server is not up, please run the server first------")
        return f(*args)
    return wrapper



