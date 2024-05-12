#!/bin/python3

import sys
import requests
import json
import argparse

def Help():
    parser = argparse.ArgumentParser(
        prog = "shodan",
        description = "Script process a shdoan api adnd api responses a lists of open ports",
    )

    parser.add_argument("APIkey")
    parser.add_argument("ip")
    args=parser.parse_args()

def APIcall(APIkey, ip) -> dict:
    try:
        url = f"https://api.shodan.io/shodan/host/{ip}?key={APIkey}"
        return json.loads(requests.get(url).text)
    except:
        sys.exit(-1)

def ActivePorts(APIkey, ip):
    try:
        ports = APIcall(APIkey, ip)["ports"]

        print(f"{ip} active ports:")
        for i in ports:
            print(i)
    except:
        sys.exit(-1)
    

if __name__ == "__main__":
    
    APIkey = sys.argv[1]
    ip = sys.argv[2]
    ActivePorts(APIkey, ip)