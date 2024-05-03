#!/bin/python3

import requests
import sys
import json

# assumption: length of columnOne and columnTwo is equal
def TablePrint(headlineOne:str, headlineTwo:str, columnOne:list, columnTwo:list):
    if len(columnOne) != len(columnTwo):
        # if that statement is true, its a critital error
        sys.exit -1
    
    iterator = 0

    print(headlineOne+"\t"+"\t"+headlineTwo)
    for iterator in range(len(columnOne)):
        print(str(columnOne[iterator])+"\t"+str(columnTwo[iterator]))
    print("")

def CurrentExangeRate(CurrencyName:str):
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{CurrencyName}/"
    return float((json.loads(requests.get(url).text))["rates"][0]['mid'])

def Diffrence(dates:list, currencyRates:list):
    datesDiffrences = []
    ratesDiffrence = []

    iterator = 1
    currencyLen = len(currencyRates)

    while iterator < currencyLen:
        datesDiffrences.append("from "+dates[iterator-1]+" to "+dates[iterator])
        ratesDiffrence.append(currencyRates[iterator-1]-currencyRates[iterator])
        iterator += 1
    
    TablePrint("days", "rate change", datesDiffrences, ratesDiffrence)

def Last5DaysCurrentExangeRate(CurrencyName:str):
    lastDays = 5
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{CurrencyName}/last/{lastDays}/"
    fiveDaysCurrency = json.loads(requests.get(url).text)["rates"]
    
    dates = []
    currencyRates = []
    for iterator in fiveDaysCurrency:
        currencyRates.append(iterator["mid"])
        dates.append(iterator["effectiveDate"])
    
    TablePrint("Dates", "CurrencyRates", dates, currencyRates)
    Diffrence(dates, currencyRates)
    

if __name__ == "__main__":
    # todo: pobieranie nazwy waluty ze standardowego wejscia
    """
    currencyName = "USD"
    currentResponse = CurrentExangeRate(currencyName)
    print(currentResponse)
    """
    Last5DaysCurrentExangeRate("USD")