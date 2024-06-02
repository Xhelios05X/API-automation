#!/bin/python3

import sys
import requests
import json
import argparse

# funcion call help of that script in cmd
def Help():
    parser = argparse.ArgumentParser(
        prog = "newsSearch.py",
        description = "Script process a news API api response and return lists of articles about typed keyword",
    )

    parser.add_argument("-f", "--file", action="store_true")
    parser.add_argument("APIkey")
    parser.add_argument("keyword")
    args=parser.parse_args()
    return args

def OutputToFile(APIresponse):
    #   ToDo:
    #   function output file
    pass

# funcion send API request and return an API response as dict
def APIcall(APIkey:str, keyword:str) -> dict:
    try:
        url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={APIkey}"
        return json.loads(requests.get(url).text)
    except:
        # if something goes wrong then script exits with error code -1
        sys.exit(-1)


# function interpets an API response
def APIresponseInterpreter(APIkey:str, keyword:str, isFile = False):
    try:
        APIresponse = APIcall(APIkey, keyword)
    
        # if API response isn't ok, then script exit with error code -1
        if APIresponse["status"] != "ok":
            sys.exit(-1)

        if help.file:
            OutputToFile(APIresponse)
        else:
            # printing a header
            print(f"lists of articles about {keyword}:\n")

            # loop lists an articles
            for iterator in range(len(APIresponse["articles"])):
                print("author: "+str(APIresponse["articles"][iterator]["author"])+
                    "\ntitle: "+APIresponse["articles"][iterator]["title"]+
                    "\nurl: "+APIresponse["articles"][iterator]["url"]+"\n")
    except:
        # if something goes wrong, program exits with error code -1
        sys.exit(-1)

# main function
# sys.argv[1] - API key
# sys.argv[2] - keyword of news
if __name__ == "__main__":
    help = Help()

    APIkey = sys.argv[1]
    keyword = sys.argv[2]
    APIresponseInterpreter(APIkey, keyword, help.)