#!/bin/python3

import requests
import sys
import json
import argparse

# this funcion call a help of that script
def Help():
    parser = argparse.ArgumentParser(
        prog = 'CurrencyExxhangeRate.py',
        description = '''Script process a NBP's API response \n
        and return a currency exange rate''',
    )

    parser.add_argument('currencyName')
    args=parser.parse_args()

# assumption: length of columnOne and columnTwo is equal
# function is printing a table with headlines and data
def TablePrint(headlineOne:str, headlineTwo:str, columnOne:list, columnTwo:list):
    if len(columnOne) != len(columnTwo):
        # if that statement is true, its a critital error
        sys.exit(-1)
    
    iterator = 0

    print(headlineOne+"\t"+"\t"+headlineTwo)
    for iterator in range(len(columnOne)):
        print(str(columnOne[iterator])+"\t"+str(columnTwo[iterator]))

    print("")

# funcion send call to API about currnet currency exange rate 
def CurrentExangeRate(CurrencyName:str):
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{CurrencyName}/"

    try:
        # it's standard return of this function, if everything gone well
        currentExangeRate = float((json.loads(requests.get(url).text))["rates"][0]['mid'])
        print(f"Current {CurrencyName} exange rate {currentExangeRate}", end = "\n")

    except:
        # if API return an error, that excpet will return and exit from program
        print(f"currency {CurrencyName} don't exist")
        sys.exit(-1)

# funcion counts currency price changes
def Diffrence(dates:list, currencyRates:list):
    datesDiffrences = []
    ratesDiffrence = []

    # iterator = 1
    currencyLen = len(currencyRates)

    for iterator in range(1, len(currencyRates)):
        datesDiffrences.append("from "+dates[iterator-1]+" to "+dates[iterator])
        ratesDiffrence.append((currencyRates[iterator]-currencyRates[iterator-1]))

        iterator += 1
    
    # all data is transferred to TablePrint function, to be displayed as a table
    TablePrint("days", "rate change", datesDiffrences, ratesDiffrence)

def Last5DaysCurrentExangeRate(CurrencyName:str):
    lastDays = 5
    try:
        # it's standard algorithm of funcion, if everything gone well
        url = f"http://api.nbp.pl/api/exchangerates/rates/A/{CurrencyName}/last/{lastDays}/"
        fiveDaysCurrency = json.loads(requests.get(url).text)["rates"]
    
        dates = []
        currencyRates = []
        for iterator in fiveDaysCurrency:
            currencyRates.append(iterator["mid"])
            dates.append(iterator["effectiveDate"])
    
        TablePrint("Dates", "CurrencyRates", dates, currencyRates)
        Diffrence(dates, currencyRates)

    except:
        print(f"currency {CurrencyName} don't exist")
        sys.exit(-1)
    

# it's standard main function of script
if __name__ == "__main__":
    Help()

    currency = sys.argv[1]

    CurrentExangeRate(currency)
    Last5DaysCurrentExangeRate(currency)
