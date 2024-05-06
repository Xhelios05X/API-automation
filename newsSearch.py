#!/bin/python3

import sys
import requests
import json

def APIcall(APIkey:str, keyword:str):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={APIkey}"
    print(json.loads(requests.get(url).text))

# sys.argv[1] - API key
# sys.argv[2] - keyword of news
if __name__ == "__main__":
    APIkey = sys.argv[1]
    keyword = sys.argv[2]
    APIcall(APIkey, keyword)