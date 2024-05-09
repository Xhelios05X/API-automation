#!/bin/python3

import sys
import requests
import json
import argparse

def Help():
    parser = argparse.ArgumentParser(
        prog = 'newsSearch.py',
        description = '''Script process a news API api response and return lists of articles about typed keyword''',
    )

    parser.add_argument('APIkey')
    parser.add_argument('keyword')
    args=parser.parse_args()

def APIcall(APIkey:str, keyword:str):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={APIkey}"
    return json.loads(requests.get(url).text)

def APIresponseInterpreter(APIkey:str, keyword:str):
    try:
        APIresponse = APIcall(APIkey, keyword)
    
        # if API response isn't ok, then script exit with error code -1
        if APIresponse["status"] != "ok":
            sys.exit(-1)
    
        print(f"lists of articles about {keyword}:\n")
        for iterator in range(len(APIresponse["articles"])):
            print("author: "+str(APIresponse["articles"][iterator]["author"])+"\ntitle: "+APIresponse["articles"][iterator]["title"]+"\nurl: "+APIresponse["articles"][iterator]["url"]+"\n")
    except:
        sys.exit(-1)

# sys.argv[1] - API key
# sys.argv[2] - keyword of news
if __name__ == "__main__":
    Help()

    APIkey = sys.argv[1]
    keyword = sys.argv[2]
    APIresponseInterpreter(APIkey, keyword)